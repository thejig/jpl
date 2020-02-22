"""Jiggy Playbook Lint Command Line Interface"""
import click
import jpl

import jpl.cli.config as config


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
def lint(verbose, show, playbook):  # pragma no cover
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

    linted = jpl.JiggyPlaybookLint(path=playbook).run()
    generate_jpl_report(linted=linted, show=show, verbose=verbose)


def generate_jpl_report(
        linted: list, show: bool, verbose=None, passing=True
):  # pragma no cover
    """
    Generate `Click` response for jpl linter.

    Args:
        linted: (list) - array of JiggyRule response objects
        show: (bool) - boolean flag to show "PASSED" rules in CLI
        verbose: (count) - flag to denote response with verbosity
        passing: (bool) - indicator for CLI success message

    Returns:
         click.echo - `with style`
    """
    for rule in linted:
        rule_meta = "[{}] {}:".format(rule.rule, rule.__class__.__name__)
        if rule.task:
            rule_meta = "[{}] {} - {}:".format(
                rule.rule, rule.__class__.__name__, rule.task
            )

        if show and rule.mark == "PASSED":
            continue

        passing = False
        resp = "{:<50}{:<30}".format(
            rule_meta,
            click.style(rule.mark, bold=True, fg=config.MARK_TO_COLOR.get(rule.mark)),
        )

        if verbose:
            resp = "{} {}".format(resp, rule.message)

        click.echo(resp)

    if passing:
        click.echo(
            click.style(
                "All checks passed - Time to get jiggy wit' it!", fg="green"
            )
        )

    return exit()
