def fibonacci(n):
    if n in (1, 2):
        return 1
    assert n > 1, 'Функция не может вычислить число меньше 1'
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(0.1))