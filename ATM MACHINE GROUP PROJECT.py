import sys
name="USER"
Greetings="Hello "+"Mr/Mrs. "+name
print("------------------------------")
print("WELCOME TO XYZ ATM MACHINE")
print("------------------------------")
print(Greetings)
print("------------------------------")


cash=20000

while True:
        action = input("What would you like to do? (1.Withdraw/2.Deposit/3.Check Balance/4.Exit): ")
        print("------------------------------")
        if action.lower() == "1":
            while True:
                try:
                    withdraw_amount = int(input("How much would you like to withdraw? "))

                    if cash-withdraw_amount < 3000 :
                        print("Minimum Bank balance is Rs.3000 , Low Balance")
                        print("-----------------------------")

                    if withdraw_amount <= cash and cash-withdraw_amount > 3000:
                        cash -= withdraw_amount
                        print("You have withdrawn " + str(withdraw_amount) + ". Your new balance is " + str(cash) + ".")
                        print("-----------------------------")
                        break
                    else:
                        print("You do not have enough money to withdraw that amount.")
                        print("-----------------------------")
                except ValueError:
                    print("Invalid input.")
        elif action.lower() == "2":
            while True:
                try:
                    deposit_amount = int(input("How much would you like to deposit? "))
                    cash += deposit_amount
                    print("You have deposited " + str(deposit_amount) + ". Your new balance is " + str(cash) + ".")
                    break
                except ValueError:
                    print("Invalid input.")                    
        elif action.lower() == "3":
            while True:
                try:
                    print("Your Current Balance is:",str(cash) + ".")
                    print("-----------------------------")
                    break
                except ValueError:
                    print("Invalid input.")                    
        elif action.lower() == "4":
            sys.exit()
else:
    print("Invalid input.")