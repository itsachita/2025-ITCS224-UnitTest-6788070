import unittest

def get_age_category(age):
    if 0 <= age <= 9:
        return "is_child"
    elif 18 <= age <= 64:
        return "is_adult"
    elif age >= 65:
        return "is_golden"
    return "unknown"

class TestAgeCategories(unittest.TestCase):

    def test_child_age(self):
        """Checks all ages in the child range (0-9)"""
        category = "is_child"
        for age in range(0, 10):
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(get_age_category(age), category)

    def test_adult_age(self):
        """Checks a range of adult ages (18-20)"""
        category = "is_adult"
        for age in range(18, 21):
            with self.subTest(age=age):
                print(f"{age} is considered as an adult.")
                self.assertEqual(get_age_category(age), category)

    def test_golden_age(self):
        """Checks a range of golden ages (65-67)"""
        category = "is_golden"
        for age in range(65, 68):
            with self.subTest(age=age):
                print(f"{age} is considered as a golden age.")
                self.assertEqual(get_age_category(age), category)

if __name__ == '__main__':
    unittest.main(verbosity=2)