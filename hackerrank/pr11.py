n = int(input())
data = []

for i in range(0,n):
    command = input().split(' ') #it will take command (insert 30) (print) (add 50)
    if command[0] == "add":
        data.append(int(command[1]))
    elif command[0] == "print":
        print(data)
    elif command[0] == "average":
        average = sum(data) / len(data)
        print(round(average,2))      
    else:
        pass
