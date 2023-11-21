import ctypes
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


class ArraysNotEqualError(Exception):
    pass


@dataclass
class Student(Generic[T]):
    def __init__(self, SNP=None, group_number=None, course=None, age=None, avg_grade=None):
        self.SNP = SNP
        self.group_number = group_number
        self.course = course
        self.age = age
        self.avg_grade = avg_grade

    def __eq__(self, other: Optional["Student[T]"]) -> bool:
        if self.age == other.age and self.course == other.course and self.SNP == other.SNP and self.avg_grade == other.avg_grade and self.group_number == other.group_number:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"({self.SNP} {self.course} {self.group_number} {self.age} {self.avg_grade})"


class DynamicArray(Generic[T]):

    def __init__(self, capacity: int) -> None:
        self._length: int = 0
        self._capacity: int = capacity
        self._arr: ctypes.Array[T] = (capacity * ctypes.py_object)()

    def get_length(self) -> int:
        return self._length

    def get_capacity(self) -> int:
        return self._capacity

    def _resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array[T] = (new_capacity * ctypes.py_object)()
        for it in range(self._length):
            new_array[it] = self._arr[it]

        self._arr = new_array
        self._capacity = new_capacity

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def add(self, element: T) -> None:
        if self._length == self._capacity:
            self._resize(self._capacity * 2)

        self._arr[self._length] = element
        self._length += 1

    def get(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        return self._arr[index]

    def remove(self, index: int) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        for i in range(index, self._length - 1):
            self._arr[i] = self._arr[i + 1]
        self._length -= 1
        return ok

    def put(self, index: int, element: T) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        self._arr[index] = element
        return ok

    def __str__(self) -> str:
        my_str: str = ""
        for it in range(self._length):
            my_str += str(self._arr[it]) + " "
        return f"[{my_str}]"

    def __eq__(self, y: Optional["DynamicArray[T]"]) -> bool:
        if self._length == y._length:
            for i in range(self.get_length()):
                if self.get(i) != y.get(i):
                    return False
            return True
        else:
            return False

    def copy(self) -> 'DynamicArray[T]':
        new_array = DynamicArray[T](self._capacity)
        for i in range(self._length):
            new_array.add(self.get(i))
        return new_array

    def sort_fio(self) -> None:
        left = 0
        right = self._length - 1
        control = right
        while left < right:
            for i in range(left, right):
                if self.get(i).SNP > self.get(i + 1).SNP:
                    s_i_1, s_i = self.get(i + 1), self.get(i)
                    self.put(i, s_i_1)
                    self.put(i + 1, s_i)
                    control = i
            right = control
            for i in range(right, left, -1):
                if self.get(i).SNP < self.get(i - 1).SNP:
                    s_i_m1, s_mi = self.get(i - 1), self.get(i)
                    self.put(i, s_i_m1)
                    self.put(i - 1, s_mi)
                    control = i
            left = control

    def sort_avg_grade(self) -> None:
        left = 0
        right = self._length - 1
        control = right
        while left < right:
            for i in range(left, right):
                if self.get(i).avg_grade > self.get(i + 1).avg_grade:
                    s_i_1, s_i = self.get(i + 1), self.get(i)
                    self.put(i, s_i_1)
                    self.put(i + 1, s_i)
                    control = i
            right = control
            for i in range(right, left, -1):
                if self.get(i).avg_grade < self.get(i - 1).avg_grade:
                    s_i_m1, s_mi = self.get(i - 1), self.get(i)
                    self.put(i, s_i_m1)
                    self.put(i - 1, s_mi)
                    control = i
            left = control

    def __heapify_1(self, heap_size: int, root_index: int) -> None:
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and self.get(left_child).course < self.get(largest).course:
            largest = left_child

        if right_child < heap_size and self.get(right_child).course < self.get(largest).course:
            largest = right_child

        if largest != root_index:
            a_root_index, a_largest = self.get(largest), self.get(root_index)
            self.put(root_index, a_root_index)
            self.put(largest, a_largest)
            self.__heapify_1(heap_size, largest)

    def sort_course(self) -> None:
        n = self._length
        for i in range(n, -1, -1):
            self.__heapify_1(n, i)
        for i in range(n - 1, 0, -1):
            n_i, n_0 = self.get(0), self.get(i)
            self.put(i, n_i)
            self.put(0, n_0)
            self.__heapify_1(i, 0)



    def ternary_search(self, element):
        arr_1 = self.copy()
        arr_1.sort_avg_grade()
        if self != arr_1:
            raise ArraysNotEqualError('Массив не отсортирован')
        else:
            l = 0
            r = self._length - 1
            while l <= r:
                h = (r - l) // 3
                m1 = l + h
                m2 = r - h
                if self.get(m1).avg_grade == element:
                    return self.get(m1)
                if self.get(m2).avg_grade == element:
                    return self.get(m2)
                if self.get(m1).avg_grade < element < self.get(m2).avg_grade:
                    l = m1 + 1
                    r = m2 - 1
                elif element < self.get(m1).avg_grade:
                    r = m1 - 1
                else:
                    l = m2 + 1
            return "Элемента нет в контейнере"


if __name__ == '__main__':
    ...
