# Необходимо сравнить скорость работы 2 алгоритмов вычисления чисел
# Фибоначчи и определить, какой из них работает быстрее. Так различия
# начнутся уже с 40 члена последовательности.
import time


def fibonacci(n):
    if n in (1, 2):
        return n - 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    fib1, fib2 = 0, 1
    if n == 1:
        print(fib1, end=" ")
    elif n >= 2:
        print(fib1, fib2, end=" ")
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=" ")


n = 35
start_time = time.time()
for i in range(1, n + 1):
    print(f"{i}: {fibonacci(i)}", end=" ")
end_time = time.time()
print()
print(f"{(end_time - start_time) * 10 ** 3:.03f},s")
print()
start_time = time.time()
fibonacci2(n)
end_time = time.time()
print()
print(f"{(end_time - start_time) * 10 ** 3:.03f},s")
