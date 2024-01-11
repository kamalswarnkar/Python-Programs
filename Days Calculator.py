while True:
    print("Date Format = DDMMYYYY")
    dob = input("Starting From: ")
    if len(dob) != 8:
        print("❌ ERROR!! ❌ ,D.O.B - Date Format is INVALID")
    else:
        td = input("To: ")
        if len(td) != 8:
            print("❌ ERROR!! ❌ ,Today's Date - Date Format is INVALID")
        else:
            x = int(dob[0] + dob[1])
            y = int(dob[2] + dob[3])
            z = int(dob[4] + dob[5] + dob[6] + dob[7])

            x1 = int(td[0] + td[1])
            y1 = int(td[2] + td[3])
            z1 = int(td[4] + td[5] + td[6] + td[7])

            if y > 12 and y1 > 12:
                print("❌ ERROR!! ❌ ,Given Month is INVALID")
            else:
                ny = []  # listing no. of normal years
                ly = []  # listing no. of leap years

                dd = 0  # no. of days in initial and last month of initial and last year respectively
                md = 0  # no. of days fixed in months between initial and last month of initial and last year respectively
                yd = 0  # no. of days fixed in years between initial and last year
                td = 0  # total no. of days

                ddi = 0  # no. of days in initial month of initial year
                ddf = 0  # no. of days in last month of last year

                dimny = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # listing no. of days in months of normal year
                dimly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # listing no. of days in months of leap year

                ny1 = ny[:]
                ly1 = ly[:]

                if z < z1:
                    for i in range(z + 1, z1):
                        if i % 4 != 0:
                            ny.append(i)
                        else:
                            if i % 100 == 0:
                                if i % 400 == 0:
                                    ly.append(i)
                                else:
                                    ny.append(i)
                            else:
                                ly.append(i)

                    yd += (len(ny) * 365) + (len(ly) * 366)
                    # checking whether the initial and final year falls in leap year or not
                    if z % 4 != 0:
                        ny1.append(z)
                    else:
                        if z % 100 == 0:
                            if z % 400 == 0:
                                ly1.append(z)
                            else:
                                ny1.append(z)
                        else:
                            ly1.append(z)
                    if z1 % 4 != 0:
                        ny1.append(z1)
                    else:
                        if z1 % 100 == 0:
                            if z1 % 400 == 0:
                                ly1.append(z1)
                            else:
                                ny1.append(z1)
                        else:
                            ly1.append(z1)

                    if z in ny1 and z1 in ny1:
                        for i in range(y + 1, 13):
                            ddi += dimny[i - 1]
                        for i in range(1, y1):
                            ddf += dimny[i - 1]
                        dd += dimny[y - 1] - x + x1 + 1
                    elif z in ny1 and z1 in ly1:
                        for i in range(y + 1, 13):
                            ddi += dimny[i - 1]
                        for i in range(1, y1):
                            ddf += dimly[i - 1]
                        dd += dimny[y - 1] - x + x1 + 1
                    elif z in ly1 and z1 in ny1:
                        for i in range(y + 1, 13):
                            ddi += dimly[i - 1]
                        for i in range(1, y1):
                            ddf += dimny[i - 1]
                        dd += dimly[y - 1] - x + x1 + 1
                    elif z in ly1 and z1 in ly1:
                        for i in range(y + 1, 13):
                            ddi += dimly[i - 1]
                        for i in range(1, y1):
                            ddf += dimly[i - 1]
                        dd += dimly[y - 1] - x + x1 + 1
                    md += ddi + ddf

                    td += yd + md + dd
                    print("Total No. of Days:", td)
                elif z == z1:
                    # checking whether the particular year is leap year or not
                    if z % 4 != 0:
                        ny1.append(z)
                    else:
                        if z % 100 == 0:
                            if z % 400 == 0:
                                ly1.append(z)
                            else:
                                ny1.append(z)
                        else:
                            ly1.append(z)

                    if y < y1:
                        if z in ny1:
                            for i in range(y + 1, y1):
                                ddi += dimny[i - 1]
                            dd += dimny[y - 1] - x + x1 + 1
                        elif z in ly1:
                            for i in range(y + 1, y1):
                                ddi += dimly[i - 1]
                            dd += dimly[y - 1] - x + x1 + 1
                    elif y == y1:
                        dd += x1 + 1 - x
                    elif y > y1:
                        print("❌ ERROR!! ❌ ,Given Data is INVALID")
                        yd = 0
                        md = 0
                        dd = 0
                    md += ddi

                    td += yd + md + dd
                    print("Total No. of Days:", td)
                else:
                    print("❌ ERROR!! ❌ ,Given Year is INVALID")

    print("-----------------------------------------------------------------------------------------------------------")
