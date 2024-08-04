def jos(n, k):
    if(n <= 0):
        return
    if(n == 1):
        return 0
    
    return (jos(n - 1, k) + k) % n

n, k = map(int, input().split())
print(jos(n, k))