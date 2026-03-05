# test_utils.py
import unittest
from unittest.mock import patch
from datetime import datetime
from utils import (
    sum_numbers,
    create_user,
    filter_adults,
    find_in_list,
    parse_json,
    approximate_division,
)


class TestExactEquality(unittest.TestCase):
    """
    Jest equivalents: toBe, toEqual, toStrictEqual
    """
    def test_sum_assertEqual_passes(self):
        self.assertEqual(sum_numbers(2, 2), 4)

    def test_sum_assertEqual_fails(self):
        # self.assertEqual(sum_numbers(2, 2), 5)
        pass
    
    def test_create_user_assertDictEqual_passes(self):
        fixed_time = datetime(2025, 1, 1, 12, 0, 0)
        with patch("utils.datetime") as mock_dt:
            mock_dt.now.return_value = fixed_time
            user = create_user("Alice", 30)

        expected = {"name": "Alice", "age": 30, "created_at": fixed_time}
        self.assertDictEqual(user, expected)

    def test_create_user_assertDictEqual_fails(self):
        fixed_time = datetime(2025, 1, 1, 12, 0, 0)
        with patch("utils.datetime") as mock_dt:
            mock_dt.now.return_value = fixed_time
            user = create_user("Alice", 30)

        wrong_expected = {"name": "Bob", "age": 30, "created_at": fixed_time}
        # self.assertDictEqual(user, wrong_expected)
        pass
    
    def test_filter_adults_assertListEqual_passes(self):
        users = [{"name": "Alice", "age": 20}, {"name": "Tom", "age": 15}]
        result = filter_adults(users)
        self.assertListEqual(result, [{"name": "Alice", "age": 20}])

    def test_filter_adults_assertListEqual_fails(self):
        users = [{"name": "Alice", "age": 20}]
        result = filter_adults(users)
        # self.assertListEqual(result, [{"name": "Bob", "age": 20}])
        pass

    def test_assertIs_passes(self):
        result = find_in_list([1, 2, 3], 2)
        self.assertIs(result, True)

    def test_assertIs_fails(self):
        # self.assertIs(1, True)
        pass


class TestNegation(unittest.TestCase):
    """
    Jest equivalent: .not
    """

    # Test 5: assertNotEqual
    def test_assertNotEqual_passes(self):
        self.assertNotEqual(sum_numbers(1, 1), 3)

    def test_assertNotEqual_fails(self):
        # self.assertNotEqual(sum_numbers(1, 1), 2)
        pass

    def test_assertIsNot_passes(self):
        self.assertIsNot(None, 0)

    def test_assertNotIn_string_passes(self):
        self.assertNotIn("z", "apple")

    def test_assertNotIn_list_passes(self):
        self.assertNotIn(99, [1, 2, 3])

    def test_assertNotIn_list_fails(self):
        # self.assertNotIn(2, [1, 2, 3])
        pass


class TestTruthiness(unittest.TestCase):
    """
    Jest equivalents: toBeNull, toBeUndefined, toBeDefined, toBeTruthy, toBeFalsy
    """

    def test_assertIsNone_passes(self):
        result = None
        self.assertIsNone(result)

    def test_assertIsNone_fails(self):
        # self.assertIsNone("hello")
        pass

    def test_assertIsNotNone_passes(self):
        fixed_time = datetime(2025, 1, 1)
        with patch("utils.datetime") as mock_dt:
            mock_dt.now.return_value = fixed_time
            user = create_user("Bob", 25)
        self.assertIsNotNone(user)

    def test_assertTrue_passes(self):
        self.assertTrue(find_in_list([1, 2, 3], 2))

    def test_assertTrue_fails(self):
        # self.assertTrue(find_in_list([1, 2, 3], 4))
        pass

    def test_assertFalse_passes(self):
        self.assertFalse(find_in_list([1, 2, 3], 4))

    def test_assertFalse_fails(self):
        # self.assertFalse(find_in_list([1, 2, 3], 2))
        pass

    def test_undefined_equivalent_assertIsNone(self):
        def returns_nothing():
            pass  # implicitly returns None

        self.assertIsNone(returns_nothing())


