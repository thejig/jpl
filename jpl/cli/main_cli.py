"""Jiggy Playbook Lint Command Line Interface"""
import click
import jpl

MARK_TO_COLOR = {"PASSED": "green", "WARNING": "yellow", "FAILED": "red"}


@click.command()
@click.option(
    "-v", "--verbose", required=False, count=True, help="Run `jpl` with verbosity."
)
@click.option(
    "-s",
    "--show",
    required=False,
    is_flag=True,
    default=True,
    help="Show `PASSED` rules in jpl report",
)
@click.option("-p", "--playbook", required=True, help="Filepath to Jiggy Playbook")
def lint(verbose, show, playbook):
    """Click CLI entrypoint to run JiggyPlaybookLint.

    CLI Args:

    -v --verbose: Run `jpl` with verbosity.

    -s --show: Show "PASSED" rules in JiggyPlaybookLint Report.

    -p --playbook: Location of JiggyPlaybook to lint.


    Returns:

        click.echo - `with style`
    """
    click.echo(
        """
   __        ______      __        
  /\ \      /\  == \    /\ \       
 _\_\ \     \ \  _-/    \ \ \____  
/\_____\     \ \_\       \ \_____\ 
\/_____/iggy  \/_/laybook \/_____/inter            
        """
    )
    linted = jpl.JiggyPlaybookLint(path=playbook, show=show).run()

    generate_jpl_report(linted=linted, verbose=verbose)


def generate_jpl_report(linted: list, verbose=None):  # pragma no cover
    """
    Generate `Click` response for jpl linter.

    Args:
        linted: (list) - array of JiggyRule response objects
        verbose: (count) - flag to denote response with verbosity

    Returns:
         click.echo - `with style`
    """
    for rule in linted:
        rule_meta = "[{}] {}:".format(rule.rule, rule.__class__.__name__)
        if rule.task:
            rule_meta = "[{}] {} - {}:".format(
                rule.rule, rule.__class__.__name__, rule.task
            )

        if verbose == 1:
            click.echo(
                "{:<50}{:<20} {}".format(
                    rule_meta,
                    click.style(rule.mark, fg=MARK_TO_COLOR.get(rule.mark)),
                    rule.message,
                )
            )
        elif verbose > 1:
            click.echo(
                "{:<50}{:<20} {} \nPriority: `{}` - Description: `{}`\n".format(
                    rule_meta,
                    click.style(rule.mark, fg=MARK_TO_COLOR.get(rule.mark)),
                    rule.message,
                    rule.priority,
                    rule.description,
                )
            )
        else:
            click.echo(
                "{:<50}{:<50}".format(
                    rule_meta, click.style(rule.mark, fg=MARK_TO_COLOR.get(rule.mark))
                )
            )

    return exit()
