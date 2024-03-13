# This program is a number guessing game where the user selects a
# range of integers, and has to guess the correct number, between the range,
# in x amount of attempts.


import random
import math

# Taking Inputs
lower = int(input("Enter lower bound: "))

# Taking Inputs
upper = int(input("Enter upper bound: "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the number!\n")

# Initializing the number of guesses.
count = 0

# Calculation of the minimum number of
# guesses depends on the range.
# formula for determing minimum number of guesses is
# log2(Upper bound – lower bound + 1)
while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking the guessed number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you guessed it in ",
              count, " attempt(s)!")
        # If guessed correctly, the loop will break
        break
    elif x > guess:
        print("Too low!")
    elif x < guess:
        print("Too high!")

# Output if guesses are more than required
if count > math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)



