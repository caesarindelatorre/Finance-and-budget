from datetime import date
balance = 0.0
expenses = 0.0
expense_history = {}
budgets = 0.0
budget_history = {}

while True:
    print("finance and budget")
    print()
    print("1. insert income")
    print("2. insert expense")
    print("3. view balance")
    print("4. expense history")
    print("5. budget")
    print("6. budget history")
    print("7. exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
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
            print("1. insert expense")
            print("2. main menu")
            next = input("next: ")
            print("1. insert expense")
            print("2. main menu")
            if next == "1":
                expense = float(input("Enter the amount of expense: $"))
                balance -= expense
                day = input("what is the day of the expense? month/day/year: ")
                expense_history[day] = expense_history.get(day, 0) + expense
            else:
                break
    elif choice == "3":      
        while True:
            print("Current balance: $", balance)
            input("press enter to return to main menu")
            break
    elif choice == "4":
        while True:
            print("1. view all expense history")
            print("2. view expense history by day, month and year")
            print("3. main menu")
            next = input("next: ")
            if next == "1":
                print("Expense history:")
                print(expense_history)
            elif next == "2":
                day = input("what is the day of the expense? month/day/year: ")
                if len(day) != 8:
                    print("invalid date format. please use the format month/day/year.")
                else:
                    print(expense_history[day])
            else:
                break
    elif choice == "5":
        while True:
            print("1. insert budget")
            print("2. main menu")
            next = input("next: ")
            if next == "1":
                budget = float(input("Enter your monthly budget: $"))
                day = input("what is the day of the budget? month/day/year: ")
                if len(day) != 8:
                    print("invalid date format. please use the format month/day/year.")
                    break
                else:
                    budget_history[day] = budget_history.get(day, 0) + budget
            else:
                break
    elif choice == "6":
        while True:
            print("Budget history:")
            print("1. view all budget history")
            print("2. view budget history by day, month and year")
            print("3. main menu")
            n = input("next: ")
            if n == "1":
                print(budget_history)
            elif n == "2":
                day = input("what is the day of the budget? month/day/year: ")
                if len(day) != 8:
                    print("invalid date format. please use the format month/day/year, or no budget entered for that day.")
                else:
                    print(budget_history[day])
            else:
                break
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
