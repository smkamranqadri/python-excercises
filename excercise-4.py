# Question 4 (Chapter 5):

# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied
# to the program:hello world! 123Then,
# the output should be:LETTERS 10DIGITS 3

letter = 0
digit = 0

param = input("Please enter sequence to calculate Letters and Digists?")

for i, c in enumerate(param):
    if(str.isalpha(c)):
        letter = letter + 1
    if(str.isdigit(c)):
        digit = digit + 1

print('Letter: ' + str(letter) + ', Digit: ' + str(digit))