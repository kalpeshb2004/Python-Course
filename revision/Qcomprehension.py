# LIST COMPREHENSION — 5 Q
# Q1
# Numbers 1-50 — sirf wo numbers jo 3 se bhi divide ho aur 5 se bhi.
# → [15, 30, 45]

lst = [x for x in range(50) if x%3==0 and x%5==0]
print(lst)

# Q2
# Words list lo — sirf wo words jo vowel (a,e,i,o,u) se start ho.
# ["apple","mango","orange","kiwi"] → ["apple","orange"]

lst = ["apple","mango","orange","kiwi"]
vowels = "aeiou"
result = [x for x in lst if x[0].lower() in vowels]
print(result)

# Q3
# List of numbers lo — har number ka square nikalo sirf odd numbers ka.
# [1,2,3,4,5] → [1, 9, 25]

lst = [x*x for x in range(5+1) if x%2 != 0]
print(lst)

# Q4
# Sentence lo — har word ka pehla letter capital karo list comprehension se.
# "hello world bye" → ["Hello", "World", "Bye"]

line = "hello world bye"
lst = [x.capitalize() for x in line.split(" ")]
print(lst)

# Q5
# List of temperatures Celsius me — Fahrenheit me convert karo.
# formula = C * 9/5 + 32
# [0, 25, 100] → [32.0, 77.0, 212.0]

celcius = [0, 25, 100]
lst = [x * 9/5 + 32 for x in celcius]
print(lst)

# LIST — 2 CONDITIONS
# Q6
# Numbers 1-100 — sirf wo jo 5 se divide ho aur 50 se bade ho.
# → [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

lst = [x for x in range(101) if x%5==0 and x> 50]
print(lst)

# Q7
# Words list — sirf wo words jo 4 se zyada letters wale ho aur uppercase me ho.
# ["hi","HELLO","RAM","KALPESH"] → ["HELLO","KALPESH"]

words = ["hi","HELLO","RAM","KALPESH"]
lst = [x for x in words if x.upper() and len(x) > 4]
print(lst)

# DICT COMPREHENSION — 5 Q
# Q1
# Numbers list — har number aur uska cube dict me.
# [1,2,3,4] → {1:1, 2:8, 3:27, 4:64}

dct = {x:x**3 for x in range(1,5)}
print(dct)

# Q2
# 2 lists lo names aur marks — zip karke dict banao.
# ["Raj","Jay"] + [95,88] → {"Raj":95, "Jay":88}

key = ["Raj","Jay"]
value = [95,88]
dct = {k:v for k,v in zip(key,value)}
print(dct)

# Q3
# Dict lo — values double karo comprehension se.
# {"a":1, "b":2, "c":3} → {"a":2, "b":4, "c":6}

dct = {"a":1, "b":2, "c":3}
dct1 = {k:v*2 for k,v in dct.items()}
print(dct1)

# Q4
# Words list — sirf odd length wale words aur unki length dict me.
# ["hi","ram","kalpesh","jay"] → {"ram":3, "kalpesh":7}

word = ["hi","ram","kalpesh","jay"]
dct = {k:len(k) for k in word if len(k) % 2 != 0}
print(dct)

# Q5
# List of students (name, marks) — sirf passing (>=40) ka dict banao.
# [("Raj",95),("Jay",35)] → {"Raj":95}

lst = [("Raj",95),("Jay",35)]
dct = {name:marks for name,marks in lst if marks >=40}
print(dct)


# DICT — 2 CONDITIONS
# Q6
# Numbers 1-20 — sirf even numbers aur jo 3 se bhi divide ho — key:value = number:square.
# → {6:36, 12:144, 18:324}

dct = {num:num*num for num in range(1,20) if num%2==0 and num%3==0}
print(dct)

# Q7
# Words list — sirf wo words jo 4 se zyada letters wale ho aur 'a' contain karo — word:length dict.
# ["mango","kiwi","banana","apple"] → {"mango":5, "banana":6, "apple":5}

words = ["mango","kiwi","banana","apple"]
dct = {w:len(w) for w in words if len(w) >4 and "a" in w}
print(dct)

# TOTAL: 14 Q 💪
# Shuru kar! 🪨