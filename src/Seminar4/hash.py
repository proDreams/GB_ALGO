class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        # self.previousNode = None


class HashTable:
    def __init__(self, size):
        # self.head = None
        self.size = size
        # self.slots = [None] * self.size
        self.data = [[None, None]] * self.size

    def get_hash(self, key):
        return key % self.size

    def insert_data(self, key, value):
        index = self.get_hash(key)
        if self.data[index][0]:

        self.data[index] = [key, value]

    def get_data(self, key):
        index = self.get_hash(key)
        return self.data[index][1]


table = HashTable(10)
table.insert_data(1, "a")
table.insert_data(2, "b")
print(table.get_data(31))
