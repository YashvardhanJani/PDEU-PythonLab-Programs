""" 
08. Implement a String class containing the following functions:
a.	Overloaded += operator function to perform string concatenation
b.	Method toLower() to convert upper case letters to lower case.
c.	Method toUpper() to convert lower case letters to upper case. """

class String:
    def __init__(self, content=""):
        self.content = content

    def __str__(self):
        return self.content

    def __iadd__(self, other):
        if isinstance(other, String):
            self.content += other.content
        elif isinstance(other, str):
            self.content += other
        else:
            raise TypeError("Can only concatenate String or str type")
        return self

    def toLower(self):
        self.content = self.content.lower()

    def toUpper(self):
        self.content = self.content.upper()


# Main Program
def main():
    s1 = String(input("Enter first string: "))
    s2 = String(input("Enter second string: "))

    print("\nOriginal Strings:")
    print("s1 =", s1)
    print("s2 =", s2)

    s1 += s2
    print("\nAfter Concatenation (s1 += s2):")
    print("s1 =", s1)

    s1.toLower()
    print("\nAfter Converting to Lowercase:")
    print("s1 =", s1)

    s1.toUpper()
    print("\nAfter Converting to Uppercase:")
    print("s1 =", s1)


if __name__ == "__main__":
    main()