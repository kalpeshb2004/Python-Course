# lexicographic order problem
# Constraints

# Print the list in lexicographic increasing order.

# Sample Input 0
# 1
# 1
# 1
# 2

# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
result = [
    [a ,b, c]
    for a in range(x+1)
    for b in range(y+1)
    for c in range(z+1)
    if a+b+c != n
]

print(result)