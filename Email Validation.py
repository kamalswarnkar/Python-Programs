def fun(s):
    if(s.count('@') != 1 or s.count('.') != 1):
        return False
    
    idx_1 = s.index('@')
    idx_2 = s.index('.')

    if(idx_1 > idx_2):
        return False
    
    for char in s[:idx_1]:
        if(not(char.isalnum() or char in "-_")):
            return False
    
    for char in s[idx_1 + 1:idx_2]:
        if(not char.isalnum()):
            return False

    ext = s[idx_2 + 1:]
    if(not (1 <= len(ext) <= 3 and ext.isalpha())):
        return False
    
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
