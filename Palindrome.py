x = input("num/word: ")
r = x.replace(" ","")
s = r.upper()

s_new = s[::-1]

if s == s_new:
    print(f"😊 Its a Palindrome 😊")
else:
    print(f"😥 Its not a Palindrome 😥")