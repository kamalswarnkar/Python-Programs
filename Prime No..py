x = int(input("num: "))

if x >= 0:
    if x == 0 or x == 1:
        print("Its Neither a Prime No. NOR Composite No.")
    elif x == 2:
        print("Its a Prime No.")
    else:
        l = []
        for i in range(2, x):
            if x % i == 0:
                l.append(i)

        if len(l) == 0:
            print("Its a Prime No.")
        else:
            print("Its a Composite No.")
else:
    print("Number should be positive")
