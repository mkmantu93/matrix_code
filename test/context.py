# See https://docs.python-guide.org/writing/structure/#test-suite
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.matrix_calc import Matrix