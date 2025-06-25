# 05. Write a program that creates and uses a Time class to perform various time arithmetic operations.

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        # Convert seconds > 60 and minutes > 60
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def add(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        result = Time()
        result.from_seconds(total_seconds)
        return result

    def subtract(self, other):
        total_seconds = abs(self.to_seconds() - other.to_seconds())
        result = Time()
        result.from_seconds(total_seconds)
        return result


# Main program to demonstrate usage
def main():
    print("Enter first time:-")
    h1 = int(input("Hours: "))
    m1 = int(input("Minutes: "))
    s1 = int(input("Seconds: "))

    print("\nEnter second time:-")
    h2 = int(input("Hours: "))
    m2 = int(input("Minutes: "))
    s2 = int(input("Seconds: "))

    time1 = Time(h1, m1, s1)
    time2 = Time(h2, m2, s2)

    print("\nTime 1: ", end="")
    time1.display()

    print("Time 2: ", end="")
    time2.display()

    print("\nAddition Result: ", end="")
    time1.add(time2).display()

    print("Subtraction Result (absolute): ", end="")
    time1.subtract(time2).display()


if __name__ == "__main__":
    main()