# Berikut contoh penerapan edge case test

import re
import unittest


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .])$", name)
    if result is None:  # bagian ini tambahan perbaikan akibat edge case
        return ""  # bagian ini tambahan perbaikan akibat edge case
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


unittest.main(argv = ['first-arg-is-ignored'], exit = False)
