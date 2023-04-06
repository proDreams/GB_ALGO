# Очередь — это абстрактный тип данных, который реализует понятие "первым пришел,
# первым вышел" (FIFO, First-In-First-Out).
# Элементы добавляются в конец очереди, и извлекаются только с начала.
#
# Очередь часто используется в системах, где требуется обрабатывать элементы в порядке их поступления,
# например, в очереди задач на выполнение в операционной системе.
#
# Для очереди необходимо реализовать следующие операции:
#
# enqueue (добавление элемента в очередь) - добавляет элемент в конец очереди.
# dequeue (удаление элемента из очереди) - удаляет элемент с начала очереди.
# peek (просмотр элемента в начале очереди) - возвращает элемент в начале очереди без его удаления.
# clear - очистка очереди.
# len - получение текущего количества элементов в очереди.
# Реализуйте очередь с помощью python list. В зависимости от выбранного вами начала и конца очереди,
# в виде комментария укажите сложность операций:
#
# enqueue
# dequeue
# peek
# dequeue
# len
# Например,
#
# ...
# def dequeue(self):  # O(...)
#     ...
# При решении нельзя пользоваться готовой структурой данных очередь.
import random
import time

from src.Seminar2.sort import Queue

q = Queue()


# q.queue = [1, 6, 5, 3, 8, 6, 9, 3, 5]
# print(q)
# print(q.counting_sort())


# for i in range(5):
#     q.enqueue(i)
# print(q)
# q.bubble_sort()
# q.quick_sort(0, len(q.queue) - 1)
# print(q)


def speed_compare():
    # q.queue = [1, 6, 5, 3, 8, 6, 9, 3, 5] * 3000
    # start1 = time.time()
    # q.bubble_sort()
    # end1 = time.time()
    # first = end1 - start1
    # print(f"Сортировка пузырьком {round(first, 3)}")
    temp = [random.randint(0, 100000000) for _ in range(1000000)]
    q.queue = temp[:]
    # q.queue = [1, 6, 5, 3, 8, 6, 9, 3, 5] * 100000
    start2 = time.time()
    q.quick_sort(0, len(q.queue) - 1)
    end2 = time.time()
    second = end2 - start2
    print(f"Быстрая сортировка {round(second, 3)}")
    # q.queue = [1, 6, 5, 3, 8, 6, 9, 3, 5] * 100000
    q.queue = temp[:]
    start3 = time.time()
    q.counting_sort()
    end3 = time.time()
    third = end3 - start3
    print(f"Сортировка подсчётом {round(third, 3)}")


speed_compare()
