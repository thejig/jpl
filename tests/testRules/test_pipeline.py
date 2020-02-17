"""Test module for jpl/rules/pipeline/pipeline."""
import pytest

from jpl.rules.pipeline.pipeline import (
    PipelineHasTasks,
    PipelineHasRunner,
    RunnerIsSupported,
    SecretsHasMetadata,
    SecretsLocationExists,
)

from tests.test_utils import load_from_json


class MockPlaybook:
    def __init__(self):
        self.data = load_from_json(
            fp="testData/playbook.json"
        )

    @property
    def passing(self):
        return self.data

    @property
    def runner_missing(self):
        self.data["pipeline"]["runner"] = None
        return self.data

    @property
    def runner_not_supported(self):
        self.data["pipeline"]["runner"] = "dask"
        return self.data

    @property
    def secrets_list(self):
        self.data["pipeline"]["secrets"] = ["somelist"]
        return self.data

    @property
    def secrets_location(self):
        self.data["pipeline"]["secrets"].pop("location")
        return self.data

    @property
    def secrets_loc_nonexistent(self):
        self.data["pipeline"]["secrets"]["location"] = (
            "some.wrong.file.path"
        )
        return self.data

    @property
    def secrets_source(self):
        self.data["pipeline"]["secrets"].pop("source")
        return self.data

    @property
    def tasks_missing(self):
        self.data["pipeline"].pop("tasks")
        return self.data


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().runner_missing, "WARNING")
    ]
)
def test_pipeline_has_runner(playbook, expected):
    rule = PipelineHasRunner()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().runner_not_supported, "FAILED")
    ]
)
def test_runner_is_supported(playbook, expected):
    rule = RunnerIsSupported()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().secrets_list, "FAILED"),
        (MockPlaybook().secrets_location, "FAILED"),
        (MockPlaybook().secrets_source, "FAILED")
    ]
)
def test_secrets_metadata(playbook, expected):
    rule = SecretsHasMetadata()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().secrets_loc_nonexistent, "FAILED"),
    ]
)
def test_secrets_location_exists(playbook, expected):
    rule = SecretsLocationExists()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().tasks_missing, "FAILED"),
    ]
)
def test_pipeline_has_tasks(playbook, expected):
    rule = PipelineHasTasks()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected
