class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0

    def add_daily_expenses(self, date, number):
        for i in range(number):
            print(f"\nExpense {i + 1}")

            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))

            expense = Expense(date, description, amount)
            self.expenses.append(expense)

        print(f"\n{number} expenses added successfully!")

    def edit_expense(self, index):
        if 0 <= index < len(self.expenses):

            expense = self.expenses[index]

            print("\nCurrent Expense:")
            print(f"Date: {expense.date}")
            print(f"Description: {expense.description}")
            print(f"Amount: Rs. {expense.amount:.2f}")

            print("\nEnter new details:")

            expense.date = input("Enter new date (YYYY-MM-DD): ")
            expense.description = input("Enter new description: ")
            expense.amount = float(input("Enter new amount: "))

            print("Expense updated successfully.")

        else:
            print("Invalid expense number.")


    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense number.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("\nNo expenses found.")
        else:
            print("\n --EXPENSE LIST--")

            for i, expense in enumerate(self.expenses, start=1):
                print(
                    f"{i}. Date: {expense.date}, "
                    f"Description: {expense.description}, "
                    f"Amount: Rs. {expense.amount:.2f}"
                )

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def set_budget(self, budget):
        self.monthly_budget = budget
        print(f"Monthly budget set to Rs. {budget:.2f}")

    
    def monthly_summary(self):
        total = sum(expense.amount for expense in self.expenses)

        print("\n-------MONTHLY SUMMARY-------")
        print(f"Monthly Budget : Rs. {self.monthly_budget:.2f}")
        print(f"Total Spent    : Rs. {total:.2f}")

        if self.monthly_budget == 0:
            print("Budget has not been set.")

        elif total < self.monthly_budget:
            remaining = self.monthly_budget - total
            print(f"Remaining      : Rs. {remaining:.2f}")
            print("Status: You are within your budget.")

        elif total == self.monthly_budget:
            print("Remaining      : Rs. 0.00")
            print("Status: You have reached your budget.")

        else:
            exceeded = total - self.monthly_budget
            print(f"Over Budget By : Rs. {exceeded:.2f}")
            print("WARNING: You have exceeded your budget!")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():

    tracker = ExpenseTracker()

    while True:

        print("\n-------- EXPENSE TRACKER --------")
        print("1. Add Daily Expenses")
        print("2. Edit Expense")
        print("3. Remove Expense")
        print("4. View Expenses")
        print("5. Set Monthly Budget")
        print("6. Monthly Summary")
        print("7. Exit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        choice = input("Enter your choice (1-7): ")

        
        if choice == "1":

            date = input("Enter the date (YYYY-MM-DD): ")

            number = int(input("How many expenses do you want to add today? "))

            tracker.add_daily_expenses(date, number)

        
        elif choice == "2":

            tracker.view_expenses()

            if len(tracker.expenses) > 0:

                index = int(input("Enter the expense number to edit: "))

                tracker.edit_expense(index - 1)

        elif choice == "3":

            tracker.view_expenses()

            if len(tracker.expenses) > 0:

                index = int(input("Enter the expense number to remove: "))

                tracker.remove_expense(index - 1)

        elif choice == "4":
            tracker.view_expenses()

        elif choice == "5":

            budget = float(input("Enter your monthly budget: "))

            tracker.set_budget(budget)

        
        elif choice == "6":
            tracker.monthly_summary()

        
        elif choice == "7":
            print("\nExiting Expense Tracker!")
            print("Thank you for using the Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()