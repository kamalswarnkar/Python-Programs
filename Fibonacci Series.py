print("Type the no. upto which you want the Fibonacci Series")
n = int(input("Num: "))
a = 0
b = 1
l = [0,1]
for i in range(n+1):
    c = a + b
    l.append(c)
    a = b
    b = c
print("Fibonacci Series:", l)
