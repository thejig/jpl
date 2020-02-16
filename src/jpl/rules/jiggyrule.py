"""A base class for JiggyRule."""


class JiggyRule(object):
    """Base class for JiggyRule."""

    def __repr__(self):
        return "<JiggyRule: {}>".format(self.rule)

    def __verbose__(self):
        return "<JiggyRule: {} - {}>".format(self.rule, self.desc)

    def run(self, playbook):
        """Baseclass runner."""
        raise NotImplementedError()
