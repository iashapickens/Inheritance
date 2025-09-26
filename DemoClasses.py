# main.py
from EmployeeClass import ProductionWorker, ShiftSupervisor

# ----------- Production Worker Demo -----------
print("Enter Production Worker Information:")
name = input("Name: ")
emp_number = input("Employee Number: ")
shift = int(input("Shift (1=Day, 2=Night): "))
hourly_rate = float(input("Hourly Pay Rate: "))

worker = ProductionWorker(name, emp_number, shift, hourly_rate)

print("\n--- Production Worker Info ---")
print(f"Name: {worker.get_name()}")
print(f"Employee Number: {worker.get_employee_number()}")
print(f"Shift: {'Day' if worker.get_shift_number() == 1 else 'Night'}")
print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

# ----------- Shift Supervisor Demo -----------
print("\nEnter Shift Supervisor Information:")
name = input("Name: ")
emp_number = input("Employee Number: ")
salary = float(input("Annual Salary: "))
bonus = float(input("Annual Production Bonus: "))

supervisor = ShiftSupervisor(name, emp_number, salary, bonus)

print("\n--- Shift Supervisor Info ---")
print(f"Name: {supervisor.get_name()}")
print(f"Employee Number: {supervisor.get_employee_number()}")
print(f"Annual Salary: ${supervisor.get_annual_salary():.2f}")
print(f"Annual Bonus: ${supervisor.get_annual_bonus():.2f}")
