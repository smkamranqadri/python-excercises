
# Question (Chapter 3 Lists):
# Use a list comprehension to square each odd number in a list. The list is input
# by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.

param = input("Please input the list by a sequence of comma-separated numbers? ")

numbers = str(param).split(',')

for i in range(0, len(numbers)):
    if i % 2:
        print(i, end=", ")

print('\r')
