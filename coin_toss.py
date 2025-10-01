# FILE NAME - coin_toss.py

# NAME: Makiko Michelle Yasumi
# DATE: October 1, 2025
# BRIEF DESCRIPTION: This program randomly returns heads or tails.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!
import random

def main():
    cointoss()

def cointoss():
    print("=" * 5 + " Coin Flipper " + "=" * 5)
    number = random.randint(1,100)
    if number in range(51,101):
        print("Tails")
    else:
        print("Heads")

main()





########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
Remembering randint() function. I somehow managed to memorize it as randomint().

'''
