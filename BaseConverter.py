def num_sys(n):
    
    width = len(bin(n)) - 2  # taking width of the largest number provided by user to later give appropriate and uniform space between all the numbers

    print("Num".rjust(width), "Oct".rjust(width), "Hex".rjust(width), "Bin".rjust(width))

    for i in range(1, n + 1):
        b = bin(i)
        o = oct(i)
        h = hex(i).upper()

        b = b[2:]
        o = o[2:]
        h = h[2:]

        print(str(i).rjust(width), o.rjust(width), h.rjust(width), b.rjust(width)) # rjust ---> to adjust all the individual number to right side

        #     ^int doesn't have rjust fn 


n = int(input())
num_sys(n)
