# Output Format
# Print the runner-up score.

# Sample Input 0
# 5
# 2 3 6 6 5

# Sample Output 0
# 5

n = int(input()) #no of input
arr = map(int,input().split()) #input


duplicates = list(set(arr)) #remove duplicates

sort = sorted(duplicates , reverse=True) #sorted in descending order

print(sort[1]) #print second position