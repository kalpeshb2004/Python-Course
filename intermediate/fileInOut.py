# P1 — Easy
# notes.txt file banao. User se 3 lines lo input se aur file me likho. Phir file padhke print karo.

with open("notes.txt","w") as f:
     for i in range(3):
          enter = input(f"enter {i+1}: ")
          f.write(enter + "\n")

with open("notes.txt","r") as f:
     content = f.read()

print(content)


# P2 — Medium
# students.txt file me 5 students ka data likho (name, marks). File padho aur sirf passing students (marks >= 40) print karo.

with open("students.txt" , "w") as f:
    f.write("kalpesh,21\n")
    f.write("jayesh,25\n")
    f.write("ram,73\n")
    f.write("krishna,78\n")
    f.write("laxman,67")

with open("students.txt","r") as f:
    for line in f:
        name,marks = line.strip().split(",")
        marks = int(marks)
        if marks >= 25:
            print(name,marks)

# P3 — Medium
# contacts.json file banao. Program me:
# Contact add karo (name, phone) → json me save
# Naam se search karo → json se load karke dhundo
# Contact delete karo → update karke save

import json

# 1. File me initial data save karo
contacts = [
    {"name": "Kalpesh", "phone": "9876543210"},
    {"name": "Ram",     "phone": "9999999999"}
]
#file me save kiya 
with open("contact.json", "w") as f:
    json.dump(contacts, f, indent=4)

# 2. File se load karo
with open("contact.json", "r") as f:
    contacts = json.load(f)

# 3. Contact add karo
contacts.append({"name": "Jayesh", "phone": "8888888888"})
with open("contact.json", "w") as f:
    json.dump(contacts, f, indent=4)
print("Contact added!")

# 4. Search karo
search = "Kalpesh"
with open("contact.json", "r") as f:
    contacts = json.load(f)
for contact in contacts:
    if contact["name"] == search:
        print(f"Found: {contact}")

# 5. Delete karo
delete = "Ram"
with open("contact.json", "r") as f:
    contacts = json.load(f)
new_contacts = [c for c in contacts if c["name"] != delete]

with open("contact.json", "w") as f:
    json.dump(new_contacts, f, indent=4)

print(f"{delete} deleted!")

print(new_contacts)

import csv
import os

FILE_NAME = "expenses.csv"

# File create karo aur header add karo
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount"])


def add_expense(date, category, amount):
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print("Expense Added!")


def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            total += float(row["amount"])

    print("Total Expenses =", total)


def expenses_by_category():
    category_totals = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            category = row["category"]
            amount = float(row["amount"])

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    print("\nCategory Wise Expenses:")
    for category, total in category_totals.items():
        print(category, ":", total)


def highest_expense():
    max_row = None
    max_amount = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            amount = float(row["amount"])

            if amount > max_amount:
                max_amount = amount
                max_row = row

    if max_row:
        print("\nHighest Expense:")
        print(
            f"Date: {max_row['date']}, "
            f"Category: {max_row['category']}, "
            f"Amount: {max_row['amount']}"
        )


# Sample Data
add_expense("2026-06-22", "Food", 200)
add_expense("2026-06-22", "Travel", 500)
add_expense("2026-06-23", "Food", 300)
add_expense("2026-06-24", "Shopping", 1000)

# Outputs
total_expenses()
expenses_by_category()
highest_expense()