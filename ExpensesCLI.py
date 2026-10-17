
import csv
import json
from pathlib import Path

DATA_FILE = "expenses.json"
CSV_FILE = "expenses.csv"

def load_expenses():
    if Path(DATA_FILE).exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load saved expenses.")
    return []

def save_expenses():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    name = input("Expense name: ").strip()
    if not name:
        print("Expense name is required.")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Category: ").strip()
    if not category:
        print("Category is required.")
        return

    expenses.append({
        "expense": name,
        "amount": amount,
        "category": category
    })
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    for count, item in enumerate(expenses, start=1):
        print(
            f'{count}. {item["expense"]} | '
            f'₹{item["amount"]:.2f} | {item["category"]}'
        )

def search_expense():
    name = input("Enter expense name to search: ").strip().lower()
    matches = [
        item for item in expenses
        if name and name in item["expense"].lower()
    ]

    if not matches:
        print("Expense not found.")
        return

    for item in matches:
        print(f'Name: {item["expense"]}')
        print(f'Amount: ₹{item["amount"]:.2f}')
        print(f'Category: {item["category"]}')

def view_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total Expenses: ₹{total:.2f}")

def export_csv():
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["expense", "amount", "category"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported successfully to {CSV_FILE}!")

expenses = load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Search expense")
    print("4. View total expenses")
    print("5. Export to CSV")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        view_total()
    elif choice == "5":
        export_csv()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-6.")
