Name = input("What's your name? ")
if len(Name) < 3:
    print("           Name must be at least 3 characters long ")
elif len(Name) > 50:
    print("           Name can be a maximum of 50 characters long")
else:
    print("           Name looks good!")

print("         It's a Weight Converter")

weight = int(input("Weight "))
unit = input("(L)lb or (K)kg ")
if unit == 'L' or unit == 'l':
    print(f"               You're {weight * 0.453592} Kgs")
elif unit == 'K' or unit == 'k':
    print(f"               You're {weight * 2.20462} Pounds")  
    









