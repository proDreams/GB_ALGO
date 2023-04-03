# start = time.time()
# end = time.time()
# print(f"{(end - start) * 10 ** 3:.03f}ms")

# напишем игру Угадай число
# пользователь вводит максимальный потолок значений
# например 1000
# компьютер загадывает число
# напишите три разных алгоритма поиска этого числа
# оценить их сложность
import random
import time

number = int(input('Введите число до какого загадать число: '))
secret_num = random.randint(0, number)
start_time = time.time()
for i in range(number):
    if i == secret_num:
        print(f"Загаданное число: {i}")
        end_time = time.time()
        print(f"{(end_time - start_time) * 10 ** 3:.03f},s")
        break

start_time = time.time()
while True:
    user_num = random.randint(0, number)
    if user_num == secret_num:
        print(f"Загаданное число: {user_num}")
        end_time = time.time()
        print(f"{(end_time - start_time) * 10 ** 3:.03f},s")
        break

start_time = time.time()
count = 0
left = 0
right = number
while True:
    user_num = (right + left) // 2
    count += 1
    if user_num == secret_num:
        print(f"Загаданное число: {user_num}")
        end_time = time.time()
        print(f"{(end_time - start_time) * 10 ** 3:.03f},s")
        print(count)
        break
    elif secret_num < user_num:
        right = user_num - 1
    else:
        left = user_num + 1
