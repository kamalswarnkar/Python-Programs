'''Armstrong No. is a no. equal to the sum of its digits
raised to the power equal to the no of digits'''

n = input("Num: ")
N = int(n)
l = []
k = len(n)
S = 0
for i in n:
    a = int(i)
    l.append(a)
    b = a ** k
    S += b
if N == S:
    print(f"😊 Its an Armstrong No. 😊")
else:
    print(f"😥 Its not an Armstrong No. 😥")