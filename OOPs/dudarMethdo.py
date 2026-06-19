# P1 — Easy
# Book class — title, pages. Implement:
# __str__ → "Book: title, Pages: pages"
# __repr__ → "Book('title', pages)"
# __gt__ → zyada pages wali book badi
# __eq__ → same pages → equal

# class book:
#     def __init__(self,title,page,):
#         self.title = title
#         self.page = page
    
#     def __str__(self):
#         return f'Book: {self.title}, Pages: {self.page}'

#     def __repr__(self):
#         return f'student: {self.title} , {self.page}'
    
#     def __gt__(self, other):
#         return self.page > other.page
    
#     def __eq__(self, other):
#         return self.page == other.page
    
# b1 = book("jungle book",277)
# print(b1)
# print(repr(b1))
# print(277 > 230)
# print(277 == 333)


# P2 — Medium
# Cart class — items (list of tuples (name, price)). Implement:
# __len__ → kitne items
# __getitem__ → index se item lo
# __contains__ → item name cart me hai?
# __str__ → sab items print karo
# add(name, price) → item add karo


class Cart:
    def __init__(self):
        self.name = []
        self.price = []

    def add(self, name, price):
        self.name.append(name)
        self.price.append(price)

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        return (self.name[index], self.price[index])

    def __contains__(self, item):
        return item in self.name

    def __str__(self):
        result = ""
        for i in range(len(self.name)):
            result += f"{self.name[i]} → ₹{self.price[i]}\n"
        return result


c1 = Cart()
c1.add("Jungle", 255)
c1.add("Ramayan", 5433)
c1.add("Gita", 221)

print(len(c1))          # → 3
print(c1[0])            # → ('Jungle', 255)
print("Gita" in c1)     # → True
print("Bible" in c1)    # → False
print(c1)               # → sab items

        
        

    
        