import socket

import click

from .sockets import PARAM
from sockets import my_socket_lib


@click.command()
@click.argument('host', )
# @click.argument('host', help="Hostname in internet domain notation or IPv4 address.")
@click.argument('url', )
# @click.argument('url', help="The url for whose response is given.")
@click.option('--port', default=PARAM.DEF_WEB_PORT, show_default=True)
@click.option('-t', '--timeout', default=PARAM.DEF_TIMEOUT, show_default=True, )
def cli(host, url, port, timeout):
    # Configure
    socket.settimeout(timeout)
    # Connect socket
    my_socket_lib.connect_socket(host, port, url)

if __name__ == '__main__':
    cli()