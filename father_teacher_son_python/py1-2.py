# 猜字游戏

import random

secret = random.randint(1,99)
guess = 0
tries = 0
print("AHOY! I'm the bread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99. I'll give your 6 tries.")

while guess != secret and tries < 6:
    guess = int(input("What's yer guess? "))
    if guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")
    tries+=1

if guess == secret:
    print("Acast! Ye got it! Found my secret, ye did! secret is ",secret)
else:
    print("not more guesses! Better luck to you, secret is ",secret)