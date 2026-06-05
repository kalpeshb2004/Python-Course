def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-len(sub_string)):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1

    return count   

#     0123456
# A = bababcq = 7
# bab = 3
# A[0:3] == bab, count = 1
# A[1:4] == aba, count = 1
# A[2:5] == bab, count = 2
# A[3:6] == abc, count = 2
# A[4:7] == bcq, count = 2
#
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)