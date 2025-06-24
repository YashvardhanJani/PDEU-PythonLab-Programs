# 01. Write a program to create a csv file that we can directly open in MS-Excel.

import csv
import os

def create_csv(filename):
    data = [
        ["Name", "Age", "City"],
        ["Yashvardhan", 18, "Jamjodhpur"],
        ["Rushi", 18, "Bhuj"],
        ["Dhruv", 12 , "Jamjodhpur"],
        ["Jaydev", 6 , "Jamnagar"]
    ]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"CSV file '{os.path.basename(filename)}' created successfully!")

create_csv("LabDay10/output_10.01.csv")