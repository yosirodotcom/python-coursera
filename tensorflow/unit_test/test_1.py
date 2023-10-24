# contoh ingin membuat unit test
# menyusun ulang nama depan dan belakang

import re
import unittest


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .])$", name)
    return "{} {}".format(result[2], result[1])


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main(argv=["first-arg-is-ignored"], exit=False)


# Pada shell:
# user@ubuntu:~$ chmod + namafile.py
# user@ubuntu:~$ ./namafile.py