class TestNumberMatchers(unittest.TestCase):
    """
    Jest equivalents: toBeGreaterThan, toBeGreaterThanOrEqual,
                      toBeLessThan, toBeLessThanOrEqual, toBeCloseTo
    """

    def test_assertGreater_passes(self):
        self.assertGreater(sum_numbers(2, 3), 4)

    def test_assertGreater_fails(self):
        # self.assertGreater(sum_numbers(2, 3), 5)
        pass

    def test_assertGreaterEqual_passes(self):
        self.assertGreaterEqual(sum_numbers(2, 3), 5)

    def test_assertLess_passes(self):
        self.assertLess(approximate_division(10, 2), 6)

    def test_assertLessEqual_passes(self):
        self.assertLessEqual(approximate_division(10, 2), 5)

    def test_assertLessEqual_fails(self):
        # self.assertLessEqual(approximate_division(10, 2), 4)
        pass

    def test_assertAlmostEqual_passes(self):
        result = approximate_division(0.3, 0.1)
        self.assertAlmostEqual(result, 3.0, places=5)

    def test_assertAlmostEqual_fails(self):
        # self.assertAlmostEqual(approximate_division(0.3, 0.1), 4.0, places=5)
        pass


class TestStringMatchers(unittest.TestCase):
    """
    Jest equivalents: toMatch, not.toMatch
    """

    def test_assertRegex_passes(self):
        self.assertRegex("Hello World", r"World")

    def test_assertRegex_on_username_passes(self):
        fixed_time = datetime(2025, 1, 1)
        with patch("utils.datetime") as mock_dt:
            mock_dt.now.return_value = fixed_time
            user = create_user("Alice", 30)
        self.assertRegex(user["name"], r"^Alice")

    def test_assertRegex_fails(self):
        # self.assertRegex("Hello World", r"Python")
        pass

    def test_assertNotRegex_passes(self):
        self.assertNotRegex("Hello World", r"Python")

    def test_assertNotRegex_fails(self):
        # self.assertNotRegex("Hello World", r"World")
        pass


class TestIterables(unittest.TestCase):
    """
    Jest equivalents: toContain, not.toContain
    """

    def test_assertIn_list_passes(self):
        users = ["Alice", "Bob", "Charlie"]
        self.assertIn("Alice", users)

    def test_assertIn_list_fails(self):
        # self.assertIn("David", ["Alice", "Bob"])
        pass

    def test_assertIn_set_passes(self):
        roles = {"admin", "editor", "viewer"}
        self.assertIn("admin", roles)

    def test_assertIn_filter_adults_passes(self):
        users = [{"name": "Alice", "age": 25}, {"name": "Tom", "age": 16}]
        adults = filter_adults(users)
        self.assertIn({"name": "Alice", "age": 25}, adults)

    def test_assertNotIn_list_passes(self):
        self.assertNotIn("David", ["Alice", "Bob"])

    def test_assertNotIn_list_fails(self):
        # self.assertNotIn("Alice", ["Alice", "Bob"])
        pass

    def test_assertNotIn_set_passes(self):
        roles = {"admin", "editor"}
        self.assertNotIn("superuser", roles)


class TestExceptions(unittest.TestCase):
    """
    Jest equivalent: toThrow
    """

    def test_assertRaises_with_none_passes(self):
        with self.assertRaises(ValueError):
            parse_json(None)

    def test_assertRaises_with_empty_string_passes(self):
        with self.assertRaises(ValueError):
            parse_json("")

    def test_assertRaisesRegex_message_passes(self):
        with self.assertRaisesRegex(ValueError, "No JSON string provided"):
            parse_json("")

    def test_assertRaises_invalid_json_passes(self):
        with self.assertRaises(Exception):
            parse_json("not-valid-json")

    def test_assertRaises_valid_json_does_not_raise(self):
        try:
            result = parse_json('{"key": "value"}')
            self.assertEqual(result, {"key": "value"})
        except Exception:
            self.fail("parse_json raised an exception for valid JSON input")


if __name__ == "__main__":
    unittest.main(verbosity=2)