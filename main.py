from practice import Employee

emp2 = (Employee('hashim','qureshi',32131231,'4'))
emp_1 = Employee('MR', 'X', 50000, 1)
emp_2 = Employee('Test', 'Employee', 60000, 2)
emp2.DepartmentName = "IT"
print(emp_1.fullname(emp2.DepartmentName))
print(emp_2.fullname(emp2.DepartmentName))
print(emp2.fullname(emp2.DepartmentName))
