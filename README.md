# <p align="center"> JiggyPlaybookLinter </p>

<p align="center">
<a href="https://travis-ci.com/thejig/jpl"><img alt="Build Status" src="https://travis-ci.com/thejig/jpl.svg?branch=master"></a>
<a href="https://coveralls.io/github/thejig/jpl?branch=master"><img alt="Coverage Status" src="https://coveralls.io/repos/github/thejig/jpl/badge.svg?branch=master"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pypi.org/project/jpl/"><img alt="PyPI" src="https://img.shields.io/pypi/v/jpl"></a>
</p>


## Description
Use Jiggy? Want to validate your playbook before deploying a pipeline?
`jpl` or the `JiggyPlaybookLinter` allows you to validate your JiggyPlaybook outside of an execution.


## Installation
From Source
```bash
$ git clone https://github.com/thejig/jpl.git
$ cd jpl
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -e .
```

From Build
```bash
$ pip install jpl
```

## Usage
Via CLI
* `jpl` has a CLI for easy usage
```bash
$ jpl --help

Usage: jpl [OPTIONS]

  Click CLI entrypoint to run JiggyPlaybookLint.

  CLI Args:
  -v --verbose: Run `jpl` with verbosity.
  -s --skip: Skip "PASSED" rules in JiggyPlaybookLint Report.
  -p --playbook: Location of JiggyPlaybook to lint.

  Returns:

      click.echo - `with style`

Options:
  -v, --verbose        Run `jpl` with verbosity.
  -s, --skip           Skip `PASSED` rules in jpl report
  -p, --playbook TEXT  Filepath to Jiggy Playbook  [required]
  --help               Show this message and exit.
```

A minimal test case
```bash
$ jpl -v -p examples/jiggy-playbook.yml
   __        ______      __
  /\ \      /\  == \    /\ \
 _\_\ \     \ \  _-/    \ \ \____
/\_____\     \ \_\       \ \_____\
\/_____/iggy  \/_/laybook \/_____/inter

[F01] FunctionSourceExists - get-weekday:         FAILED      Declared path to function: `examples.utils.dates.GetWeekdayTask` does not exist.

```

Via python client with `.validate()`
```python
import jpl

>>> client = jpl.JiggyPlaybookLint(path="path/to/playbook")
>>> result = client.validate()
```

The `validate()` method will return a `tuple`

The tuple denotes the validity of the playbook and the failing rules as `JiggyRule` objects
```bash
(False, [<JiggyRule: F01>, <JiggyRule: F01>, <JiggyRule: F01>, <JiggyRule: F01>, <JiggyRule: F01>, <JiggyRule: F01>])
```

## Overview
A `JiggyPlaybook` is broken down into chunks

* Playbook 
    * The entire `.yml` constitutes the "playbook"

* Pipeline
    * The key `pipeline` including all `tasks` constitutes the "pipeline"

* Task
    * Tasks are chunks of a pipeline having the below attributes:
        * `name`
        * `description`
        * `function` which contains `source`, `params`, `output`
        * `requires`

```yaml
name: Hello, world!
author: me@jiggy.dev
description: Show off the usage of jpl
version: 0.0.1

pipeline:
  runner: sequential
  secrets:
    location: examples/secrets/.env-example
    source: jiggy.EnvSecrets
  tasks:

  - name: print-something
    description: Print something
    function:
      source: examples.utils.string_manipulation.PrintThis
      params:
      - type: str
        value: 'THIS PIPELINE IS GREAT'
      output: null
    requires: null

```

## Rules
### Etymology:
`JiggyRule` - JiggyRule.rule consists of 3 characters (i.e.) `X01`


* X: (char) - letter describes corresponding ruleset

* 0: (digit) - incrementing based on third digit

* 0: (digit) - incrementing


Examples:

Rule: `PlaybookHasName`

* rule.rule = I (info) 0 (base 10) 1 (rule number 1)

Rule: `PipelineHasDescription`

* rule.rule = P (pipeline) 0 (base 10) 1 (rule number 1)
