# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.21 belongs to Tina. The second lowest grade of 37.2 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


student = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append([name,score])

grades = sorted(set(s[1] for s in student))
second = grades[1]
names = sorted(s[0] for s in student if s[1] == second)

for name in names:
    print(name)
