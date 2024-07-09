import string as st

size = int(input())
width = (4 * size) - 3

letters = st.ascii_lowercase[0:size]

#print(letters)

if size == 1:
    print('a')
else:
    for i in range(size):
        lft_prt = '-'.join(letters[::-1][:i+1])
        rgt_prt = '-'.join(letters[::-1][:i][::-1])
        line = lft_prt + "-" + rgt_prt
        line = line.center(width,'-')

        print(line)

    for i in range(size - 1):
        lft_prt = '-'.join(letters[::-1][:size - i - 1])
        rgt_prt = '-'.join(letters[::-1][:size - i - 2][::-1])
        line = lft_prt + "-" + rgt_prt
        line = line.center(width,'-')

        print(line)