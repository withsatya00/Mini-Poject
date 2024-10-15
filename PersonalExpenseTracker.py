expenses=[]
def add_expense():
    amount=float(input("Enetr the expense:\n"))
    category=input("Enetr the category of expense:\n")
    expenses.append({"amount": amount,"category":category})
    
def view_expense():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for idx, expense in enumerate(expenses,1):
            print(f"({idx}.{expense['category']}:{expenses['amount']})")