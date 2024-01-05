while 1 > 0:
    x = int(input("Enter No. of sec(s): "))
    H = x // 3600
    h = x / 3600
    m = (h - H)*60
    m1 = m // 1
    M = int(m1)
    s = (m - m1) * 60
    S = int(s)
    print("Time(HH:MM:SS):", H, ":", M, ":", S)
    print("-----------------------------")
