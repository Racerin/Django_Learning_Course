import click

from lib import sockets

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello.")

@cli.command()
def simple_web_browser_example():
    click.echo(sockets.read_webpage_example())

@cli.command()
def web_server_example():
    sockets.web_server()


if __name__ == "__main__":
    cli()