# 7
# add Apple
# add Banana
# add Mango
# remove Banana
# print
# count

n = int(input())
data = []

for i in range(0,n):
    command = input().split(' ')
    if command[0] == "add":
        data.append(command[1])
    elif command[0] == "remove":
        data.remove(command[1])
    elif command[0] == "print":
        print(data)
    elif command[0] == "count":
        print(len(data))
    else:
        pass                