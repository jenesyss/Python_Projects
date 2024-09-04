# dice roller

import random

repeat = True
print("Roll a d6?")
answer = input("Yes or No? ")
if answer == "Yes":
        while repeat:
            print("You rolled:")
            print(random.randrange(1,6))
            roll_again = input("Would you like to roll again? ")
            repeat = "Yes"
            if roll_again == "No":
                 exit(0)
            
            
else:
    answer == "No"
    exit(0)