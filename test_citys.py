import unittest
from city_functions import get_formatted_city
from city_functions import get_formatted_city_people

class CitysTestCase(unittest.TestCase):
    """Pruebas para 'city_functions'"""

    def test_get_formatted_city(self):
        """¿La salida es correcta capitalizando la primera letra de cada palabra?"""
        formatted_city = get_formatted_city('madrid', 'spain')
        self.assertEquals(formatted_city, 'Madrid, Spain')

    def test_get_formatted_city_people(self):
        """¿La salida es correcta capitalizando la primera letra de cada palabra y los numeros correcta?"""
        formatted_city_people = get_formatted_city_people('madrid', 'spain', 1000000)
        self.assertEquals(formatted_city_people, 'Madrid - Spain - People 1000000')

    def test_get_formatted_city_people_2(self):
        """¿La salida es correcta capitalizando la primera letra de cada palabra y los numeros correcta?"""
        formatted_city_people = get_formatted_city_people('madrid', 'spain')
        self.assertEquals(formatted_city_people, 'Madrid - Spain')

if __name__ == '__main__':
    unittest.main()