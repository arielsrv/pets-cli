import unittest

from pets.common.pets_file import get_app_name


class PetsFileTest(unittest.TestCase):
    def test_get_app_name(self):
        appname = get_app_name(".pets")
        self.assertEqual('pets-cli', appname)

    def test_get_app_name_not_found(self):
        appname = get_app_name(".not_found")
        self.assertIsNone(appname)


if __name__ == '__main__':
    unittest.main()
