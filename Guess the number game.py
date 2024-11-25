import random 

def guess_number(x):
     random_number = random.randint(1, x)
     guess = 0

     while guess != random_number:
          guess = int(input(f"Guess a number betweeen 1 and {x}: "))
          if guess < random_number: 
               print("Sorry, guess too low, try again!")
          elif guess > random_number:
               print("Sorry, guess too high, try again!")
          else: 
               print(f"Yay!, Congrats, you've guess {random_number} correctly!")

def computer_guess(x):
     low = 1
     high = x
     feedback = ''
     while feedback != 'c':
          if low != high: 
               guess = random.randint(low, high)
          else: guess = high
          feedback = input(f"Is {guess} too high(H) or too low(L) or the computer guessed correctly!(C)??: ").lower()
          if feedback == 'l':
               low = guess + 1
          elif feedback == 'h':
                    high = guess - 1
          else: 
                    print(f"Yay!, the computer guessed your number {guess} correctly!")


guess_number(10)

computer_guess(20)


               