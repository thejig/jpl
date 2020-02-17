"""JiggyPlaybook.pipeline.tasks rules."""
from jpl.rules.jiggyrule import JiggyRule

from jpl.utils.path import module_exists


class FunctionSourceExists(JiggyRule):
    """Validate task.function has attribute `name`"""

    rule = "F01"
    description = "Validate `JiggyPlaybook.pipeline.task.function` exists."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    def function_exists(self, task):
        this_func = task.get("function", {})
        function_loc = this_func.get("source")
        if function_loc:
            _exists = module_exists(function_loc)
            if not _exists:
                self.mark = "FAILED"
                self.message = "Declared path to function: `{}` does not exist.".format(
                    function_loc
                )

        elif not function_loc:
            self.mark = "FAILED"
            self.message = "Function: `{}` missing attribute `source`.".format(
                function_loc
            )

        return self.mark

    def run(self, playbook):
        return self.function_exists(playbook)


class ParamHasType(JiggyRule):
    """Validate task.function.prams has attribute `type`."""

    rule = "F02"
    description = "Validate `JiggyPlaybook.pipeline.task.function.params` has `type`."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    def param_has_attr_type(self, task):
        """Validate functino.params has `type` if exists."""
        this_func = task.get("function", {})
        params = this_func.get("params", [])
        if params:
            for param in params:
                if not param.get("type"):
                    self.mark = "FAILED"
                    self.message = "Function: `{}` missing required argument `type`.".format(
                        this_func.get("source").split(".", -1)[-1]
                        if this_func.get("source")
                        else None
                    )

        return self.mark

    def run(self, playbook):
        return self.param_has_attr_type(playbook)


class ParamHasValue(JiggyRule):
    """Validate task.function.prams has attribute `value`."""

    rule = "F03"
    description = "Validate `JiggyPlaybook.pipeline.task.function.params` has `value`."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    def param_has_attr_value(self, task):
        """Validate functino.params has `value` if exists."""
        this_func = task.get("function", {})
        params = this_func.get("params", [])
        if params:
            for param in params:
                if not param.get("value"):
                    self.mark = "FAILED"
                    self.message = "Function: `{}` missing required argument `value`.".format(
                        this_func.get("source").split(".", -1)[-1]
                        if this_func.get("source")
                        else None
                    )

        return self.mark

    def run(self, playbook):
        return self.param_has_attr_value(playbook)


class FunctionOutputIsSingular(JiggyRule):
    """Validate task.function.prams has `type` and `value`"""

    rule = "F04"
    description = "Validate `JiggyPlaybook.pipeline.task.function.output` is singular."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    def validate_func_has_value(self, task):
        """Validate functino.params has type and value if exists."""
        this_func = task.get("function", {})
        output = this_func.get("output")
        if output:
            if not isinstance(output, dict):
                self.mark = "FAILED"
                self.message = "Function {}: should return at most one value.".format(
                    this_func.get("source").split(".", -1)[-1]
                    if this_func.get("source")
                    else None
                )

        return self.mark

    def run(self, playbook):
        return self.validate_func_has_value(playbook)


rules = [
    FunctionSourceExists,
    ParamHasType,
    ParamHasValue,
    FunctionOutputIsSingular,
]
