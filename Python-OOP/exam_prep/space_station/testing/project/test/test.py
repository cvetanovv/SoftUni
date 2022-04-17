from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("Books")

    def test_init(self):
        self.assertEqual(self.library.name, "Books")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_name_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            library = Library('')
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        self.library.add_book("Ivan", "Bulgarian History")
        self.assertTrue("Ivan" in self.library.books_by_authors)
        self.assertTrue("Bulgarian History" in self.library.books_by_authors["Ivan"])

    def test_add_reader(self):
        self.library.add_reader("Pesho")
        self.assertTrue("Pesho" in self.library.readers)

        name_exist = self.library.add_reader("Pesho")
        self.assertEqual(name_exist, "Pesho is already registered in the Books library.")

    def test_if_reader_is_no_registered(self):
        result = self.library.rent_book("Katq", "name2", "testbook")
        self.assertEqual(result, "Katq is not registered in the Books Library.")

    def test_if_author_not_exist(self):
        self.library.add_reader("Katq")
        result = self.library.rent_book("Katq", "Minchev", "testbook")
        self.assertEqual(result, "Books Library does not have any Minchev's books.")

    def test_book_author_not_exist(self):
        self.library.add_reader("Katq")
        self.library.add_book("Ivan", "Bulgarian History")
        result = self.library.rent_book("Katq", "Ivan", "testbook")
        self.assertEqual(result, """Books Library does not have Ivan's "testbook".""")

    def test_successful_rent_book(self):
        self.library.add_reader("Katq")
        self.library.add_book("Ivan", "Bulgarian History")
        self.library.rent_book("Katq", "Ivan", "Bulgarian History")
        self.assertTrue({"Ivan": "Bulgarian History"} in self.library.readers["Katq"])
        self.assertTrue("Bulgarian History" not in self.library.books_by_authors["Ivan"])



if __name__ == '__main__':
    main()
