def count_substring(string, sub_string):
    l_s = len(string)
    l_ss = len(sub_string)
    count = 0
    for i in range(l_s):
        if(sub_string == string[i:i + l_ss]):
            count += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)