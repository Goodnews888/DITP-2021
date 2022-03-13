#Learning about If_Else statements

bank_charge = 10
account_balance = 100
bank_bonus = 5

if account_balance < 0:
    account_balance = account_balance - bank_charge
else:
    account_balance = account_balance + bank_bonus

print("The account balance is " + str(account_balance))

print()
print("Account balance is positive")

bank_charge = 10
account_balance =-20
bank_bonus = 5

if account_balance < 0:
    account_balance = account_balance - bank_charge
else:
    account_balance = account_balance + bank_bonus

print("The account balance is" + str(account_balance))
    
