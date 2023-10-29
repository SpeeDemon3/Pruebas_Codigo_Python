import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Pruebas para la clase Employee"""

    def setUp(self):
        """Crea un empleado para poder utilizar en todas las pruebas"""
        self.employee = Employee('Antonio', 'Ruiz', 50000)

    def test_give_predetermined_salary_increase_(self):
        """Comprueba si se agina el aumento por defecto"""
        self.employee.give_salary_increase()

    def test_give_personalized_salary_increase_(self):
        """Comprueba si asigna correctamente el aumento personalizado"""
        self.employee.give_salary_increase(30000)
