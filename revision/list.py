# LIST
# Q1 — Easy
# List lo — duplicates hatao, sort karo, reverse karo. Print karo har step pe.


lst = [1,2,3,21,3,1,32,1,1,34,2,32,322,33,2,1,32,2]
new_lst = []
for lsts in lst:
    if lsts not in new_lst:
        new_lst.append(lsts)

new_lst.sort()
new_lst.reverse()
print(new_lst)


# Q2 — Medium
# 2 lists lo — common elements nikalo bina set use kiye. Sirf list methods use karo.

lst = [1,2,3,21,3,1,32,1,1,34,2,32,322,33,2,1,32,2]
lst2 = [2,1,3,4,1,5,6,7,8,2,1,3,4,68,32]

comman = []
for i in lst:
    if i in lst2:
        comman.append(i)
print(comman)
