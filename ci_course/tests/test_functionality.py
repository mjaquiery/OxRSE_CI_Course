import unittest

import ci_course


class TestFunctionality(unittest.TestCase):

    def test_greeting(self):
        # self.assertEqual(ci_course.greet(), "Hello ")
        with self.assertRaisesRegex(ValueError, "No name, no greeting\."):
            ci_course.greet()
        self.assertEqual(ci_course.greet("Fergus"), "Hello Fergus")

    def test_minimum(self):
        self.assertEqual(ci_course.minimum(1, 2, 3), 1)
        self.assertEqual(ci_course.minimum(1.2, 2.3), 1.2)
        self.assertEqual(ci_course.minimum(-1.2, -3), -3)


if __name__ == '__main__':
    unittest.main()
