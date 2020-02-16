"""Jiggy Rule."""
import yaml

from src.jpl.rules import rules


class JiggyRule(object):
    """Base class for JiggyRule."""

    def __repr__(self):
        return "<JiggyRule: {}>".format(self.rule)

    def __verbose__(self):
        return "<JiggyRule: {} - {}>".format(self.rule, self.desc)

    def run(self, playbook):
        """Baseclass runner."""
        raise NotImplementedError()


class JiggyPlaybookLint(object):
    """Runner for jpl."""

    def __init__(self, path: str, ruleset: list, verbose=None):
        self.playbook = self._read(path)
        self.rules = ruleset
        self.resp = []
        self.verbose = verbose

    def run(self):
        linted = []
        for rule in self.rules:
            _status = rule().run(playbook=self.playbook)

            linted.append((_status, rule))

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
        for mark, rule in linted:
            rule_meta = "[{}] {}:".format(rule.rule, rule.__name__)
            if verbose:
                print("{:<30}{:<10} {}".format(rule_meta, mark, rule.message))
            else:
                print("{:<30}{:<30}".format(rule_meta, mark))

        return "Finished"

    @staticmethod
    def _pf(mark: bool):
        if mark:
            return "PASSED"
        else:
            return "FAILED"

    @staticmethod
    def _read(path: str):
        """Reader of .yml file."""
        with open(path, "r") as f:
            return yaml.full_load(f)
