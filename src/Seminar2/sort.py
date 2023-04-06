from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.queue = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.
        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue:
            raise IndexError("Очередь пуста")
        else:
            return self.queue.pop(0)  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        """
        if type(ind) != int:
            raise TypeError("Введено не число")
        elif ind > len(self.queue) - 1 or ind > -len(self.queue):
            raise IndexError("Вне границ очереди")
        else:
            return self.queue[ind]  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self.queue.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.queue)  # TODO реализовать метод __len__

    def __str__(self):
        return f"{self.queue}"

    def bubble_sort(self):
        for i in range(len(self.queue) - 1):
            for j in range(len(self.queue) - i - 1):
                if self.queue[j] > self.queue[j + 1]:
                    self.queue[j], self.queue[j + 1] = self.queue[j + 1], self.queue[j]

    def quick_sort(self, start_position, end_position):
        left_position = start_position
        right_position = end_position
        pivot = self.queue[(start_position + end_position) // 2]

        while left_position <= right_position:
            while self.queue[left_position] < pivot:
                left_position += 1

            while self.queue[right_position] > pivot:
                right_position -= 1

            if left_position <= right_position:
                if left_position < right_position:
                    self.queue[left_position], self.queue[right_position] = self.queue[right_position], self.queue[
                        left_position]
                left_position += 1
                right_position -= 1
        if left_position < end_position:
            self.quick_sort(left_position, end_position)
        if start_position < right_position:
            self.quick_sort(start_position, right_position)

    def counting_sort(self):
        max_el = max(self.queue)
        min_el = min(self.queue)
        count_arr = [0 for _ in range(min_el, max_el + 1)]
        for i in self.queue:
            count_arr[i - min_el] += 1
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]
        sorted_arr = [0 for _ in range(len(self.queue))]
        for i in range(len(self.queue) - 1, -1, -1):
            sorted_arr[count_arr[self.queue[i] - min_el] - 1] = self.queue[i]
            count_arr[self.queue[i] - min_el] -= 1
        return sorted_arr
