import unittest
import logging

from scripts.sockets import my_socket_lib


logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
)


class TestValidConnections(unittest.TestCase):

    def test_connect_socket_pr4e(self):
        """ Test for a valid connect to pr4e. """
        my_socket_lib.connect_socket('data.pr4e.org', 'http://data.pr4e.org/page1.htm', 80)

    def test_connect_socket_google(self):
        """ Test for a valid connect to google. """
        my_socket_lib.connect_socket('google.com', 'http://google.com', 80)