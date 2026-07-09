# Input
#   ↓
# 5 rules check
#   ↓
# Score calculate
#   ↓
# Weak/Medium/Strong
#   ↓
# Feedback print
'''
length should be gt=8 lt=15
atleast ek upper case 
atlest ek lower case
ek number
ek cpacial char
'''

pwd = input("Enter your password: ")

score = 0
feedback = []

def strengthChecker():
    global score,feedback
    if 8 <= len(pwd) <= 15:
     score += 1
    else:
        feedback.append("password length should be 8-15")

    if any(c.isupper() for c in pwd):
        score += 1
    else:
        feedback.append("atleast one capital letter")

    if any(c.islower() for c in pwd):
        score += 1
    else:
        feedback.append("atleast one small letter")

    if any(c.isdigit() for c in pwd):
        score +=1
    else:
        feedback.append("atleast one number")

    if any(c in "!@#$%^&*" for c in pwd):
        score +=1
    else:
        feedback.append("atleast one special character")

#result
def scoreCalculate():
    if score == 5:
     print("Password accpetd \nstrong password")

    elif score >= 3:
        print("medium pasword")
    else:
        print("easy pasword")

def result():
    for f in feedback:
        print("->",f)

strengthChecker()
scoreCalculate()
result()