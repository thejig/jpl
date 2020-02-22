"""Test module for jpl/rules/task/function."""
import pytest

from jpl.rules.task.function import (
    FunctionSourceExists,
    ParamHasType,
    ParamHasValue,
    FunctionOutputObject
)

from tests.test_utils import load_from_json


class MockTask:
    def __init__(self):
        self.data = load_from_json(
            fp="testData/task.json"
        )

    @property
    def passing(self):
        return self.data

    @property
    def source_nonexist(self):
        self.data["function"]["source"] = "i.dont.exist"
        return self.data

    @property
    def source_missing(self):
        self.data["function"]["source"] = None
        return self.data

    @property
    def type_missing(self):
        self.data["function"]["params"][0]["type"] = None
        return self.data

    @property
    def value_missing(self):
        self.data["function"]["params"][0]["value"] = None
        return self.data

    @property
    def output_list(self):
        self.data["function"]["output"] = ["someList"]
        return self.data


@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().source_nonexist, "FAILED"),
        (MockTask().source_missing, "FAILED")
    ]
)
def test_function_source_exists(task, expected):
    rule = FunctionSourceExists()
    result = rule.run(
        playbook=task
    )

    assert result == expected


@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().type_missing, "FAILED"),
    ]
)
def test_param_has_type(task, expected):
    rule = ParamHasType()
    result = rule.run(
        playbook=task
    )

    assert result == expected


@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().value_missing, "FAILED"),
    ]
)
def test_param_has_value(task, expected):
    rule = ParamHasValue()
    result = rule.run(
        playbook=task
    )

    assert result == expected


@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().output_list, "FAILED"),
    ]
)
def test_output_is_singular(task, expected):
    rule = FunctionOutputObject()
    result = rule.run(
        playbook=task
    )

    assert result == expected
