import pytest
# from src.matrix_calc import Matrix
import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from context import Matrix

def test_matrix_addition():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1 + m2
    assert result.data == [[6, 8], [10, 12]]

def test_matrix_subtraction():
    m1 = Matrix([[5, 6], [7, 8]])
    m2 = Matrix([[1, 2], [3, 4]])
    result = m1 - m2
    assert result.data == [[4, 4], [4, 4]]

def test_invalid_addition():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2]])
    with pytest.raises(ValueError):
        _ = m1 + m2

def test_invalid_subtraction():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2]])
    with pytest.raises(ValueError):
        _ = m1 - m2
