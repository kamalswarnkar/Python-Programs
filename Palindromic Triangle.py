while True:
    n = int(input("Size (int): "))
    l = []
    if n < 10:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                l.append(j)
            l1 = l[-2::-1]
            l2 = l + l1
            for k in l2:
                print(k, end='')
            l.clear()
            print("")
    else:
        print("❌ ERROR!! ❌")
        print("🙏🏻 Size should be less than 10 🙏🏻")
    print("-----------------------------------------------------------------------------------------------------------")
