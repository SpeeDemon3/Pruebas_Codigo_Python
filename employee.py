class Employee:
    """Representa un empleado en una empresa"""

    def __init__(self, name, last_name, annual_salary):
        self.name = name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.employee_registration = []


    def set_name(self, name):
        """Asigna el nombre a un empleado"""
        self.name = name

    def set_last_name(self, last_name):
        """Asigna el apellido a un empleado"""
        self.last_name = last_name

    def set_annual_salary(self, annual_salary):
        """Asigna el salario anual a un empleado"""
        self.annual_salary = annual_salary

    def give_salary_increase(self, increase = 10000):
        """Añade un aumento al salario, por defecto seran 10000"""
        self.annual_salary += increase

    def add_employee(self, employee):
        """Añade un empleado al registro"""
        self.employee_registration.append(employee)

    def show_employees(self):
        """Imprime por consola los empleados registrados"""
        for employee in self.employee_registration:
            print(employee)
