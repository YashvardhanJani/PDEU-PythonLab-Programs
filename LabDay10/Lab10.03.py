# 03. Accept contact details from the user and create a vcard that we can directly store in our mobile.

import os

def create_vcard():

    # # To input specific path
    # folder_path = input("Enter the folder path where you want to save the vCard(s): ").strip()
    # # Create folder if it doesn't exist
    # if not os.path.exists(folder_path):
    #     os.makedirs(folder_path)
    #     print(f"📁 Folder '{folder_path}' created.")

    while True:
        print("\nEnter contact details:\n")
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email Address: ")
        address = input("Address: ")
        organization = input("Organization (optional): ")

        vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{full_name}
TEL;TYPE=CELL:{phone_number}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
ORG:{organization}
END:VCARD
"""

        filename = full_name.replace(" ", "_").lower() + ".vcf"
        # filepath = os.path.join(folder_path, filename)
        filepath = os.path.join("LabDay10/", filename)

        with open(filepath, "w") as file:
            file.write(vcard_content)

        print(f"\n✅ vCard saved as '{filepath}'. You can now transfer it to your phone and import it into your contacts.")

        another = input("\nDo you want to create another vCard? (Y/N): ").strip().upper()
        if another != 'Y':
            print("\n👋 Program terminated.")
            break

create_vcard()