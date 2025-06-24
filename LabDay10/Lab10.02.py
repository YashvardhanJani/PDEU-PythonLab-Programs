# 02. Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.

import csv

def read_csv_to_dict_and_update(filename):
    students = []

    # Read the data and calculate Total
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ['Total']  # Add 'Total' to the existing headers

        for row in reader:
            row['Maths'] = int(row['Maths'])
            row['Chemistry'] = int(row['Chemistry'])
            row['Physics'] = int(row['Physics'])

            total = row['Maths'] + row['Chemistry'] + row['Physics']
            row['Total'] = total

            students.append(row)

    # Write updated data back to the CSV file with the new 'Total' column
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    # Display the updated data
    for student in students:
        print(student)

print("\n")
read_csv_to_dict_and_update("LabDay10\Student-Data.csv")
print("\n")