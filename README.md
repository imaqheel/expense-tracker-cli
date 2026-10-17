# Expense Tracker CLI

A command-line expense tracker built with Python to record, manage, search, and calculate personal expenses.

## Features

- **Add Expenses:** Record expense names, amounts, and categories.
- **View Expenses:** Display all saved expenses.
- **Search Expenses:** Find expenses by name, including partial and case-insensitive matches.
- **Calculate Total:** Calculate the total amount spent.
- **Export to CSV:** Export expense records to a CSV file.
- **Persistent Storage:** Save expenses in JSON so they remain available after restarting the program.
- **Input Validation:** Handle invalid amounts and empty fields.
- **Menu-Driven Interface:** Choose features from a simple command-line menu.

## Technologies Used

- Python
- JSON
- CSV
- PyCharm

## Requirements

- Python 3.10 or later

## How to Run

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Open the project folder in your terminal.

3. Run the program:

   ```bash
   python ExpensesCLI.py
   ```

## Usage

Choose an option from the menu:

1. Add expense
2. View expenses
3. Search expense
4. View total expenses
5. Export to CSV
6. Exit

## Project Structure

```text
Express CLI/
├── ExpensesCLI.py
├── README.md
├── .gitignore
├── expenses.json   # Created when expenses are saved
└── expenses.csv    # Created when expenses are exported
```

Personal expense data files are excluded from version control through `.gitignore`.

## Learning Outcomes

This project helped me practise Python fundamentals, including functions, loops, conditional statements, lists, dictionaries, exception handling, file handling, JSON, and CSV.

## Future Improvements

- Add expense editing and deletion.
- Filter expenses by category.
- Generate monthly expense reports.
- Add automated tests with pytest.

## Author

Created as a Python learning project.
