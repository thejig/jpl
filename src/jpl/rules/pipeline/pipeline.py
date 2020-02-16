from enum import Enum
from src.jpl.rules.jiggyrule import JiggyRule


class ExtendedEnum(Enum):
    """Enum for Jiggy.Runner types."""

    @classmethod
    def list(cls):
        """List ExtendedEnum for runner types."""
        return list(map(lambda c: c.value, cls))


class Runner(ExtendedEnum):
    """Runner Objects"""

    PARALLEL_RUNNER = "parallel"
    SEQUENTIAL_RUNNER = "sequential"


class PipelineHasRunner(JiggyRule):
    """Validate `JiggyPlaybook.pipeline` declared `runner` exists"""

    rule = "005"
    description = "Validate `pipeline` declares `runner`"
    priority = "medium"  # NOTE this will get defaulted otherwise
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def validate_runner(playbook):
        pipeline = playbook.get("pipeline", {})

        if not pipeline.get("runner"):
            PipelineHasRunner.mark = "WARNING"
            PipelineHasRunner.message = "Pipeline Runner set to `sequential`"

        return PipelineHasRunner.mark

    def run(self, playbook):
        return self.validate_runner(playbook)


class RunnerIsSupported(JiggyRule):
    """Validate `JiggyPlaybook.pipeline.runner` is supported"""

    rule = "006"
    description = "Validate `runner` is supported by Jiggy"
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def validate_runner_supported(playbook):
        pipeline = playbook.get("pipeline", {})
        runner = pipeline.get("runner")

        if not runner.lower() in [jr.value for jr in Runner]:
            RunnerIsSupported.mark = "FAILED"
            RunnerIsSupported.message = "Declared Runner: `{}` not supported by Jiggy.".format(
                runner
            )

        return RunnerIsSupported.mark

    def run(self, playbook):
        return self.validate_runner_supported(playbook)


class SecretsHasMetadata(JiggyRule):
    """Validate `JiggyPlaybook.pipeline.secrets` has relevant metadata"""

    rule = "007"
    description = "Validate `secrets` has mandatory metadata."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def validate_runner_supported(playbook):
        """Check `secrets` metadata if exists for mandatory fields."""
        MANDATORY_KEYS = ["location", "source"]

        pipeline = playbook.get("pipeline", {})
        secrets = pipeline.get("secrets")

        if secrets:
            if not isinstance(secrets, dict):
                SecretsHasMetadata.message = "Invalid `secrets` declaration."
                SecretsHasMetadata.mark = "FAILED"
            else:
                if not all(key in secrets.keys() for key in MANDATORY_KEYS):
                    SecretsHasMetadata.message = "`location` and `source` are mandatory in `secrets` declaration."
                    SecretsHasMetadata.mark = "FAILED"

        return SecretsHasMetadata.mark

    def run(self, playbook):
        return self.validate_runner_supported(playbook)


rules = [PipelineHasRunner, RunnerIsSupported, SecretsHasMetadata]
