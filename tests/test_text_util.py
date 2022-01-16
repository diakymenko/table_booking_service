import unittest

from table_booking_service.lib.text_util import StringHelper, TextHelper


class TestStringHelper(unittest.TestCase):

    def test_upper_case_word(self):
        string_helper = StringHelper("kkk")
        self.assertEqual(string_helper.upper_case(), "KKK")

    def test_upper_case_space(self):
        string_helper = StringHelper("abcd efg")
        self.assertEqual(string_helper.upper_case(), "ABCD EFG")

    def test_upper_case_capital(self):
        string_helper = StringHelper("Abcd eFg")
        self.assertEqual(string_helper.upper_case(), "ABCD EFG")

    def test_upper_case_blank(self):
        string_helper = StringHelper("")
        self.assertEqual(string_helper.upper_case(), "")


class TestTextHelper(unittest.TestCase):

    def test_upper_case_single_character(self):
        list = ["a", "b", "c"]
        TextHelper.upper_case(list)
        self.assertEqual(list, ["A", "B", "C"])

    def test_upper_case_character_upper(self):
        list = ["aB", "Fa", "aaa"]
        TextHelper.upper_case(list)
        self.assertEqual(list, ["AB", "FA", "AAA"])

    def test_upper_case_blank(self):
        list = []
        TextHelper.upper_case(list)
        self.assertEqual(list, [])


if __name__ == '__main__':
    unittest.main()
