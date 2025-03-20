import csv
import os
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Categories for expenses
CATEGORIES = ["Food", "Transportation", "Entertainment", "Bills", "Shopping", "Others"]

def initialize_file():
    """Create file if it does not exist and add sample data."""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            sample_data = [
                ["2024-03-01", 500, "Food", "Lunch at a restaurant"],
                ["2024-03-02", 200, "Transportation", "Bus fare"],
                ["2024-03-03", 1500, "Shopping", "New shoes"],
                ["2024-03-04", 800, "Bills", "Electricity bill"],
                ["2024-03-05", 300, "Entertainment", "Movie ticket"],
                ["2024-03-06", 600, "Food", "Grocery shopping"],
                ["2024-03-07", 250, "Transportation", "Taxi ride"],
                ["2024-03-08", 1200, "Shopping", "Clothing purchase"],
                ["2024-03-09", 500, "Bills", "Internet bill"],
                ["2024-03-10", 450, "Entertainment", "Concert ticket"],
                ["2024-03-11", 700, "Food", "Dinner at a cafe"],
                ["2024-03-12", 180, "Transportation", "Subway ticket"],
                ["2024-03-13", 1600, "Shopping", "Smartphone accessories"],
                ["2024-03-14", 900, "Bills", "Water bill"],
                ["2024-03-15", 350, "Entertainment", "Amusement park"]
            ]
            writer.writerows(sample_data)

def add_expense():
    """Add an expense entry."""
    try:
        amount = float(input("Enter the amount spent: "))
        print("Select category:")
        for idx, category in enumerate(CATEGORIES, 1):
            print(f"{idx}. {category}")
        category_index = int(input("Enter category number: "))
        category = CATEGORIES[category_index - 1]
        description = input("Enter description: ")
        date = datetime.today().strftime('%Y-%m-%d')
        
        with open(EXPENSE_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])
        print("Expense added successfully!")
    except (ValueError, IndexError):
        print("Invalid input! Please try again.")

def view_expenses():
    """Display all recorded expenses."""
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                print(f"Date: {row[0]}, Amount: ₹{row[1]}, Category: {row[2]}, Description: {row[3]}")
    except FileNotFoundError:
        print("No expense records found.")

def monthly_summary():
    """Generate a monthly summary of expenses."""
    expenses = {}
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                month = row[0][:7]  # Extract YYYY-MM format
                amount = float(row[1])
                expenses[month] = expenses.get(month, 0) + amount
        
        for month, total in expenses.items():
            print(f"Month: {month}, Total Expense: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expense records found.")

def category_summary():
    """Generate a category-wise summary of expenses."""
    category_expenses = {category: 0 for category in CATEGORIES}
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                category_expenses[row[2]] += float(row[1])
        
        for category, total in category_expenses.items():
            print(f"Category: {category}, Total Expense: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expense records found.")

def main():
    initialize_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
