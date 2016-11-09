# List Question (Chapter 3):
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to
# be a console input in a comma-separated form.

param = input("Please enter X, Y to generate 2-dimensional array?")
print(param)
numbers = param.split(',')
if (len(numbers) == 2):
    x = int(numbers[0])
    print(x)
    y = int(numbers[1])
    print(y)
    output = []
    for i in range(0, x):
        sublist = []
        for j in range(0, y):
            sublist.append(i * j)
        output.append(sublist)
    print(output)
else:
    print("Two input values required!")
