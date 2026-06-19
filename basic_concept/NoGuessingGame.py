# number guessing game ← easiest, fun bhi
# Q sawala puchegs 1 to n no choose karo jo tum ghuess karana chaho

# Q level choose karo easy = 10 attempt ,medium = 7 hard = 4

# Q guess karo : 

# batayega no too high he ya too low

# Q guess karo : 

# guess kiya to msg aayega success nahi to 

# jb tak attempt khatam nahi hote tab tak game chalega aur 

# attempt khatam then 

# msg aayega you loose
import random

num_range = int(input("Enter a range that you gonna guess no in between: "))
guess_level = input("Enter a level easy/medium/hard: ")

if guess_level == "easy":
    n = 10
    print(f"You choose easy level so you have {n} attempt.")
elif guess_level == "medium":
    n = 7
    print(f"You choose medium level so you have {n} attempt.")
elif guess_level == "hard":
    n = 3
    print(f"You choose hard level so you have {n} attempt.")
else:
    print("choose level easy/medium/hard not anything")
    exit()

random_num = random.randint(1, num_range)


for i in range(n,0,-1):
    print(f'You have {i} attempt')
    guess = int(input("Guess a number: "))
    if  guess > random_num:
        print("Your guess is too high")
    elif guess < random_num:
        print("Your guess is too low")
    else:
        print("You have guessed a right no. Congrats!")
        break
else:
    print("You lost the game. Better luck next time!")


    


