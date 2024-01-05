m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
P_D = []
S_D = []
for i in m:
    a = m.index(i)
    for j in i:
        b = i.index(j)

        if a == b:
            c = j
            P_D.append(c)
        if a + b == 2:
            d = j
            S_D.append(d)

print("Primary/Principle Diagonal:", P_D)
print("Secondary Diagonal:", S_D)
