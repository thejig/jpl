"""Test module for jpl/rules/playbook/info."""
import pytest

from jpl.rules.playbook.info import (
    PlaybookHasName,
    PlaybookHasAuthor,
    PlaybookHasDescription,
    PlaybookHasVersion,
    PlayBookExists
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
    def name_empty(self):
        self.data["name"] = ""
        return self.data

    @property
    def name_missing(self):
        self.data.pop("name")
        return self.data

    @property
    def author_empty(self):
        self.data["author"] = ""
        return self.data

    @property
    def author_missing(self):
        self.data.pop("author")
        return self.data

    @property
    def desc_empty(self):
        self.data["description"] = ""
        return self.data

    @property
    def desc_missing(self):
        self.data.pop("description")
        return self.data

    @property
    def version_empty(self):
        self.data["version"] = ""
        return self.data

    @property
    def version_missing(self):
        self.data.pop("version")
        return self.data

    @property
    def playbook_absent(self):
        self.data = None
        return self.data


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().name_empty, "FAILED"),
        (MockPlaybook().name_missing, "FAILED")
    ]
)
def test_playbook_has_name(playbook, expected):
    rule = PlaybookHasName()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().author_empty, "WARNING"),
        (MockPlaybook().author_missing, "WARNING")
    ]
)
def test_playbook_has_author(playbook, expected):
    rule = PlaybookHasAuthor()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().desc_empty, "WARNING"),
        (MockPlaybook().desc_missing, "WARNING")
    ]
)
def test_playbook_has_desc(playbook, expected):
    rule = PlaybookHasDescription()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().version_empty, "WARNING"),
        (MockPlaybook().version_missing, "WARNING")
    ]
)
def test_playbook_has_version(playbook, expected):
    rule = PlaybookHasVersion()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected


@pytest.mark.parametrize(
    "playbook, expected",
    [
        (MockPlaybook().passing, "PASSED"),
        (MockPlaybook().playbook_absent, "FAILED"),
    ]
)
def test_playbook_exists(playbook, expected):
    rule = PlayBookExists()
    result = rule.run(
        playbook=playbook
    )

    assert result == expected
