num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("Even and divisible by 4")
    else:
        print("Even but not divisible by 4")
else:
    print("Odd number")
