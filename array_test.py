import unittest
from dynamic_array import DynamicArray, Student


class ArrayCase(unittest.TestCase):
    def test_add_and_str(self):
        arr = DynamicArray(capacity=11)
        for i in range(11):
            arr.add(i)
        self.assertEqual(f"{arr}", "[0 1 2 3 4 5 6 7 8 9 10 ]")

    def test_get_length_and_get_capacity(self):
        arr = DynamicArray(capacity=20)
        for i in range(11):
            arr.add(i)
        self.assertEqual(arr.get_length(), 11)
        self.assertEqual(arr.get_capacity(), 20)

    def test_get(self):
        arr = DynamicArray(capacity=11)
        for i in range(11):
            arr.add(i)
        self.assertEqual(arr.get(3), 3)

    def test_remove(self):
        arr = DynamicArray(capacity=11)
        for i in range(11):
            arr.add(i)
        arr.remove(3)
        self.assertEqual(f'{arr}', "[0 1 2 4 5 6 7 8 9 10 ]")

    def test_put(self):
        arr = DynamicArray(capacity=11)
        for i in range(11):
            arr.add(i)
        arr.put(3, 100)
        self.assertEqual(f"{arr}", "[0 1 2 100 4 5 6 7 8 9 10 ]")

    def test_sort_fio(self):
        students = [
            Student("Smith John William", "101A", 2, 20, 85.5),
            Student("Johnson Emily Rose", "102B", 3, 21, 90.0),
            Student("Brown Daniel Michael", "103C", 1, 19, 78.5),
            Student("Wilson Olivia Grace", "104D", 4, 22, 88.0),
            Student("Miller James David", "105A", 2, 20, 75.0),
            Student("Anderson Sophia Elizabeth", "106B", 3, 21, 92.5),
            Student("Taylor William Robert", "107C", 1, 19, 81.0),
            Student("Clark Ava Mary", "108D", 4, 22, 87.5),
            Student("White Matthew Joseph", "109A", 2, 20, 79.5),
            Student("Harris Lily Grace", "110B", 3, 21, 93.5),
            Student("Martin Michael Christopher", "111C", 1, 19, 76.5),
            Student("Thomas Emma Oliver", "112D", 4, 22, 89.0),
            Student("Jones Sophia Liam", "113A", 2, 20, 84.0),
            Student("Moore Oliver Ethan", "114B", 3, 21, 91.0),
            Student("Robinson Ava Charlotte", "115C", 1, 19, 77.0),
            Student("Adams Ethan Noah", "116D", 4, 22, 86.5),
            Student("Hall Charlotte Mia", "117A", 2, 20, 80.5),
            Student("Lee Benjamin Lucas", "118B", 3, 21, 94.5),
            Student("Garcia Mia Emma", "119C", 1, 19, 74.0),
            Student("King Liam Aiden", "120D", 4, 22, 90.5)
        ]
        arr = DynamicArray(capacity=10)
        for i in students:
            arr.add(i)
        arr.sort_fio()
        self.assertEqual(f'{arr}',
                         "[(Adams Ethan Noah 4 116D 22 86.5) (Anderson Sophia Elizabeth 3 106B 21 92.5) (Brown Daniel Michael 1 103C 19 78.5) (Clark Ava Mary 4 108D 22 87.5) (Garcia Mia Emma 1 119C 19 74.0) (Hall Charlotte Mia 2 117A 20 80.5) (Harris Lily Grace 3 110B 21 93.5) (Johnson Emily Rose 3 102B 21 90.0) (Jones Sophia Liam 2 113A 20 84.0) (King Liam Aiden 4 120D 22 90.5) (Lee Benjamin Lucas 3 118B 21 94.5) (Martin Michael Christopher 1 111C 19 76.5) (Miller James David 2 105A 20 75.0) (Moore Oliver Ethan 3 114B 21 91.0) (Robinson Ava Charlotte 1 115C 19 77.0) (Smith John William 2 101A 20 85.5) (Taylor William Robert 1 107C 19 81.0) (Thomas Emma Oliver 4 112D 22 89.0) (White Matthew Joseph 2 109A 20 79.5) (Wilson Olivia Grace 4 104D 22 88.0) ]")

    def test_sort_course(self):
        students = [
            Student("Smith John William", "101A", 2, 20, 85.5),
            Student("Johnson Emily Rose", "102B", 3, 21, 90.0),
            Student("Brown Daniel Michael", "103C", 1, 19, 78.5),
            Student("Wilson Olivia Grace", "104D", 4, 22, 88.0),
            Student("Miller James David", "105A", 2, 20, 75.0),
            Student("Anderson Sophia Elizabeth", "106B", 3, 21, 92.5),
            Student("Taylor William Robert", "107C", 1, 19, 81.0),
            Student("Clark Ava Mary", "108D", 4, 22, 87.5),
            Student("White Matthew Joseph", "109A", 2, 20, 79.5),
            Student("Harris Lily Grace", "110B", 3, 21, 93.5),
            Student("Martin Michael Christopher", "111C", 1, 19, 76.5),
            Student("Thomas Emma Oliver", "112D", 4, 22, 89.0),
            Student("Jones Sophia Liam", "113A", 2, 20, 84.0),
            Student("Moore Oliver Ethan", "114B", 3, 21, 91.0),
            Student("Robinson Ava Charlotte", "115C", 1, 19, 77.0),
            Student("Adams Ethan Noah", "116D", 4, 22, 86.5),
            Student("Hall Charlotte Mia", "117A", 2, 20, 80.5),
            Student("Lee Benjamin Lucas", "118B", 3, 21, 94.5),
            Student("Garcia Mia Emma", "119C", 1, 19, 74.0),
            Student("King Liam Aiden", "120D", 4, 22, 90.5)
        ]
        arr = DynamicArray(capacity=10)
        for i in students:
            arr.add(i)
        arr.sort_course()
        self.assertEqual(f"{arr}", "[(Clark Ava Mary 4 108D 22 87.5) (Adams Ethan Noah 4 116D 22 86.5) (Wilson Olivia Grace 4 104D 22 88.0) (King Liam Aiden 4 120D 22 90.5) (Thomas Emma Oliver 4 112D 22 89.0) (Moore Oliver Ethan 3 114B 21 91.0) (Anderson Sophia Elizabeth 3 106B 21 92.5) (Harris Lily Grace 3 110B 21 93.5) (Lee Benjamin Lucas 3 118B 21 94.5) (Johnson Emily Rose 3 102B 21 90.0) (Jones Sophia Liam 2 113A 20 84.0) (Miller James David 2 105A 20 75.0) (Smith John William 2 101A 20 85.5) (White Matthew Joseph 2 109A 20 79.5) (Hall Charlotte Mia 2 117A 20 80.5) (Robinson Ava Charlotte 1 115C 19 77.0) (Taylor William Robert 1 107C 19 81.0) (Brown Daniel Michael 1 103C 19 78.5) (Martin Michael Christopher 1 111C 19 76.5) (Garcia Mia Emma 1 119C 19 74.0) ]")

if __name__ == '__main__':
    unittest.main()
