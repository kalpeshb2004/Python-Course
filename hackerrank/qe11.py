n = int(input())
data = []



for i in range(0,n):
    command = input().split(' ') #it will take input like (insert 0 5) acc there index value
    if command[0] == "insert":
        data.insert(int(command[1]),int(command[2]))
    elif command[0] == "print":
        print(data)
    elif command[0] == "remove":
        data.remove(int(command[1]))
    elif command[0] == "append":
        data.append(int(command[1]))
    elif command[0] == "sort":
        data.sort()
    elif command[0] == "pop":
        data.pop()
    elif command[0] == "reverse":
        data.reverse()
    else:
        pass                            
