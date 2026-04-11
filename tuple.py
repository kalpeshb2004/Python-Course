#immutable
tpl1 = ("kalpesh" , "jayesh" , 20 ,20,30,405,"hello")

tpl2 = (10,20,30,40,50)

print(type(tpl1))
print(tpl1)

#funtion
# count
count = tpl1.count(20)
print(count)

#index
index = tpl1.index("kalpesh")
print(index)

# concatnation
concate = tpl1 + tpl2
print(concate)

#addition ot two tpl with lambda function 
t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(t1)
print(t2)

new_tpl = tuple(map(lambda x ,y : x+y,t1,t2))
print("addition :" ,new_tpl)