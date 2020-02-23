"""Test module for jpl/utils."""
import json
import os
import pytest

from jpl.utils.path import (
    file_exists,
    module_exists
)


@pytest.mark.parametrize(
    "fin, expected",
    [
        ("../examples/jiggy-playbook.yml", True),
        ("../exmaples/something_else", False),
        ("../examples/", True)
    ]
)
def test_file_exists(fin, expected):
    """Test utils.path file_exists."""

    assert file_exists(fin) == expected


@pytest.mark.parametrize(
    "fin, expected",
    [
        ("jpl.rules.pipeline.pipeline.PipelineHasRunner", True),
        ("jpl.functions.Something", False),
    ]
)
def test_module_exists(fin, expected):
    """Test utils.path module_exists"""
    assert module_exists(fin) == expected


#################
# TESTING UTILS #
#################

def load_from_json(fp: str):
    in_file = os.path.join(os.path.dirname(__file__), fp)
    with open(in_file) as f:
        raw_json = f.read()
        return json.loads(raw_json)