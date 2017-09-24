from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Sudoku Solver',
  ext_modules = cythonize("sudoku_solver_c.pyx"),
)