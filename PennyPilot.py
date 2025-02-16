import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime
    
# File to store expenses
csv_file = "expenses1.csv"

# Initialize CSV file
def init_csv():
    if not os.path.exists(csv_file):
        df = pd.DataFrame(columns=["Category", "Amount", "Date"])
        df.to_csv(csv_file, index=False)

# Load data from CSV
def load_data():
    if os.path.exists(csv_file):
        return pd.read_csv(csv_file)
    else:
        return pd.DataFrame(columns=["Category", "Amount", "Date"])

# Save an expense to the CSV
def save_expense(category, amount):
    df = load_data()
    date = datetime.now().strftime("%Y-%m-%d")
    new_expense = {"Category": category, "Amount": amount,"Date":date}
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    df.to_csv(csv_file, index=False)

# View all expenses
def view_expenses():
    df = load_data()
    if df.empty:
        print("\nNo expenses recorded yet.")
    else:
        print("\nExpenses Summary:")
        print(df)

# Calculate total expenses
def calculate_total_expenses():
    df = load_data()
    total = df["Amount"].sum()
    print(f"\nTotal Expenses: ${total:.2f}")

# Set budgets
def set_budget():
    budgets = {}
    print("\nEnter budgets for categories. Type 'done' when finished.")
    while True:
        category = input("Enter category (or 'done' to finish): ").capitalize()
        if category.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter budget for {category}: "))
            budgets[category] = amount
        except ValueError:
            print("Invalid amount. Please enter a number.")
    print("\nBudgets have been set!")
    return budgets

# Budget Alerts
def budget_alerts(budgets):
    df = load_data()
    if df.empty:
        print("\nNo expenses to analyze for budget alerts.")
        return
    category_totals = df.groupby("Category")["Amount"].sum()
    for category, budget in budgets.items():
        if category_totals.get(category, 0) > budget:
            print(f"Alert: You have exceeded the budget for {category}!")
    print("\nBudget analysis completed.")

# Visualization of expenses
def visualize_expenses():
    df = load_data()
    if df.empty:
        print("\nNo expenses to visualize.")
        return
    category_totals = df.groupby("Category")["Amount"].sum()
    category_totals.plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Expense Distribution by Category")
    plt.ylabel("")
    plt.show()

# Main Program
def main():
    init_csv()
    print("Welcome to the Personal Expenses Calculator!")
    budgets = {}

    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Calculate total expenses")
        print("4. Set budgets")
        print("5. Budget alerts")
        print("6. Visualize expenses")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            category = input("Enter the category (e.g., Food, Rent, Entertainment): ").capitalize()
            try:
                amount = float(input("Enter the expense amount: "))
                save_expense(category, amount)
                print(f"Added ${amount:.2f} to {category}.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            calculate_total_expenses()

        elif choice == '4':
            budgets = set_budget()

        elif choice == '5':
            if not budgets:
                print("\nNo budgets set. Please set budgets first.")
            else:
                budget_alerts(budgets)

        elif choice == '6':
            visualize_expenses()

        elif choice == '7':
            print("Thank you for using the Personal Expenses Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()