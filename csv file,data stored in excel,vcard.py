#create a csv file that we can directly open in MS-Excel.
import csv

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow([001, "meet", 85, 90, 78])
    writer.writerow([002, "aryan", 80, 70, 88])
#Read the data stored in MS-Excel file and convert it into a dictionary.
import csv

data_dict = {}
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row["Subject1"]) + int(row["Subject2"]) + int(row["Subject3"])
        data_dict[row["Roll No"]]={
            "name": row["Name"],
            "subjects": [int(row["Subject1"]), int(row["Subject2"]), int(row["Subject3"])],
            "total": total}
print(data_dict)
#create a vcard that we can directly store in our mobile.
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD
"""

with open("contact.vcf", "w") as file:
    file.write(vcard)














    
