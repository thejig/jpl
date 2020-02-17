"""Jiggy Rule."""
import yaml

from src.jpl.rules import rules
from src.jpl.rules import task_rules


class JiggyPlaybookLint(object):
    """Runner for jpl."""

    def __init__(self, path: str, skip=None, drop_passed=None, verbose=None):
        self.playbook = self._read(path)
        self.skip = skip
        self.drop_passed = drop_passed
        self.verbose = verbose

    def run(self):
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

        if self.drop_passed:
            linted = [rule for rule in linted if rule[0] != "PASSED"]

        print(
            """
   __        ______      __        
  /\ \      /\  == \    /\ \       
 _\_\ \     \ \  _-/    \ \ \____  
/\_____\     \ \_\       \ \_____\ 
\/_____/iggy  \/_/laybook \/_____/inter            
            """
        )

        return self._parse_linted(linted=linted, verbose=self.verbose)

    @staticmethod
    def _parse_linted(linted: list, verbose=None):
        """
        Parse rule responses to generate response object
        :param linted:
        :return:
        """
        for mark, rule, task_name in linted:
            rule_meta = "[{}] {}:".format(rule.rule, rule.__class__.__name__)
            if task_name:
                rule_meta = "[{}] {} - {}:".format(
                    rule.rule, rule.__class__.__name__, task_name
                )

            if verbose:
                print("{:<50}{:<10} {}".format(rule_meta, mark, rule.message))
            else:
                print("{:<50}{:<50}".format(rule_meta, mark))

        return "Done !!"

    @staticmethod
    def _read(path: str):
        """Reader of .yml file."""
        with open(path, "r") as f:
            return yaml.full_load(f)
