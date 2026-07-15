# P1 — Easy
# String lo — sab numbers extract karo.
# "Age 21, marks 95, roll 42" → ['21', '95', '42']
import re

result = "Age 21, marks 95, roll 42"
number = re.findall(r"\d{2}",result)
print(number)

# P2 — Medium
# Email validator banao — valid/invalid batao.
# "test@gmail.com"  → Valid
# "test@"           → Invalid

def is_check_email(email):
    check = r"^[a-zA-Z0-9.!_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(check,email))
print(is_check_email("kalpeshbhure01@gmail.com"))
print(is_check_email("kalpesh@"))

# P3 — Medium
# Text lo — sab extra spaces hatao, multiple spaces ko ek karo.
# "Hello   World    Python" → "Hello World Python"

text = "Hello   World    Python"
result = re.sub(r"\s+"," ",text)
print(result)

# P4 — Hard
# Log file jaisa string lo — date, time, error level, message extract karo.
# "2024-01-15 10:30:45 ERROR Database connection failed"
# → date: 2024-01-15
# → time: 10:30:45
# → level: ERROR
# → message: Database connection failed

text = "2024-01-15 10:30:45 ERROR Database connection failed"
extract = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) ([a-zA-z]+) (.+)"

match = re.match(extract,text)

if match:
    print("date: ",match.group(1))
    print("time: ",match.group(2))
    print("level: ",match.group(3))
    print("message: ",match.group(4))
else:
    print("invalid log format")
