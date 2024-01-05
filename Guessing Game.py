secret_number = 7
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input("Guess : "))
    guess_count += 1    # we put an condition of guessing at most 3 times with line 4 and line 6
    if guess == secret_number:
        print("😀🎉😀You Won!!😀🎉😀")
        break
else:
    print("Sorry!!😔 You Failed")
