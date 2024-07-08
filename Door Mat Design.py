char = ".|."
word = "WELCOME"
n, m = map(int, input().split())


for i in range(1, (n + 1) // 2):
    print((((2 * i) - 1) * char).center(m,'-'))

print(word.center(m, '-'))

for i in range((n - 1) // 2, 0, -1):
    print((((2 * i) - 1) * char).center(m,'-'))
        