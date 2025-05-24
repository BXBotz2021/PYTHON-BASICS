num = int(input("Enter a number (1–10): "))

words = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
}

if num in words:
    print(words[num])
else:
    print("this number is not available in my diictionary")
