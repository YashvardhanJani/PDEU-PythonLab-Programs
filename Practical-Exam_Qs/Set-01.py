"""
Write a complete Python program to convert a given string into an encrypted text using following rules:
* For each character of a string, add & subtract two consecutive prime numbers respectively.
* First prime number to use is 5 then 7 and so on.
* Write string in first line and encrpted string in second line of file.
"""

def is_prime(current):
    if current < 2:
        return False
    for i in range(2, int(current**0.5) + 1):
        if current % i == 0:
            return False
    return True

def generate_primes(num):
    prime_num = []
    current = 5
    while len(prime_num) < num:
        if is_prime(current):
            prime_num.append(current)
        current += 1
    return prime_num

def encryption(string):
    n = len(string)
    prime_num = generate_primes(n)
    encrypted_str = ""

    for i, ch in enumerate(string): 
        new_ascii = ord(ch) + prime_num[i] if i % 2 == 0 else ord(ch) - prime_num[i]

        # keep characters in printable ASCII range (32–126)
        new_ascii = 32 + (new_ascii - 32) % 95

        encrypted_str += chr(new_ascii)

    return encrypted_str

def write_to_file(original, encrypted, filename="Practical-Exam_Qs/output.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("Original String: " + original + "\n")
            f.write("Encrypted String: " + encrypted + "\n")
            f.write("\n")
        print(f"Encrypted string written to file '{filename}' successfully.")
    except Exception as e:
        print("Error writing to file:", e)

# Main
input_str = input("Enter the string for encryption: ")
encrypted_str = encryption(input_str)
print(f"Encrypted string: {encrypted_str}")
write_to_file(input_str, encrypted_str)