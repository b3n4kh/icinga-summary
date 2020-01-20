import click
from icinga2ve.summary import main
import socket


@click.group(invoke_without_command=True)
@click.option('--debug/--no-debug', default=False)
@click.option('--basicauth/--no-basicauth', default=True)
@click.option('--host', default=socket.getfqdn())
@click.pass_context
def cli(ctx, debug, basicauth, host):
    """CLI Entrypoint."""
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    main(host=host, basicauth=basicauth)


@cli.command()
@click.pass_context
def api(ctx):
    """Raw API Mode."""
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))


if __name__ == '__main__':
    cli(obj={})
