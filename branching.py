import sys
from functions import add_numbers

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])
sum = add_numbers(first_number, second_number)

def branch(sum=0):
    if sum <= 0:
        print("You have chosen the path of destitution.")
    elif sum > 100: 
        print("You have chosen the path of excess.")
    else:
        print("You have chosen the path of plenty.")

branch(sum)
