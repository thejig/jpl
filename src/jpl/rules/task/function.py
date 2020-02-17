"""JiggyPlaybook.pipeline.tasks rules."""
from src.jpl.rules.jiggyrule import JiggyRule

from src.jpl.utils.path import module_exists


class FunctionSourceExists(JiggyRule):
    """Validate task has attribute `name`"""

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

        return self.mark

    def run(self, playbook):
        return self.function_exists(playbook)


rules = [FunctionSourceExists]
