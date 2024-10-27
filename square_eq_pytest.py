import pytest

from math import sqrt

# функция вычисления квадратного корня
def square_eq_solver(a, b, c):
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant == 0:
       result.append(-b / (2 * a))
   else:
      result.append((-b + sqrt(discriminant)) / (2 * a))
      result.append((-b - sqrt(discriminant)) / (2 * a))


   return result

def test_no_root():
   res = square_eq_solver(10, 0, 2)
   assert len(res) == 0

def test_single_root():
   res = square_eq_solver(10, 0, 0)
   assert len(res) == 1
   assert res == [0]

def test_multiple_root():
   res = square_eq_solver(2, 5, -3)
   assert len(res) == 2
   assert res == [0.5, -3]
