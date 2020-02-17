"""Test module for jpl/rules/task/task."""
import pytest

from jpl.rules.task.task import (
    TaskHasName,
    TaskHasDescription,
    TaskHasFunction
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
    def name_empty(self):
        self.data["name"] = ""
        return self.data

    @property
    def name_missing(self):
        self.data.pop("name")
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
    def function_missing(self):
        self.data.pop("function")
        return self.data



@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().name_empty, "FAILED"),
        (MockTask().name_missing, "FAILED")
    ]
)
def test_task_has_name(task, expected):
    rule = TaskHasName()
    result = rule.run(
        playbook=task
    )

    assert result == expected


@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().desc_empty, "WARNING"),
        (MockTask().desc_missing, "WARNING")
    ]
)
def test_task_has_desc(task, expected):
    rule = TaskHasDescription()
    result = rule.run(
        playbook=task
    )

    assert result == expected


@pytest.mark.parametrize(
    "task, expected",
    [
        (MockTask().passing, "PASSED"),
        (MockTask().function_missing, "FAILED")
    ]
)
def test_task_has_function(task, expected):
    rule = TaskHasFunction()
    result = rule.run(
        playbook=task
    )

    assert result == expected
