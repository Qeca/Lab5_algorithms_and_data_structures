import unittest
from DoubleLinkedList import DoublyLinkedList, Book


class TestLinkedList(unittest.TestCase):

    def test_append_and_str_int(self):
        llist = DoublyLinkedList()
        for i in range(1, 11):
            llist.append(i)
        self.assertEqual(f'{llist}', '[1 2 3 4 5 6 7 8 9 10 ]')

    def test_len(self):
        llist = DoublyLinkedList()
        for i in range(11):
            llist.append(i)
        llist1 = DoublyLinkedList()
        for i in range(16):
            llist1.append(i)
        llist2 = DoublyLinkedList()
        for i in range(25):
            llist2.append(i)
        self.assertEqual(len(llist), 11)
        self.assertEqual(len(llist1), 16)
        self.assertEqual(len(llist2), 25)

    def test_remove(self):
        llist = DoublyLinkedList()
        for i in range(11):
            llist.append(i)
        llist.remove(3)
        self.assertEqual(f'{llist}', '[0 1 2 4 5 6 7 8 9 10 ]')

    def test_insert(self):
        llist = DoublyLinkedList()
        for i in range(11):
            llist.append(i)
        llist.insert(3, 22)
        self.assertEqual(f"{llist}", "[0 1 2 22 3 4 5 6 7 8 9 10 ]")

    def test_get(self):
        llist = DoublyLinkedList()
        for i in range(11):
            llist.append(i)
        self.assertEqual(llist.get(5), 5)

    def test_head(self):
        llist = DoublyLinkedList()
        for i in range(11):
            llist.append(i)
        llist.push_head(12)
        self.assertEqual(f"{llist}", "[12 0 1 2 3 4 5 6 7 8 9 10 ]")

    def test_set(self):
        llist = DoublyLinkedList()
        for i in range(11):
            llist.append(i)
        llist.set(0, 100)
        self.assertEqual(f'{llist}', "[100 1 2 3 4 5 6 7 8 9 10 ]")

    def test_find_max(self):
        llist = DoublyLinkedList()
        tuples = [(1, 2), (3, 4), (5, -1), (6, 146)]
        for i in tuples:
            llist.append(i)
        self.assertEqual(llist.find_max(key=lambda x: x[1]), (6, 146))

    def test_find_min(self):
        llist = DoublyLinkedList()
        tuples = [(1, 2), (3, 4), (5, -1), (6, 146)]
        for i in tuples:
            llist.append(i)
        self.assertEqual(llist.find_min(key=lambda x: x[0]), (1, 2))

    def test_gnome_sort(self):
        llist = DoublyLinkedList()
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
            Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469")
        ]
        for i in books:
            llist.append(i)
        llist.gnome_sort()
        self.assertEqual(f'{llist}',
                         "[(Agatha Christie, William Morrow Paperbacks, 288, 7, 978-0062073485) (Ernest Hemingway, Scribner, 332, 10, 978-0684801469) (F. Scott Fitzgerald, Scribner, 180, 7, 978-0743273565) (George Orwell, Signet Classic, 328, 9, 978-0451524935) (George R.R. Martin, Bantam, 694, 9, 978-0553593716) (Harper Lee, Harper Perennial Modern Classics, 376, 8, 978-0061120084) (J.K. Rowling, Bloomsbury Publishing, 332, 19, 978-0747558194) (J.R.R. Tolkien, Mariner Books, 1178, 14, 978-0544003415) (Jane Austen, Vintage Classics, 368, 14, 978-0099589273) (Leo Tolstoy, Vintage Classics, 1392, 12, 978-0670021049) (Mark Twain, Dover Publications, 224, 3, 978-0486400778) (William Golding, Penguin Books, 224, 9, 978-0143129400) ]")

    def test_counting_sort(self):
        llist = DoublyLinkedList()
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
            Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469")
        ]
        for i in books:
            llist.append(i)
        llist.counting_sort()
        self.assertEqual(f"{llist}",
                         "[(Leo Tolstoy, Vintage Classics, 1392, 12, 978-0670021049) (J.R.R. Tolkien, Mariner Books, 1178, 14, 978-0544003415) (George R.R. Martin, Bantam, 694, 9, 978-0553593716) (Harper Lee, Harper Perennial Modern Classics, 376, 8, 978-0061120084) (Jane Austen, Vintage Classics, 368, 14, 978-0099589273) (J.K. Rowling, Bloomsbury Publishing, 332, 19, 978-0747558194) (Ernest Hemingway, Scribner, 332, 10, 978-0684801469) (George Orwell, Signet Classic, 328, 9, 978-0451524935) (Agatha Christie, William Morrow Paperbacks, 288, 7, 978-0062073485) (William Golding, Penguin Books, 224, 9, 978-0143129400) (Mark Twain, Dover Publications, 224, 3, 978-0486400778) (F. Scott Fitzgerald, Scribner, 180, 7, 978-0743273565) ]")

    def test_fib_search(self):
        llist = DoublyLinkedList()
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
            Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469")
        ]
        for i in books:
            llist.append(i)
        llist.gnome_sort()
        self.assertEqual(f'{llist.fib_search(180)}', "(F. Scott Fitzgerald, Scribner, 180, 7, 978-0743273565)")

    def test_eq(self):
        llist = DoublyLinkedList()
        llist_1 = DoublyLinkedList()
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
            Book("Ernest Hemingway", "Scribner", 332, 10, "978-0684801469")
        ]
        books_1 = books.copy()
        for i in books:
            llist.append(i)
        llist.gnome_sort()
        for i in books_1:
            llist_1.append(i)
        self.assertEqual(llist == llist_1, False)
        llist_1.gnome_sort()
        self.assertEqual(llist == llist_1, True)
if __name__ == '__main__':
    unittest.main()
