# 08. Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.

def remove_articles(input_file, output_file):

    words_to_remove = {'a', 'an', 'the'}

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.split()
            new_line = ' '.join('' if word.lower() in words_to_remove else word for word in words)
            # Replace multiple spaces with single space and strip
            outfile.write(' '.join(new_line.split()) + '\n')
    print(f"✅ Program exicuted!")       

remove_articles('LabDay10/test_10.08.txt', 'LabDay10/output_10.08.txt')