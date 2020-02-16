from src.jpl import JiggyPlaybookLint
from src.jpl.rules import rules


if __name__ == "__main__":
    linter = JiggyPlaybookLint(path="examples/jiggy-playbook.yml", ruleset=rules).run()
