# SET
# Q1 — Easy
# 2 lists lo — dono me common elements nikalo set se. Sirf ek line me karo.

lst1 = [3,2,1,3,4,5,6,4,3,4,56]
lst2 = [2,2,3,2,1,3,4,3,21,2,1]

new = set(lst1).intersection(set(lst2))
print(new)

# Q2 — Medium
# List of words lo — duplicate words set se hatao, unique words count karo, sabse chota word nikalo.

lst = ["kalpesh","dharmraj","bhure","bhure","ram"]
print(list(set(lst)))
print(len(list(set(lst))))
small_word = min(lst,key=lambda x: len(x))
print(small_word)