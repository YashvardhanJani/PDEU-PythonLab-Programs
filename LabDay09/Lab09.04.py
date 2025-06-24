# 04. Write a program that defines a function sum_avg() to accept marks of five subjects and calculates total and average. It should return directly both values.

def sum_avg(n):
    subjects = []
    for i in range(1, n+1):
        name = input(f"Enter the name of subject {i} : ")
        marks = input(f"Enter marks for {name} : ").strip()
        subjects.append((name, marks))

    total = sum(int(marks) for _, marks in subjects if marks.isdigit())
    average = total / len(subjects)

    print(f"\nTotal Marks : {total}")
    print(f"Average Marks : {average}")

sum_avg(5)    