import random
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


class ArraysNotEqualError(Exception):
    pass


@dataclass
class Book(Generic[T]):
    def __init__(self, author, publisher, page_count, price, isbn):
        self.author = author
        self.publisher = publisher
        self.page_count = page_count
        self.price = price
        self.isbn = isbn

    def __eq__(self, other: Optional['Book[T]']) -> bool:
        if self.author == other.author and self.isbn == other.isbn and self.price == other.price and self.page_count == other.page_count and self.publisher == other.publisher:
            return True
        else:
            return False

    def __str__(self):
        return f"({self.author}, {self.publisher}, {self.page_count}, {self.price}, {self.isbn})"


@dataclass
class DoublyNode(Generic[T]):
    data: Optional['Book[T]']
    next_ptr: Optional['DoublyNode[T]'] = None
    prev_ptr: Optional['DoublyNode[T]'] = None


class DoublyLinkedList(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._head: Optional[DoublyNode[T]] = None
        self._tail: Optional[DoublyNode[T]] = None
        self.i = 0
        self.p = 0
        self.q = 0
        self.stop = False

    def __len__(self) -> int:
        return self._length

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def append(self, data: T) -> None:
        node = DoublyNode[T](data, None)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        self._tail.next_ptr = node
        node.prev_ptr = self._tail
        self._tail = node
        self._length += 1

    def push_head(self, data: T) -> None:
        node = DoublyNode[T](data)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        node.next_ptr = self._head
        self._head.prev_ptr = node
        self._head = node
        self._length += 1

    def insert(self, index: int, data: T) -> None:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        if index == 0:
            self.push_head(data)
            return
        elif index == self._length - 1:
            self.append(data)
            return

        node = self._head
        for i in range(0, index):
            node = node.next_ptr

        insert_node = DoublyNode[T](data)
        insert_node.next_ptr = node
        node.prev_ptr.next_ptr = insert_node
        insert_node.prev_ptr = node.prev_ptr
        node.prev_ptr = insert_node
        self._length += 1

    def get(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        if index == 0:
            return self._head.data
        if index == self._length - 1:
            return self._tail.data

        node = self._head
        for i in range(0, index):
            node = node.next_ptr
        return node.data

    def set(self, index: int, data: T) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")
        node = self._head
        for i in range(0, index):
            node = node.next_ptr
        node.data = data

    def remove(self, index: int) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        if index == 0:
            node = self._head
            self._head = node.next_ptr
            self._head.prev_ptr = None
            del node
            self._length -= 1
            return True

        node = self._head
        for i in range(0, index - 1):
            node = node.next_ptr

        if index == self._length - 1:
            self._tail.prev_ptr = None
            self._tail = node
            self._tail.next_ptr = None
            self._length -= 1
            return True

        delete_node = node.next_ptr
        node.next_ptr = delete_node.next_ptr
        node.next_ptr.prev_ptr = delete_node.prev_ptr
        self._length -= 1
        return True

    def __str__(self) -> str:
        my_str: str = ""
        node = self._head
        while node is not None:
            my_str += str(node.data) + " "
            node = node.next_ptr
        return f"[{my_str}]"

    def find_max(self, key: Optional[Callable[[T], bool]] = None) -> Optional[T]:
        if self._length == 0:
            return None

        max_value = self._head.data
        node = self._head.next_ptr
        while node is not None:
            if key is not None and key(node.data):
                if key(node.data) > key(max_value):
                    max_value = node.data
            else:
                if node.data > max_value:
                    max_value = node.data
            node = node.next_ptr
        return max_value

    def find_min(self, key: Optional[Callable[[T], bool]] = None) -> Optional[T]:
        if self._length == 0:
            return None

        min_value = self._head.data
        node = self._head.next_ptr
        while node is not None:
            if key is not None and key(node.data):
                if key(node.data) < key(min_value):
                    min_value = node.data
            else:
                if node.data < min_value:
                    min_value = node.data
            node = node.next_ptr
        return min_value

    def gnome_sort(self) -> Optional['DoublyLinkedList[T]']:
        index = 1
        i = 0
        n = self._length
        while i < n - 1:
            if self.get(i).page_count <= self.get(i + 1).page_count:
                i, index = index, index + 1
            else:
                a_i, a_i_1 = self.get(i + 1), self.get(i)
                self.set(i, a_i)
                self.set(i + 1, a_i_1)
                i = i - 1
                if i < 0:
                    i, index = index, index + 1
        return self

    def copy(self) -> 'DoublyLinkedList[T]':
        new_list = DoublyLinkedList[T]()
        current_node = self._head
        while current_node is not None:
            new_list.append(current_node.data)
            current_node = current_node.next_ptr

        return new_list

    def counting_sort(self) -> None:
        min_value = self.find_min(key=lambda x: x.page_count).page_count
        max_value = self.find_max(key=lambda x: x.page_count).page_count
        support = [0 for i in range(max_value - min_value + 1)]
        sup_1 = [self.get(i).page_count for i in range(len(self))]
        for el in range(len(self)):
            support[self.get(el).page_count - min_value] += 1
        index = len(self) - 1
        sup_2 = []
        for i in range(len(support)):
            for el in range(support[i]):
                sup_2.append(i + min_value)
                index -= 1
        sup_2.sort(reverse=True)
        a = []
        for k in range(len(sup_2)):
            a.append(self.get(sup_1.index(sup_2[k])))
            sup_1[sup_1.index(sup_2[k])] = None
        for ind in range(len(self)):
            self.set(ind, a[ind])

    def __eq__(self, y: Optional['DoublyLinkedList[T]']) -> bool:
        if self._length == y._length:
            for i in range(len(self)):
                if self.get(i) != y.get(i):
                    return False
            return True
        else:
            return False

    def __get_fibonacci_number(self, k: int) -> int:
        first = 0
        second = 1
        n = 0
        while n < k:
            temp = second
            second = first + second
            first = temp
            n += 1
        return first

    def __start(self) -> None:
        self.stop = False
        k = 0
        n = len(self)
        while self.__get_fibonacci_number(k + 1) < len(self):
            k += 1
        m = self.__get_fibonacci_number(k + 1) - (n + 1)
        self.i = self.__get_fibonacci_number(k) - m
        self.p = self.__get_fibonacci_number(k - 1)
        self.q = self.__get_fibonacci_number(k - 2)

    def __up_index(self) -> None:
        if self.p == 1:
            self.stop = True
        self.i = self.i + self.q
        self.p = self.p - self.q
        self.q = self.q - self.p

    def __down_index(self) -> None:
        if self.q == 0:
            self.stop = True
        self.i = self.i - self.q
        temp = self.q
        self.q = self.p - self.q
        self.p = temp

    def fib_search(self, element: int) -> int:
        arr_1 = self.copy()
        arr_1.gnome_sort()
        if self != arr_1:
            raise ArraysNotEqualError('Список не отсортрован')
        else:
            self.__start()
            res_ind = -1
            while not self.stop:
                if self.i < 0:
                    self.__up_index()
                elif self.i >= len(self):
                    self.__down_index()
                elif self.get(self.i).page_count == element:
                    res_ind = self.i
                    break
                elif element < self.get(self.i).page_count:
                    self.__down_index()
                elif element > self.get(self.i).page_count:
                    self.__up_index()
            else:
                return "Элемента нет в контейнере"
            return self.get(res_ind)


if __name__ == '__main__':
    ...
