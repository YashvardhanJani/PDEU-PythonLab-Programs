# 14. Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail.

def get_grade(marks):

    if marks == "Absent":
        return "NA"
    
    marks = int(marks)  

    if 0 <= marks <= 39:
        return "F"
    elif 40 <= marks <= 44:
        return "P"
    elif 45 <= marks <= 49:
        return "C"
    elif 50 <= marks <= 54:
        return "B"
    elif 55 <= marks <= 59:
        return "B+"
    elif 60 <= marks <= 69:
        return "A"
    elif 70 <= marks <= 79:
        return "A+"
    elif 80 <= marks <= 100:
        return "O"
    else:
        return "Invalid"

subjects = []

for i in range(1, 4):
    name = input(f"Enter the name of subject {i} : ")
    marks = input(f"Enter marks for {name} (or 'Absent') : ").strip()
    subjects.append((name, marks))

is_fail = any(marks == "Absent" or (marks.isdigit() and int(marks) <= 39) for _, marks in subjects)

if not is_fail:
    total = sum(int(marks) for _, marks in subjects if marks.isdigit())
    average = total / len(subjects)
else:
    total = "Not Applicable"
    average = "Not Applicable"

# Print results :

print("\nSubject-wise Grades:")

for i, (name, marks) in enumerate(subjects):
    grade = get_grade(marks)
    print(f"{i + 1}. {name} : Marks = {marks}, Grade = {grade}")

print("\nResults:")

print(f"Total Marks : {total}")
print(f"Average Marks : {average}")
print(f"Final Status : {'Fail' if is_fail else 'Pass'}")