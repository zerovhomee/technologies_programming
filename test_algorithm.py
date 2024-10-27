import unittest
from memory_profiler import profile
from datetime import datetime

@profile
def search(n,k,arr):
    #assert k in arr, 'Элемент должен находиться в массиве'
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            pass
        else:
            left_part = arr[i+1:]
            right_part = arr[:i+1]

            print(left_part, right_part)

            if k <= left_part[-1]:
                low = 0
                high = len(left_part) - 1
                while low <= high:
                    mid = (low+high)//2
                    guess = left_part[mid]
                    if guess == k:
                        return  mid+(i+1)
                    if guess > k:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                low = 0
                high = len(right_part) - 1
                while low <= high:
                    mid = (low+high)//2
                    guess = right_part[mid]
                    if guess == k:
                        return mid
                    if guess > k:
                        high = mid - 1
                    else:
                        low = mid + 1

    #сначала ищем в левой части, затем в правой части и прибавляем индекс i+1 либо отнимаем за счет сьезда массива
#unittest cases

class Test(unittest.TestCase):
    def test_1(self):
       res = search(2, 5, [19, 21, 100, 101, 1, 4, 5, 7, 12])# вводим три параметра
       self.assertEqual(res, 6) # проверяем чтобы ответ совпал

    def test_2(self):
       res = search(2, 1, [5,1])
       self.assertEqual(res, 1) # проверка, что результат = 1

    def test_3(self):
       res = search(2, 5, [19, 21, 100, 101, 1, 4, 5, 7, 12])
       self.assertEqual(res, 2)
'''''

#pytest tests
def test_1():
    res = search(2, 5, [19, 21, 100, 101, 1, 4, 5, 7, 12])# вводим три параметра
    assert res == 6 # проверяем чтобы ответ совпал

def test_2():
    res = search(2, 1, [5,1])
    assert res == 1 # проверка, что результат = 1

def test_3():
    res = search(2, 5, [19, 21, 100, 101, 1, 4, 5, 7, 12])
    assert res == 2
'''
'''
length_of_array = int(input('Введите длину массива '))
number_for_search = int(input('Введите искомый элемент '))
array = list(map(int, input('Введите массив ').split()))

start = datetime.now()
print(search(length_of_array, number_for_search, array))
print(datetime.now()-start)
'''

if __name__ == "__main__":
    unittest.main()