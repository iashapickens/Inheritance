class Employee:
    def __init__(self, name, employee_number):
        self._name = name
        self._employee_number = employee_number

    def get_name(self):
        return self._name

    def get_employee_number(self):
        return self._employee_number

    def set_name(self, name):
        self._name = name

    def set_employee_number(self, employee_number):
        self._employee_number = employee_number

class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(name, employee_number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self._shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate

class ShiftSupervisor(Employee):
    def __init__(self, name, employee_number, annual_salary, annual_bonus):
        super().__init__(name, employee_number)
        self._annual_salary = annual_salary
        self._annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self._annual_salary

    def get_annual_bonus(self):
        return self._annual_bonus

    def set_annual_salary(self, annual_salary):
        self._annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self._annual_bonus = annual_bonus
