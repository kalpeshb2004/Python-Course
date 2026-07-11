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



# Q2
# 2 lists lo names aur marks — zip karke dict banao.
# ["Raj","Jay"] + [95,88] → {"Raj":95, "Jay":88}

# Q3
# Dict lo — values double karo comprehension se.
# {"a":1, "b":2, "c":3} → {"a":2, "b":4, "c":6}

# Q4
# Words list — sirf odd length wale words aur unki length dict me.
# ["hi","ram","kalpesh","jay"] → {"ram":3, "kalpesh":7}

# Q5
# List of students (name, marks) — sirf passing (>=40) ka dict banao.
# [("Raj",95),("Jay",35)] → {"Raj":95}

# DICT — 2 CONDITIONS
# Q6
# Numbers 1-20 — sirf even numbers aur jo 3 se bhi divide ho — key:value = number:square.
# → {6:36, 12:144, 18:324}

# Q7
# Words list — sirf wo words jo 4 se zyada letters wale ho aur 'a' contain karo — word:length dict.
# ["mango","kiwi","banana","apple"] → {"mango":5, "banana":6, "apple":5}

# TOTAL: 14 Q 💪
# Shuru kar! 🪨