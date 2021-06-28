import random
print("--------TEST YOUR LUCK WITH DICE GAME------\n")
print("roll the both dice")
dice_possible_options = (1,2,3,4,5,6)
possible_sum = (2,3,4,5,6,7,8,9,10,11,12)
roll_the_dice_1 = random.choice(dice_possible_options)
print(roll_the_dice_1)
roll_the_dice_2 = random.choice(dice_possible_options)
print(roll_the_dice_2)
sum_we_got = roll_the_dice_1 + roll_the_dice_2
print("the sum_we_got is : ")
print(sum_we_got)
random_sum = random.choice(possible_sum)
print("the random_sum is :")
print(sum)
if (total == sum):
   print("you are so luck!")
   print("whatever you wish for you will get it")
else:
        print("better luck next time")