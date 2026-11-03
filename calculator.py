str1 = "good morning"
print(str1[2:5])

class employee:
    def __init__(self,employeeID , name):
        self.employeeID = employeeID
        self.name = name

    def show(self):
        print("employeeId : " , self.employeeID)
        print("name : " ,self.name)

e = employee(101,"kalpesh")
e.show()