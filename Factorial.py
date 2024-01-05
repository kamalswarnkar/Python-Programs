n = int(input("Num: "))
x = 1
if n > 0:
    for k in range(0, n):
        x *= (n - k)
    r = x
elif n == 0:
    r = 1
else:
    r = 'Num is not valid'
print("Num! =", r)