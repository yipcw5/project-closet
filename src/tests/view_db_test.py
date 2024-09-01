# Created using ChatGPT

import pytest
from unittest.mock import patch, MagicMock
import psycopg2

from constants.db_commands import *
from constants.errors import ERR_INVALID_INPUT, ERR_DB_CONN, ERR_DB_TABLES_INIT, ERR_DB_QUERY
from modules.view_db.view_db import init_db

def test_init_db_success():
    # Mock the connection and cursor objects
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch('psycopg2.connect', return_value=mock_conn):
        # Call the function
        conn, cursor = init_db()

        # Assertions
        assert conn == mock_conn
        assert cursor == mock_cursor

        # Check that the correct queries were executed
        expected_queries = [RESET_DB, INIT_TABLES, INIT_FROM_CSV, VIEW_CLOTHING_ENTRIES]
        for query in expected_queries:
            mock_cursor.execute.assert_any_call(query)

def test_init_db_connection_error():
    # Simulate a connection error
    with patch('psycopg2.connect', side_effect=psycopg2.Error("Connection failed")):
        with pytest.raises(Exception) as excinfo:
            init_db()
        assert str(excinfo.value) == f"{ERR_DB_CONN}: Connection failed"

def test_init_db_table_initialization_error():
    # Mock the connection and cursor objects
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Simulate a table initialization error
    mock_cursor.execute.side_effect = psycopg2.Error("Initialization failed")

    with patch('psycopg2.connect', return_value=mock_conn):
        with pytest.raises(Exception) as excinfo:
            init_db()
        assert str(excinfo.value) == f"{ERR_DB_TABLES_INIT}: Initialization failed"