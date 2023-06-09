


import math

print("Hello.  Welcome to Blagden Financials!")
print()
print("To start, please select which calculation you require: ")
print()
print(" INVESTMENT - to calculate the amount of interest you'll earn on your investment.")
print()
print(" OR")
print()
print(" BOND - to calculate the amount you'll have to pay on a home loan.")
print()


while True:

    calculation_choice = input("Please enter either 'investment' or 'bond' from the choice above to proceed: ")
    print()
    calculation_choice = calculation_choice.lower()


    if calculation_choice == "investment":

        while True:
            try:
                money_to_deposit = float(input("Please enter the amount of money you wish to deposit: "))
                print()
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break

        while True:
            try:
                inv_interest_rate = float(input("Now please enter the interest rate that you have chosen: "))
                print()
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break

        while True:
            try:
                years_investing = int(input("And how many years would you like to invest this money for? "))
                print()
                if years_investing > 40:
                    print("I'm sorry, we only allow our clients to invest for a maximum of 40 years. Please try again.")
                    print()
                    continue
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break

        while True:
            try:
                interest = input("And would you like to invest your money with 'simple' or 'compound' interest? ")
                print()
                if interest == "simple" or interest == "compound":
                    break
                else:
                    print()
                    print("I'm sorry, that isn't a valid entry. Please try again, and make sure to use only lowercase letters!")
                    print()
                    continue
            except:
                continue


        inv_interest_rate = inv_interest_rate/100


        if interest == "simple":
            simple_total_return = money_to_deposit * \
                (1 + inv_interest_rate*years_investing)
            print(
                f"After {years_investing} years, you will have accrued {simple_total_return} in total.")
            print()
            break

        elif interest == "compound":
            compound_total_return = money_to_deposit * \
                math.pow((1+inv_interest_rate), years_investing)
            print(
                f"After {years_investing} years, you will have accrued {compound_total_return} in total.")
            print()
            break

    elif calculation_choice == "bond":

        while True:
            try:
                house_value = int(
                    input("How much is your property currently worth? "))
                print()
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break

        while True:
            try:
                bond_interest_rate = float(
                    input("And what is the interest rate? "))
                print()
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break

        while True:
            try:
                months_repay = float(
                    input("And how many months would you like to take to repay the bond? "))
                print()
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break

        bond_interest_rate = bond_interest_rate/100
        monthly_interest_rate = bond_interest_rate/12
        monthly_repayment = (monthly_interest_rate * house_value) / \
            (1 - (1 + monthly_interest_rate)**(-months_repay))
        print(f"Your montly repayments will be {monthly_repayment}.")
        print()
        break

    else:
        print("I'm sorry, that is an invalid entry. Please try again.")
        print()