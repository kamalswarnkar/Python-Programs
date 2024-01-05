x = int(input("num1: "))
y = int(input("num2: "))

l1 = []
l2 = []

for i in range(1,x+1):
    if x % i ==0:
        a = i
        l1.append(a)
for j in range(1,y+1):
    if y % j == 0:
        b = j
        l2.append(b)


l3 = list(filter(lambda k : k in l1,l2))

r = max(l3)
print("GCD:",r)