lst = ["hello", "ram", 10, 20, 30, 40, 50, 20]

# print list
print(lst)

# first 3 elements
print(lst[:3])

# append
lst.append("ram")
print(lst)

# extend
lst.extend(["jay", "shree", "ram"])
print(lst)

# insert
lst.insert(3, "hanuman")
print(lst)

# remove
lst.remove(20)
print(lst)

# pop
lst.pop(5)
print(lst)

# index
print(lst.index("ram"))

# count
print(lst.count(20))

# reverse
lst.reverse()
print(lst)

# clear (keep this last)
lst.clear()
print(lst)