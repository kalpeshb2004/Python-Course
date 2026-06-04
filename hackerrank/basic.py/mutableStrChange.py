def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:] #

# 5 tak character alag hua aur hamara char add hua
# and then same 5 se chalu hua to hamara char insert hua replace nahi
# ex = abracadabra  / without +1
# 5 tak count hua abrac
# add hua k
# 5 se chalu hua adabra 
# result aaya =abrackadabra

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

