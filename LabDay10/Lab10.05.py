# 05. Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.

def copy_and_convert_to_upper(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        # Convert lowercase characters to uppercase
        upper_content = content.upper()

        with open(destination_file, 'w') as dest:
            dest.write(upper_content)

        print(f"✅ Contents copied from '{source_file}' to '{destination_file}' with lowercase converted to uppercase.")

    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source = "LabDay10/test_10.05.txt"
destination = "LabDay10/output_10.05.txt"
copy_and_convert_to_upper(source, destination)