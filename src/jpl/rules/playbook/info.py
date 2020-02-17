"""JiggyPlaybook rules."""
from src.jpl.rules.jiggyrule import JiggyRule


class PlaybookHasName(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `name`"""

    rule = "I01"
    description = "Validate `JiggyPlaybook` has attribute `name`"
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def has_name(playbook):
        if not playbook.get("name"):
            PlaybookHasName.mark = "FAILED"
            PlaybookHasName.message = "Playbook `name` has not been declared."

        return PlaybookHasName.mark

    def run(self, playbook):
        return self.has_name(playbook)


class PlaybookHasAuthor(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `author`"""

    rule = "I02"
    description = "Validate `JiggyPlaybook` has attribute `author`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def has_author(playbook):
        if not playbook.get("author"):
            PlaybookHasAuthor.mark = "WARNING"
            PlaybookHasAuthor.message = "Playbook `author` has not been declared."

        return PlaybookHasAuthor.mark

    def run(self, playbook):
        return self.has_author(playbook)


class PlaybookHasDescription(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `author`"""

    rule = "I03"
    description = "Validate `JiggyPlaybook` has attribute `description`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def has_desc(playbook):
        if not playbook.get("description"):
            PlaybookHasDescription.mark = "WARNING"
            PlaybookHasDescription.message = (
                "Playbook `description` has not been declared."
            )

        return PlaybookHasDescription.mark

    def run(self, playbook):
        return self.has_desc(playbook)


class PlaybookHasVersion(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `author`"""

    rule = "I04"
    description = "Validate `JiggyPlaybook` has attribute `version`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""

    @staticmethod
    def has_version(playbook):
        if not playbook.get("version"):
            PlaybookHasVersion.mark = "WARNING"
            PlaybookHasVersion.message = "Playbook `version` has not been declared."

        return PlaybookHasVersion.mark

    def run(self, playbook):
        return self.has_version(playbook)


rules = [PlaybookHasName, PlaybookHasAuthor, PlaybookHasDescription, PlaybookHasVersion]
