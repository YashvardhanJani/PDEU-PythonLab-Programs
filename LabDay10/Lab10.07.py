""" 07.	If an Employee object contains following details:
empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data."""

import json

employee = {
    "empcode": "S597",
    "empname": "Nikunj Joshi",
    "Date of Joining": "01-09-2022",
    "Salary": 55000.00
}

# --- Serialization ---  (Convert dictionary to JSON and save to a file)
with open("LabDay10/employee.json", "w") as file:
    json.dump(employee, file)
print("Employee data serialized and saved to employee.json\n")

# --- Deserialization ---  (Read JSON from the file and convert back to dictionary)
with open("LabDay10/employee.json", "r") as file:
    loaded_employee = json.load(file)
print("Employee data deserialized:")
print(loaded_employee)