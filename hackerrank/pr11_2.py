# 8
# append 5
# append 10
# append 15
# sum
# max
# min
# print
# length

n = int(input())
data = []

for i in range(0,n):
    command = input().split(' ')
    if command[0] == "append":
        data.append(int(command[1]))
    elif command[0] == "sum":
        print(sum(data))
    elif command[0] == "max":
        print(max(data))
    elif command[0] == "min":
        print(min(data))
    elif command[0] == "print":
        print(data)
    elif command[0] == "length":
        print(len(data))
    else:
        pass                   

