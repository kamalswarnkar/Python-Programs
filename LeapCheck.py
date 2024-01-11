def leap_year(year):
    ly = []
    ny = []

    if year % 4 != 0:
        ny.append(year)
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                ly.append(year)
            else:
                ny.append(year)
        else:
            ly.append(year)

    if year in ly:
        print("✔️YUP✔️")
    else:
        print("❌NOPE❌")


year = int(input("Is it a Leap Year? >> "))
leap_year(year)
