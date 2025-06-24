# Read a file and display its contents along with line number at the beginning of each line.

def display_file_with_line_numbers(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line}", end='')  # end='' avoids adding extra newline
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

filename = input("Enter the filename (with extension): ")
display_file_with_line_numbers(filename)