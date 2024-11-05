# FUNNCY GAMES
# guessing game

# FEATURES 
# *Generate random numbers
# *allow User input
# *user lives
# * award


# NOTES


import random
from random import randint


import random as r

# # GENERATED RANDOM NUMBERS(1,50)
# generated_random_number = r.randint(1,50)
# # # get user input
# user_input = int(input('enter your guess(1,50): '))
# # verify if user input correspond to generated number
# if generated_random_number == user_input:
#     print('you won')
# else:
#  print('you lose',generated_random_numer)





# # generate random numberrs(1,50)
# generated_random_numbers = r.randint(1,50)
# # inform user's of total lives
# print('you have 3 lives')
# set user live to 1
# user_lives = 1
# # determine if user has exhausted live
# while user_lives < 4:
#    #  get user input
#    user_input= int(input('enter your guess(1,50)'))
   # #  verify if user input correspond to generated numbers
   # if generated_random_numbers == user_input:
   #    print('you won')
   #    break
   # else:
   #    print('lose')
   #    # increment user lives
   #    user_lives = user_lives +1


# example2
# generate random numbers(1,50)
generated_random_numbers = r.randint(1,50)
# inform user's of total lives
print('you have 3 lives')
# set user live to 1
user_lives =1
# determine if user has exhausted live
while  user_lives < 4:
   # get use input
   user_input = int(input('enter your guess(1,50)'))
   # verify if user input correspond to generated numbers
   if generated_random_numbers == user_input:
    print('you won')
    break
   elif user_input>generated_random_numbers:
      print('guess too high,please try again')
   elif user_input <generated_random_numbers:
      print('guess low,please try again')
   else:
      print('you lose,please sorry')
   user_lives = user_lives + 1