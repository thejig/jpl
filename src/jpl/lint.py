from src.jpl import JiggyPlaybookLint


if __name__ == "__main__":
    linter = JiggyPlaybookLint(
        path="examples/jiggy-playbook.yml", verbose=True, drop_passed=True
    ).run()
