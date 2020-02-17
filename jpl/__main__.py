#!/usr/bin/env python
# NOTE: this is temporary runner
import os
import sys

import jpl


if sys.path[0] == "" or sys.path[0] == os.getcwd():
    sys.path.pop(0)


if __name__ == "__main__":
    if not sys.argv[-1].endswith(".yml"):
        print("Please enter filepath to .yml")
        sys.exit()
    else:
        jpl.JiggyPlaybookLint(path=sys.argv[-1], verbose=True, drop_passed=True).run()
