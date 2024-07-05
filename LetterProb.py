from itertools import combinations as com

n = int(input())

l = [input().strip() for _ in range(n)]

k = int(input())


ss = com(l, k)

count = 0
total = 0
for i in ss:
    total += 1
    i = list(i)

    for j in range(len(i)):
        if(i[j] == 'a'):
            count += 1 
            break 


r = count / total

print(f"{r:.3f}")