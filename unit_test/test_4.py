# raising error
import unittest


def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("Minumum password length must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_millen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


unittest.main()


print(OrganizeList(my_new_list))
