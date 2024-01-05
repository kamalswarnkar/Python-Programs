n = int(input("No. of Rows: "))
v = '* '
s = " "
for i in range(1, n+1):
    k = n - i
    print(k*s, v*i, k*s)
