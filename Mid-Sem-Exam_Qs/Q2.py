# 02. A list contains rupee denominations like 500, 200, 100, 50, 20, 10, 5, 2 and 1. Accept amount from the user and calculate minimum number of notes required for disbursement from ATM.

def atm(amount):
    denominations = [500,200,100,50,20,10,5,2,1]
    i = 0
    while amount:
        n = amount//denominations[i]
        if n:
            print(n," note/coin(s) of ",denominations[i])
        amount-=n*denominations[i]
        i+=1

atm(1254)            