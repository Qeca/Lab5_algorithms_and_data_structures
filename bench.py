from DoubleLinkedList import DoublyLinkedList, Book
from dynamic_array import DynamicArray, Student
import timeit

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
    Student("King Liam Aiden", "120D", 4, 22, 90.5),
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
    Student("King Liam Aiden", "120D", 4, 22, 90.5),
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
books = [
    Book("Jane Austen", "Vintage Classics", 368, 14, "978-0099589273"),
    Book("George Orwell", "Signet Classic", 328, 9, "978-0451524935"),
    Book("J.K. Rowling", "Bloomsbury Publishing", 332, 19, "978-0747558194"),
    Book("Harper Lee", "Harper Perennial Modern Classics", 376, 8, "978-0061120084"),
    Book("F. Scott Fitzgerald", "Scribner", 180, 7, "978-0743273565"),
    Book("William Golding", "Penguin Books", 224, 9, "978-0143129400"),
    Book("J.R.R. Tolkien", "Mariner Books", 1178, 14, "978-0544003415"),
    Book("George R.R. Martin", "Bantam", 694, 9, "978-0553593716"),
    Book("Mark Twain", "Dover Publications", 224, 3, "978-0486400778"),
    Book("Leo Tolstoy", "Vintage Classics", 1392, 12, "978-0670021049"),
    Book("Agatha Christie", "William Morrow Paperbacks", 288, 7, "978-0062073485"),
    Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469"),
    Book("Jane Austen", "Vintage Classics", 368, 14, "978-0099589273"),
    Book("George Orwell", "Signet Classic", 328, 9, "978-0451524935"),
    Book("J.K. Rowling", "Bloomsbury Publishing", 332, 19, "978-0747558194"),
    Book("Harper Lee", "Harper Perennial Modern Classics", 376, 8, "978-0061120084"),
    Book("F. Scott Fitzgerald", "Scribner", 180, 7, "978-0743273565"),
    Book("William Golding", "Penguin Books", 224, 9, "978-0143129400"),
    Book("J.R.R. Tolkien", "Mariner Books", 1178, 14, "978-0544003415"),
    Book("George R.R. Martin", "Bantam", 694, 9, "978-0553593716"),
    Book("Mark Twain", "Dover Publications", 224, 3, "978-0486400778"),
    Book("Leo Tolstoy", "Vintage Classics", 1392, 12, "978-0670021049"),
    Book("Agatha Christie", "William Morrow Paperbacks", 288, 7, "978-0062073485"),
    Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469"),
    Book("Jane Austen", "Vintage Classics", 368, 14, "978-0099589273"),
    Book("George Orwell", "Signet Classic", 328, 9, "978-0451524935"),
    Book("J.K. Rowling", "Bloomsbury Publishing", 332, 19, "978-0747558194"),
    Book("Harper Lee", "Harper Perennial Modern Classics", 376, 8, "978-0061120084"),
    Book("F. Scott Fitzgerald", "Scribner", 180, 7, "978-0743273565"),
    Book("William Golding", "Penguin Books", 224, 9, "978-0143129400"),
    Book("J.R.R. Tolkien", "Mariner Books", 1178, 14, "978-0544003415"),
    Book("George R.R. Martin", "Bantam", 694, 9, "978-0553593716"),
    Book("Mark Twain", "Dover Publications", 224, 3, "978-0486400778"),
    Book("Leo Tolstoy", "Vintage Classics", 1392, 12, "978-0670021049"),
    Book("Agatha Christie", "William Morrow Paperbacks", 288, 7, "978-0062073485"),
    Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469"),
    Book("Jane Austen", "Vintage Classics", 368, 14, "978-0099589273"),
    Book("George Orwell", "Signet Classic", 328, 9, "978-0451524935"),
    Book("J.K. Rowling", "Bloomsbury Publishing", 332, 19, "978-0747558194"),
    Book("Harper Lee", "Harper Perennial Modern Classics", 376, 8, "978-0061120084"),
    Book("F. Scott Fitzgerald", "Scribner", 180, 7, "978-0743273565"),
    Book("William Golding", "Penguin Books", 224, 9, "978-0143129400"),
    Book("J.R.R. Tolkien", "Mariner Books", 1178, 14, "978-0544003415"),
    Book("George R.R. Martin", "Bantam", 694, 9, "978-0553593716"),
    Book("Mark Twain", "Dover Publications", 224, 3, "978-0486400778"),
    Book("Leo Tolstoy", "Vintage Classics", 1392, 12, "978-0670021049"),
    Book("Agatha Christie", "William Morrow Paperbacks", 288, 7, "978-0062073485"),
    Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469")
]

llist = DoublyLinkedList()
for i in books:
    llist.append(i)
start = timeit.default_timer()
llist.gnome_sort()
print(f"Гномья сортировка: {float(timeit.default_timer() - start)}, колво обьектов: {len(books)}")

start_1 = timeit.default_timer()
llist.counting_sort()
print(f"Сортировка подсчетом: {float(timeit.default_timer() - start_1)}, колво обьектов: {len(books)}")

arr = DynamicArray(capacity=10)
for i in students:
    arr.add(i)
start = timeit.default_timer()
arr.sort_fio()
print(f"Сортировка перемешиванием: {float(timeit.default_timer() - start)}, колво обьектов: {len(students)}")
start_1 = timeit.default_timer()
arr.sort_course()
print(f"Сортировка кучей: {float(timeit.default_timer() - start_1)}, колво обьектов: {len(students)}")
