import unittest
from exo2 import solution

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)

class Exo2Test(unittest.TestCase):
    def test_fixed_true(self):
        for string, ending in fixed_tests_True:
            with self.subTest(string=string, ending=ending):
                self.assertTrue(solution(string, ending))

    def test_fixed_false(self):
        for string, ending in fixed_tests_False:
            with self.subTest(string=string, ending=ending):
                self.assertFalse(solution(string, ending))

if __name__ == "__main__":
    unittest.main()
