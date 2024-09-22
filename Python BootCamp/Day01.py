"""
Question:

Imagine a fun game where you're challenged to guess a secret number. The computer selects a number between 1 and 100, and your task is to figure it out. With each guess, you'll receive hints to guide you.

What You’ll Build:

The Secret Number:
The game begins with the computer randomly selecting a number between 1 and 100. This is the secret number you'll be trying to guess.

Making Guesses:
You'll be prompted to guess a number between 1 and 100. If your input is outside that range or not a number, the game will remind you to try again.

Hints and Feedback:
If your guess is too low: "Too low! Try again."
If your guess is too high: "Too high! Try again."
If you guess correctly, you'll receive a congratulatory message along with the number of attempts.

Keep Guessing:
The game continues until you guess the correct number, so take your time and think carefully.

Ending the Game:
Once you've guessed the number, the game will end and let you know how many attempts it took.

Fun Extras:
To make it even better, handle any mix-ups in input (like letters instead of numbers) gracefully so you can focus on having fun.
"""

import random

def makevalid(num):
    new_num = ''
    for i in num:
        if(i.isdigit()):
            new_num += i
    if(new_num != ''):
        return int(new_num)
    else:
        return 0

print("LISTEN: If your guess doesn't include any number in it, we will consider it 0")

secret_no = int(random.random() * 100)
count = 0

num = input("Guess: ")
num = makevalid(num)

while(num != secret_no):
    count += 1
    print("OOPS!! Wrong Guess")
    if(num < secret_no):
        print("TRY AGAIN!, Your guess is LOW!")
    else:
        print("TRY AGAIN!, Your guess is HIGH!")
    num = input("Guess Again: ")
    num = makevalid(num)

print("YAY!!, You got it, CONRATS :)")
print(f"Well Done, You took {count + 1} attempts to reach here :)")

