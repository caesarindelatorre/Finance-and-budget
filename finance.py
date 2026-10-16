import sys

def main_menu():

    from datetime import datetime
    balance = 0.0
    expenses = 0.0
    expense_history = {}
    budgets = 0.0
    budget_history = {}


    while True:
        print()
        print("finance and budget")
        print()
        print("1. insert income")
        print("2. insert expense")
        print("3. view balance")
        print("4. expense history")
        print("5. budget")
        print("6. budget history")
        print("7. exit")
        print()
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                print()
                print("1. insert income")
                print("2. main menu")
                next = input("next: ")
                if next == "1":
                    income = float(input("Enter the amount of income: $"))
                    balance += income
                else:
                    break
        elif choice == "2":
            while True:
                print()
                print("1. insert expense")
                print("2. main menu")
                next = input("next: ")
                if next == "1":
                    expense = float(input("Enter the amount of expense: $"))
                    balance -= expense
                    expense_history[datetime.now().strftime("%m/%d/%Y")] = expense_history.get(datetime.now().strftime("%m/%d/%Y"), 0) + expense
                    break
        elif choice == "3":      
            while True:
                print()
                print("Current balance: $", balance)
                input("press enter to return to main menu")
                break
        elif choice == "4":
            while True:
                print()
                print("1. view all expense history")
                print("2. view expense history by day, month and year")
                print("3. main menu")
                next = input("next: ")
                if next == "1":
                    print()
                    print("Expense history:")
                    print(expense_history)
                elif next == "2":
                    print()
                    day = input("what is the day of the expense? month/day/year: ")
                    if day not in expense_history:
                        print("invalid date format. please use the format month/day/year.")
                    else:
                        print(expense_history[day])
                else:
                    break
        elif choice == "5":
            while True:
                print()
                print("1. insert budget")
                print("2. main menu")
                next = input("next: ")
                if next == "1":
                    print()
                    budget = float(input("Enter your monthly budget: $"))
                    balance -= budget
                    budget_history[datetime.now().strftime("%m/%d/%Y")] = budget_history.get(datetime.now().strftime("%m/%d/%Y"), 0) + budget
                    if len(datetime.now().strftime("%m/%d/%Y")) != 8:
                        print("invalid date format. please use the format month/day/year.")
                        break
                    else:
                        budget_history[day] = budget_history.get(day, 0) + budget
                else:
                    break
        elif choice == "6":
            while True:
                print()
                print("Budget history:")
                print("1. view all budget history")
                print("2. view budget history by day, month and year")
                print("3. main menu")
                n = input("next: ")
                if n == "1":
                    print()
                    print(budget_history)
                elif n == "2":
                    print()
                    day = input("what is the day of the budget? month/day/year: ")
                    if len(day) != 10:
                        print("invalid date format. please use the format month/day/year, or no budget entered for that day.")
                    else:
                        print("your spent budget for", day, "is:", budget_history[day])
                else:
                    break
        elif choice == "7":
            break
        else:
            print()
            print("Invalid choice. Please try again.")

    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        app_choice = sys.argv[1].lower()
        if app_choice == "finance":
            main_menu()
        else:
            print("Invalid argument. app does not exist.")
    