# 06. Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.

def merge_alternate_lines(file1_path, file2_path, output_path):
    def get_sentences(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            # Split by '.' and remove any trailing empty strings
            sentences = [s.strip() + '.' for s in content.split('.') if s.strip()]
        return sentences

    sentences1 = get_sentences(file1_path)
    sentences2 = get_sentences(file2_path)

    max_len = max(len(sentences1), len(sentences2))

    with open(output_path, 'w') as out:
        for i in range(max_len):
            if i < len(sentences1):
                out.write(sentences1[i] + ' ')
            if i < len(sentences2):
                out.write(sentences2[i] + ' ')

    print(f"✅ Merged sentences written to '{output_path}'.")

# Example usage
file1 = 'LabDay10/test_10.05.txt'
file2 = 'LabDay10/test_10.08.txt'
output_file = 'LabDay10/output_10.06.txt'

merge_alternate_lines(file1, file2, output_file)