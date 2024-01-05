# A Perfect No. is no that is equal to the sum of its factors

n = int(input("Num: "))
s = 0
for i in range(1,n):
    if n % i == 0:
        s += i

if n == s:
    print(f"😊 Its a Perfect No. 😊")
else:
    print(f"😥 Its not a Perfect No. 😥")

