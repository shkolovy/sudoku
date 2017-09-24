#import timeit


ar = [[0, 2, 0, 8, 0, 0, 0, 9, 0],
      [0, 0, 0, 1, 0, 0, 7, 0, 5],
      [0, 0, 0, 0, 4, 7, 0, 6, 0],
      [0, 0, 2, 0, 0, 0, 9, 0, 0],
      [0, 0, 0, 0, 5, 3, 0, 0, 0],
      [0, 3, 0, 4, 0, 0, 1, 0, 0],
      [9, 0, 0, 0, 0, 0, 0, 0, 6],
      [0, 0, 7, 0, 1, 0, 0, 0, 3],
      [0, 0, 3, 7, 0, 2, 0, 0, 0]]

import sudoku_solver as ss
import sudoku_solver_c as ssc
import pprint
from timeit import default_timer

# start = default_timer()
# res = ssc.solve_sudoku(ar)
# end = default_timer()
# x = float(end - start)
# print(x)


start = default_timer()
res = ss.solve_sudoku(ar)
end = default_timer()
y = float(end - start)
print(y)

#print(f"faster {x/y} times")
#pprint.pprint(res)

#pprint.pprint(ssc.solve_sudoku(ar))



# cy = timeit.timeit("ct.fun(1,2)", setup="import cython_test as ct", number=2)
# py = timeit.timeit("ct.fun(1,2)", setup="import python_test as ct", number=2)

# print(cy, py)
# print(f"cython faster {py/cy} times")

