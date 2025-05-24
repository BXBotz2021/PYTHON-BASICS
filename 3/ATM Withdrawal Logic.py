balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Withdrawal rejected: no balance")
elif withdraw % 100 != 0:
    print("Withdrawal rejected: amount must be multiple of 100")
else:
    balance -= withdraw
    print("Withdrawal successful. available balance:", balance)
