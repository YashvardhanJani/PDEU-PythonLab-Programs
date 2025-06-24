# Write a program to create a user-defined class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.

class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

    def __str__(self):
        return f"{self.date[0]:02d}-{self.date[1]:02d}-{self.date[2]}"

def input_date(prompt):
    print(prompt)
    day = int(input("Enter day (1-31): "))
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (e.g., 2025): "))
    return Date(day, month, year)

# Create two date objects from user input
date1 = input_date("Enter 1st date:")
date2 = input_date("Enter 2nd date:")

print("\nDate 1:", date1)
print("Date 2:", date2)


if date1 == date2:
    print("The two dates are equal.")
else:
    print("The two dates are NOT equal.")