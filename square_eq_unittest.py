import unittest
from math import sqrt

# функция вычисления квадратного корня
def square_eq_solver(a, b, c):
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant == 0:
       result.append(-b / (2 * a))
   elif discriminant > 0:
      result.append((-b + sqrt(discriminant)) / (2 * a))
      result.append((-b - sqrt(discriminant)) / (2 * a))


   return result

# unittest
class SquareEqSolverTestCase(unittest.TestCase):
    def test_no_root(self):
       res = square_eq_solver(10, 0, 2)# вводим три параметра
       self.assertEqual(len(res), 0) # проверяем чтобы не было корней

    def test_single_root(self):
       res = square_eq_solver(10, 0, 0)
       self.assertEqual(len(res), 1)
       self.assertEqual(res, [0]) # проверка, что результат = 0

    def test_multiple_root(self):
       res = square_eq_solver(2, 5, -3)
       self.assertEqual(len(res), 2)
       self.assertEqual(res, [0.5, -3])# проверка, что здесь два корня = 0.5, -3

if __name__ == '__main__':
    unittest.main()
