"""Jiggy Rule."""
import yaml

from jpl.rules import PlayBookExists, rules, task_rules


class JiggyPlaybookLint(object):  # pragma no cover
    """Runner for jpl."""

    def __init__(self, path: str, skip=None):
        self.playbook = self._read(path)
        self.skip = skip

    def run(self):
        """Runner for JiggyPlaybookLinter."""
        pbe = PlayBookExists()
        exists = pbe.run(self.playbook)
        if exists == "FAILED":
            return [(exists, pbe, None)]

        linted = []
        for rule in rules:
            init_rule = rule()

            _status = init_rule.run(playbook=self.playbook)

            linted.append((_status, init_rule, None))

        for task in self.playbook.get("pipeline", {}).get("tasks"):
            for rule in task_rules:
                init_rule = rule()

                _status = init_rule.run(playbook=task)
                linted.append((_status, init_rule, task.get("name")))

        if self.skip:
            linted = [rule for rule in linted if rule[0] != "PASSED"]

        return linted

    @staticmethod
    def _read(path: str):  # pragma no cover
        """Reader of .yml file."""
        with open(path, "r") as f:
            return yaml.full_load(f)
