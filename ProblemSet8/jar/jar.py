class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('The capacity must be bigger than zero')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ('🍪' * self._size)

    def deposit(self, n):
        total = self._size + n
        if total > self._capacity:
            raise ValueError('Too much cookies')
        self._size = total
        return self._size

    def withdraw(self, n):
        total = self._size - n
        if total < 0:
            raise ValueError('Not enough cookies')
        self._size = total
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('The capacity must be bigger than zero')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self._capacity:
            raise ValueError(f'The size must be between zero and {self._capacity}')
        self._size = size
