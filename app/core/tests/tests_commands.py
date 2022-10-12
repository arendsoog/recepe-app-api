""" Test custom Django management commands"""

from dbm import _Database
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_Command.check')
class CommandTest(SimpleTestCase):
    """ Test commands"""

    def test_wait_for_db_ready(self, pached_check):
        """Test waiting for database if database is ready"""
        pached_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])


