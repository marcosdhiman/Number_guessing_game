
import random 

print("Number guessing game") 

print('Hello! What is your name?')
myName = input()


number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')



chances = 0

print("Guess a number (between 1 and 20):") 


while chances < 3: 

    guess = int(input()) 

    if guess == number: 

        print("Congratulation YOU WON!!!") 
        break

    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 

    else: 
        print("Your guess was too high: Guess a number lower than", guess) 

    chances += 1

if not chances < 3: 
    print("YOU LOSE!!! The number is", number) 
