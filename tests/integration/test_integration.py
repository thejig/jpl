"""Integration test modules."""
import pytest

from unittest import TestCase

from jpl import JiggyPlaybookLint


class TestJiggyPlaybookLintEmpty(TestCase):
    """Integration test client (empty)."""
    def setUp(self):
        """Build JiggyPlaybookLintClient."""
        self.empty_jpl = JiggyPlaybookLint(
            path="../examples/jiggy-playbook-empty.yml"
        )

    def test_validate(self):
        """Emptry TestCase for jpl."""
        validity_result, jpl_response = self.empty_jpl.validate()

        assert validity_result is False
        assert len(jpl_response) == 1


class TestJiggyPlaybookLintPassing(TestCase):
    """Integration test client (passing)."""
    def setUp(self):
        """Build JiggyPlaybookLintClient."""
        self.passing_jpl = JiggyPlaybookLint(
            path="../examples/jiggy-playbook-passing.yml"
        )

    def test_validate(self):
        """Passing TestCase for jpl."""
        validity_result, jpl_response = self.passing_jpl.validate()

        assert validity_result is True
        assert not jpl_response


class TestJiggyPlaybookLintBasic(TestCase):
    """Integration test client (basic)."""
    def setUp(self):
        """Build JiggyPlaybookLintClient."""
        self.basic_jpl = JiggyPlaybookLint(
            path="../examples/jiggy-playbook.yml",
            allow_warning=False,
        )

    def test_validate(self):
        """Basic TestCase for jpl."""
        validity_result, jpl_response = self.basic_jpl.validate()

        assert validity_result is False
        assert len(jpl_response) == 7


class TestJiggyPlaybookLintComplex(TestCase):
    """Integration test client (basic)."""
    def setUp(self):
        """Build JiggyPlaybookLintClient."""
        self.complex_jpl = JiggyPlaybookLint(
            path="../examples/jiggy-playbook-flawed.yml",
            allow_warning=False,
        )

    def test_validate(self):
        """Basic TestCase for jpl."""
        validity_result, jpl_response = self.complex_jpl.validate()

        assert validity_result is False
        assert len(jpl_response) == 15