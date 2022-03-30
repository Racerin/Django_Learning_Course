import socket

import click

from sockets import my_socket_lib

@click.command()
def cli():
    my_socket_lib.create_server()

if __name__ == "__main__":
    cli()