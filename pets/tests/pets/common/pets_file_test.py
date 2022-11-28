import unittest

from pets.common.pets_file import get_app_name


class PetsFileTest(unittest.TestCase):
    def test_get_app_name(self):
        appName = get_app_name(".pets")
        self.assertEqual('pets-cli', appName)

    def test_get_app_name_not_found(self):
        appName = get_app_name(".not_found")
        self.assertIsNone(appName)


if __name__ == '__main__':
    unittest.main()
