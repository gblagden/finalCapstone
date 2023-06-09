# I started by writing "import math" at the top of the code, and I then introduce the program as per the instructions, with some creations of my own.


'''
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
'''


# I remember from a previous task that using a while loop prevents the user from having to run the program from the beginning if they type something incorrectly.
# I really wanted my program to work regardless of what the user typed, without crashing.  So I did some more research, and came across this article:

# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

# This article really helped with some of the more complicated parts of the code below.
# So I have implemented while loops for the remainder of the code to make sure that if the user types something incorrectly, they will be asked the same question again.

# Also, I wanted the user to be able to enter numbers with decimals as values for the interest rates, and I realised if I replaced "int" in front of the input functions with "float", this would allow them to supply floats for certain questions.

# I start by asking the user which calculation they would prefer, and store it in a variable called "calculation_choice".
# I then convert their answer to lowercase.


'''
while True:

    calculation_choice = input("Please enter either 'investment' or 'bond' from the choice above to proceed: ")
    print()
    calculation_choice = calculation_choice.lower()
'''

# I create an if/elif/else statement with lots of nested while loops to help run through the questions in the "investment" branch.


'''
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
'''

        
 # Once I have all the user's answers for the questions I needed to ask, I divide the interest rate they gave me by 100, as per the instructions.
 # I then use a nested if/elif/else statement to display the total amount the user receives after the respective interest is applied, utilising the formula from the instructions.


'''                
        inv_interest_rate = inv_interest_rate/100

        if interest == "simple":
            simple_total_return = money_to_deposit*(1 + inv_interest_rate*years_investing)
            print(f"After {years_investing} years, you will have accrued {simple_total_return} in total.")
            print()   
            break

        elif interest == "compound":
            compound_total_return = money_to_deposit * math.pow((1+inv_interest_rate),years_investing)
            print(f"After {years_investing} years, you will have accrued {compound_total_return} in total.")
            print()
            break
'''


# I repeat the above processes for the "bond" branch of questions.


'''
    elif calculation_choice == "bond":

        while True:
            try:
                house_value = int(input("How much is your property currently worth? "))
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
                bond_interest_rate = float(input("And what is the interest rate? "))
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
                months_repay = float(input("And how many months would you like to take to repay the bond? "))
                print()
            except ValueError:
                print()
                print("I'm sorry, that isn't a valid entry. Please try again.")
                print()
                continue
            else:
                break
'''


        # I divide the interest rate the user provided me with by 100, and divide this figure by 12 to get the monthly interest rate.
        # I then display the user's monthly repayment figure by using the formula provided in the instructions for the "bond" branch.


'''
        bond_interest_rate = bond_interest_rate/100
        monthly_interest_rate = bond_interest_rate/12
        monthly_repayment = (monthly_interest_rate * house_value)/(1 - (1 + monthly_interest_rate)**(-months_repay))
        print(f"Your montly repayments will be {monthly_repayment}.")
        print()
        break

    else:
        print("I'm sorry, that is an invalid entry. Please try again.")
        print()
'''




### SO THE CODE IN FULL APPEARS LIKE THIS:  ###





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