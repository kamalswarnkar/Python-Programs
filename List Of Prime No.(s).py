prime_no = []


def prime_No(s, e):
    for x in range(s, e + 1):
        if x >= 0:
            if x == 0 or x == 1:
                pass
            elif x == 2:
                prime_no.append(x)
            else:
                l = []
                for i in range(2, x):
                    if x % i == 0:
                        l.append(i)

                if len(l) == 0:
                    prime_no.append(x)
                else:
                    pass
        else:
            print("Number should be positive")


a = int(input("From: "))
b = int(input("To: "))

prime_No(a, b)

print(prime_no)