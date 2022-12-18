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

@cli.command()
@click.argument('port', type=int)
def ip_port_available(port):
    # click.echo("Yes") if sockets.is_port_available(port) else click.echo("No")
    if sockets.is_port_available(port):
        click.echo("Yes") 
    else:
        click.echo("No")


if __name__ == "__main__":
    cli()