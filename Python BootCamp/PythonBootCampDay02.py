"""
In this assignment you’ll be building your own Personal Expense Tracker based on what we covered in the Day 2 session of the Python Bootcamp. This command-line app will help you track daily expenses with the following features:
Requirements:

1. Add Expenses with categories.
2. View All Expenses and calculate your total spending.
3. Save Expenses to a text file for record-keeping.
"""

import os
import datetime
import csv

exp_file = "expense_file.txt"

def add_exp(expense):  # Adds a new expense to the expense file
    with open(exp_file, 'a') as file:
        file.write(expense + "\n")
    print("Expense ADDED Successfully!")

def view_exp():  # Displays all recorded expenses
    if not os.path.exists(exp_file):
        print("OOPS!! No Expense Found")
        return
    
    head = "Date".center(12, ' ') + " | " + "Category".center(15, ' ') + " | " + "Amount(in Rs.)".center(15, ' ') + " | " + "Description".center(25, ' ')
    print(head)
    print("-" * len(head))
    
    with open(exp_file, 'r') as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 4:  # Ensure we have exactly 4 parts
                date, category, amt, description = parts
                print(f"{date.ljust(12, ' ')} | {category.ljust(15, ' ')} | {amt.ljust(15, ' ')} | {description.ljust(25, ' ')}")
            else:
                print(f"Invalid entry: {line.strip()}")

def del_exp():  # Deletes an expense from the expense file
    expenses = []
    with open(exp_file, "r") as file:
        expenses = file.readlines()
    
    for i, line in enumerate(expenses):
        parts = line.strip().split(", ")
        if len(parts) == 4:  # Ensure we have exactly 4 parts
            date, category, amt, description = parts
            print(f"{i + 1}. {date} | {category} - ₹{amt}")
    
    choice = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= choice < len(expenses):
        del expenses[choice]
        with open(exp_file, "w") as file:
            file.writelines(expenses)
        print("Expense DELETED Successfully!")
    else:
        print("Invalid choice OR No Expense")

def edit_exp():  # Edits an existing expense
    expenses = []
    with open(exp_file, "r") as file:
        expenses = file.readlines()
    
    if not expenses:
        print("OOPS!! No Expense Found")
        return
    
    print("Current Expenses:")
    for i, line in enumerate(expenses):
        parts = line.strip().split(", ")
        if len(parts) == 4:  # Ensure we have exactly 4 parts
            date, category, amt, description = parts
            print(f"{i + 1}. {date} | {category} - ₹{amt}")

    try:
        choice = int(input("Enter the number of the expense to edit: ")) - 1
        if 0 <= choice < len(expenses):
            date, category, amt, description = expenses[choice].strip().split(", ")
            new_category = input(f"Enter new category (current: {category}) or press Enter to keep it the same: ")
            new_amt = input(f"Enter new amount (current: ₹{amt}) or press Enter to keep it the same: ")
            if new_category.strip() == "":
                new_category = category
            if new_amt.strip() == "":
                new_amt = amt
            expenses[choice] = f"{date}, {new_category}, {new_amt}, {description}\n"
            with open(exp_file, "w") as file:
                file.writelines(expenses)
            print("Expense UPDATED Successfully!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def exp_stat():  # Displays monthly expense statistics
    if not os.path.exists(exp_file):
        print("OOPS!! No Expense Found")
        return

    monthly_expenses = {}
    with open(exp_file, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 4:  # Ensure we have exactly 4 parts
                date, category, amt, description = parts
                amt = float(amt)
                date = datetime.datetime.strptime(date, "%d-%m-%Y")
                month_year = date.strftime("%B %Y")
                
                if month_year not in monthly_expenses:
                    monthly_expenses[month_year] = []
                monthly_expenses[month_year].append(amt)

    if not monthly_expenses:
        print("No expenses to analyze.")
        return

    print("\n--- Monthly Expense Statistics ---")
    for month_year, expenses in monthly_expenses.items():
        total_expenses = sum(expenses)
        average_expense = total_expenses / len(expenses)
        max_expense = max(expenses)
        min_expense = min(expenses)
        
        print(f"\n{month_year.center(30, ' ')}:")
        print(f"  Total Spending: ₹{total_expenses:.2f}".ljust(40))
        print(f"  Average Spending: ₹{average_expense:.2f}".ljust(40))
        print(f"  Maximum Expense: ₹{max_expense:.2f}".ljust(40))
        print(f"  Minimum Expense: ₹{min_expense:.2f}".ljust(40))

def csv_file():  # Exports expenses to a CSV file
    if not os.path.exists(exp_file):
        print("OOPS!! No Expense Found")
        return
    
    csv_filename = input("Enter the CSV file name (with .csv extension): ")
    
    with open(exp_file, "r") as file:
        expenses = file.readlines()

    if not expenses:
        print("OOPS!! No Expense Found")
        return
    
    with open(csv_filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Date", "Category", "Amount", "Description"])
        
        for line in expenses:
            parts = line.strip().split(", ")
            if len(parts) == 4:  # Ensure we have exactly 4 parts
                date, category, amt, description = parts
                csvwriter.writerow([date, category, amt, description])
            else:
                print(f"Skipping invalid line: {line.strip()}")

while True:
    print("Personal Expense Tracker")
    print("'Add'    - Add Expense")
    print("'View'   - View Expense")
    print("'Delete' - Delete Expense")
    print("'Edit'   - Edit Expense")
    print("'Stat'   - Show Expense Statistics")
    print("'Export' - Export to CSV file")
    print("'Exit'   - To exit from Expense Tracker")

    choice = input("Choose: ").strip().lower()

    if choice == "add":
        date = input("Enter Date(DD-MM-YYYY): ")
        category = input("Category(Food, Travel, Med, etc...): ")
        amt = float(input("Amount: "))
        description = input("Description: ")
        exp = f"{date}, {category}, {amt}, {description}"
        add_exp(exp)
    elif choice == "view":
        view_exp()
    elif choice == "delete":
        del_exp()
    elif choice == "edit":
        edit_exp()
    elif choice == "stat":
        exp_stat()
    elif choice == "export":
        csv_file()
    elif choice == "exit":
        print("!!Come Again!!")
        break
    else:
        print("!!Invalid Command!!")
