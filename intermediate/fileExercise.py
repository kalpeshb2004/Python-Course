# def work_checker():
#     with open("practice.txt" ,"r") as f:
#      data = f.read()
#     if("learning" in  data):
#         print("found")
#     else:
#         print("not found")

# work_checker()

# def line_count():
#     data = True
#     count = 1
#     word = "larning"
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(count)
#                 return
#             count += 1
#     return -1

# print(line_count())


data = True
count = 1
with open("practice.txt","r") as f:
    data = f.read()
    lst = data.split(",")
    for val in lst:
        if(int(val) % 2 == 0):
            count
        else:
            count+=1
      
print(count)
            
        
        
    


