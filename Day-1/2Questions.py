# 1.	Declare two variables a and b, assign integer values to them, and print their sum. 
var1 = 3
var2 = 4
print(var1+var2)
# 2.	Create a variable name and assign your name to it. Print a greeting message using your name. 
# o	Expected Output: Greeting message with your name, e.g., "Hello, John!"
name = "Srinadh Chintakindi"
print("Hello,{}".format(name))
print(f"Hello,{name}")
# 3.	Define a variable pi and assign the value of π (pi) to it. Print the value of pi. 
# o	Expected Output: The value of π (pi), e.g., 3.14159.
pi = 3.14159; print(pi)
# 4.	Define a variable is_raining and ask the user to input either "True" or "False" (as a string). Convert the input to a boolean and print its type. 
# o	Expected Input: "True" or "False"
# o	Expected Output: The data type of the converted boolean.
def is_raining():
    is_raining = input("Enter is True or False:\n")
    print(type(eval(is_raining)))

# 5.	Create a string variable sentence containing any sentence of your choice. Ask the user to input a number, convert it to an integer, and print the sentence repeated that number of times. 
# o	Expected Input: A number (e.g., "3")
# o	Expected Output: The sentence repeated the specified number of times.
def sentence_repeat(value):
    print("This is Srinadh chintakindi\n"*value)
#sentence_repeat(3)

# 6.	Given two variables x and y, perform the following operations and print the results: 
# o	Addition of x and y.
# o	Subtraction of y from x.
# o	Multiplication of x and y.
# o	Division of x by y.
# o	x raised to the power of y.
# o	The remainder when x is divided by y.
# o	The floor division of x by y.

def operations(x,y):
    print(f"1. Addition {x+y}")
    print(f'2. Subtraction {x-y}')
    print(f'Multipliy {x/y}')
    print(f'X Power y {x**y}')
    print(f'Floor Division {x//y}')
#operations(3,2)

# 7.	Define a variable value and assign any numerical value to it. Ask the user to input a new value. Update the variable value with the new input and print the updated value.
# •	Expected Input: A numerical value (e.g., "42")
# •	Expected Output: The updated value of the variable.
# These questions cover a range of scenarios related to variables and data types in Python. You can use input() function to get user input for interactive questions

def updateValue(value):
    number = 5;
    print(f'original value {number}');
    number =value;
    print(f'Updated value {number}');

updateValue(int(input("Enter a new number : \n")))
