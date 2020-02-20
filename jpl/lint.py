import jpl

if __name__ == "__main__":
    client = jpl.JiggyPlaybookLint(path="examples/jiggy-playbook-flawed.yml")
    result = client.run()
