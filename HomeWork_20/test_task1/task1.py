import pytest
from HomeWork_20.test_task1.function import with_index

def test_with_index():
    iterable_list = ['a', 'b', 'c']
    result_list = list(with_index(iterable_list))
    assert result_list == [(0, 'a'), (1, 'b'), (2, 'c')]