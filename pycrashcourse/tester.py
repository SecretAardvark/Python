

print("How many years will you be saving? ")
years= int(input('Enter years: '))

print('How much money is currently in the account? ')
principal = float(input("Enter current amount: "))

print('How much money do you plan on investing monthly?')
monthly_invest= float(input("Enter amount: "))

print("What is the yearly interest? ")
interest = float(input("Enter interest in decimal numbers (10%= .1): "))



def compound(principal, interest, monthly_invest, years):
    monthly_invest = monthly_invest * 12 
    final_amount = 0 
    for i in range(0, years):
        if final_amount == 0:
            final_amount = principal
        final_amount = (final_amount + monthly_invest) * (1 + interest)
        return final_amount

    

compound(100, .078, 100, 20)