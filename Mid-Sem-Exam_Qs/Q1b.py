# 01.(b) Create a dictionary with dept name, employee roll no. and salary. Find out department wise minimum and maximum of salary.

def create_employee_dict():
    employee_dict = {}
    num_employees = int(input("Enter the number of employees: "))

    for i in range(num_employees):
        dept_name = input(f"Enter department name for employee {i + 1}: ")
        emp_roll_no = input(f"Enter employee roll number for employee {i + 1}: ")
        salary = float(input(f"Enter salary for employee {i + 1}: "))

        # Add data to the dictionary
        if dept_name not in employee_dict:
            employee_dict[dept_name] = {}
        employee_dict[dept_name][emp_roll_no] = salary

    return employee_dict

def find_min_max_salary(employee_dict):
    dept_min_max = {}

    for dept_name, employees in employee_dict.items():
        salaries = list(employees.values())
        min_salary = min(salaries)
        max_salary = max(salaries)
        dept_min_max[dept_name] = {"Min Salary": min_salary, "Max Salary": max_salary}

    return dept_min_max

employee_dict = create_employee_dict()
print("\nEmployee Data:", employee_dict)

dept_min_max = find_min_max_salary(employee_dict)
print("\nDepartment-wise Minimum and Maximum Salaries:")
for dept_name, salaries in dept_min_max.items():
    print(f"Department {dept_name}: Min Salary = {salaries['Min Salary']}, Max Salary = {salaries['Max Salary']}")