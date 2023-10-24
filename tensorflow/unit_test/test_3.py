# Contoh tes lainnya

import re
import unittest


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .])$", name)
    if result is None:
        return name  # bagian ini diperbaiki akibat test_one_name
    return "{} {}".format(result[2], result[1])


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    # edge case
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    # tambahan unit test
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    # tambahan unit test
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main(argv=["first-arg-is-ignored"], exit=False)
