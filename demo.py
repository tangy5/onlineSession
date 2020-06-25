from employee import Employee, Secretary

employee_A = Employee()
hours = employee_A.get_hours()

secretary_A = Secretary()
salary = secretary_A.get_salary()
secretary_A.take_dictation('Hello World')
print(salary)


