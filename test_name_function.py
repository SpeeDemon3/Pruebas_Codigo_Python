import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Pruebas para 'name_function.py'"""

    def test_first_last_name(self):
        """¿Funcionan nombres compuestos?"""
        formatted_name = get_formatted_name('connor', 'macgregor')
        self.assertEquals(formatted_name, 'Connor Macgregor')


if __name__ == '__main__':
    unittest.main()