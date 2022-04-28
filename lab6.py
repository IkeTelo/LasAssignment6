# Laymens Terms!!!
"""
To start, we will generate a random interger between 1 and 20; then
based on the result of the random number, we check to see if it falls under
a certin range
if the number is > 15, then the result will = "Cherries"
otherwise if the number is > 10, the result will = "Orange"
otherwise if the number is > 5, the result will = "Plum"
otherwise if the number is > 2, the result will = "Melon"
otherwise if the number is > 1, the result will = "Bell"
if the number is not any of the ubove, then the result will = "Bar"

we iterate over using a loop three times and print the results to the user.
An example "Plum Cherries Melon"

"""
# Psudocode !!!

"""
import random
num = generate random number between 1 and 20

if the number is > 15,
    then the result will = "Cherries"
otherwise if num is > 10,
    the result will = "Orange"
otherwise if num is > 5,
    the result will = "Plum"
otherwise if num is > 2,
    the result will = "Melon"
otherwise if num is > 1,
    the result will = "Bell"
otherwise
    the result will be "Bar"

loop three times
    print the output (fruit) to the user

"""

# Code!!!!

import random
def main():
    for i in range(0, 3):
        spin()
def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if(rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "Orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Melon"
    elif(rand_num > 2):
        output = "Bell"
    else:
        output = "Bar"
    print(output, end=" ")
main()