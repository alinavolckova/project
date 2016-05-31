from unittest import TestCase
from Searcher import Searcher
from SearcherExeption import SearcherException


class MainTests(TestCase):
    def setUp(self):
        self.search = Searcher()

    def test_ContainsPartString1(self):
        self.assertEqual("содержит на позиции 0", self.search.contains("abcdef", "abc").__str__())

    def test_ContainsPartString2(self):
        self.assertEqual("содержит на позиции 3", self.search.contains("abcdef", "def").__str__())

    def test_NotContainsPartString1(self):
        self.assertEqual("не содержит", self.search.contains("abcdef", "dg").__str__())

    def test_NotContainsPartString2(self):
        self.assertEqual("не содержит", self.search.contains("abcdef", "drf").__str__())

    def test_ContainsFullString(self):
        self.assertEqual("содержит на позиции 0", self.search.contains("abcdef", "abcdef").__str__())

    def test_OutOfLenght(self):
        with self.assertRaises(SearcherException):
            self.search.contains("abcdef", "acvhfjfcsm").__str__()

    def test_EmptyString(self):
        with self.assertRaises(SearcherException):
            self.search.contains("", "acvhfjfcsm").__str__()

    def test_EmptySubString(self):
        with self.assertRaises(SearcherException):
            self.search.contains("ahfjkvl", "").__str__()
