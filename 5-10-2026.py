# ================================
#        EXPENSE MANAGER
# ================================

# 1. Add Expense
# 2. View Expenses
# 3. Update Expense
# 4. Delete Expense
# 5. Search Expenses
# 6. Monthly Summary
# 7. Category Summary
# 8. Exit

# Choose an option:

class ExpenseM():

    def __init__(self):
        self.Expenses = []

    def Add_Expense(self,category,description,date,Amount):

        expense = {
            "category":category,
            "description":description,
            "date":date,
            "Amount":Amount
        }

        self.Expenses.append(expense)

        return print("Your Expense Is Add Successfully")

    def view_expenses_list(self):
 

        total = sum(Expense["Amount"] for Expense in self.Expenses)
        print(f"YOUR TOTAL EXPENSES {self.Expenses}")

        response = input("Do You Want TOTAL EXPENSE AMOUNT :")

        if response.lower() == "y" :
            return print(total)


    def Delete_Expense(self):

        INPUT =input("WHICH CATEGORY DO YOU WANT TO DELETE ")

        for expense in self.Expenses :
            if expense["category"] == INPUT :
                self.Expenses.remove(expense)
                break
            
            else :
                print("NOT Found")

        return print(f"Your Expense  Is Deleted \n Your Updated Expenses Is {self.Expenses}")


    def Category_Summary(self):

        self.categories = {}

        for item in self.Expenses :
            key = item["category"]
            value = item["Amount"]

            if key not in self.categories :
                self.categories[key] = 0

            self.categories[key] += int(value)


        return print(f"YOUR CATEGORY WISE EXPENSE IS \n {"="*10} {self.categories}{"="*10} ")


    def Update_expense(self):

        print("=" * 20)

        category = input("WHICH EXPENSE YOU WANT TO UPDATE: ")

        specific_expense = input(
            "WHAT DO YOU WANT TO UPDATE "
            "(category/description/date/Amount): "
        )

        value = input("ENTER NEW VALUE: ")

        print("=" * 20)

        for expense in self.Expenses:

            if expense["category"] == category:

                if specific_expense == "category":
                    expense["category"] = value

                elif specific_expense == "description":
                    expense["description"] = value

                elif specific_expense == "date":
                    expense["date"] = value

                elif specific_expense == "Amount":
                    expense["Amount"] = float(value)

                else:
                    print("INVALID EXPENSE FIELD")

                break

        else:
            print("EXPENSE NOT FOUND")

        print("=" * 20)

        print(f"THIS IS YOUR UPDATED LIST\n{self.Expenses}")



def menu(self):
    while True:

        print("""
================================
        EXPENSE MANAGER
================================
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Search Expenses
6. Monthly Summary
7. Category Summary
8. Exit
================================
""")

        choice = input("Choose an option: ")

        if choice == "1":
           self.Add_expense()
        elif choice == "2":
             self.view_expenses_list()
        elif choice == "3":
             self.Category_Summary()
        elif choice == "4":
             self.Delete_Expense()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid option!")

# expense_manager = ExpenseM()

# category = input("Enter category: ")
# description = input("Enter description: ")
# date = input("Enter date: ")
# Amount = float(input("Enter amount: "))
# expense_manager.Add_Expense(category,description,date,Amount)

# category = input("Enter category: ")
# description = input("Enter description: ")
# date = input("Enter date: ")
# Amount = float(input("Enter amount: "))

# expense_manager.Add_Expense(category,description,date,Amount)

# expense_manager.view_expenses_list()
# expense_manager.Category_Summary()
# expense_manager.Update_expense()



