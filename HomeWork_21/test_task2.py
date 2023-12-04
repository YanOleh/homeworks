import pytest
import io
from unittest.mock import patch
from task1 import FileContextManager


@pytest.fixture
def test_file_path(tmp_path):
    test_file = tmp_path / 'test_file.txt'
    with open(test_file, 'w') as file:
        file.write('Test data')
    return test_file

def test_file_context_manager_enter(test_file_path):
    with FileContextManager(test_file_path, 'r') as file:
        assert isinstance(file, io.TextIOWrapper)
        result = file.read()
        assert result == "Test data"

def test_file_context_manager_exit(test_file_path):
    with FileContextManager(test_file_path, 'r') as file:
        pass
    assert file.closed == True



