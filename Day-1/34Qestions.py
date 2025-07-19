# 1.	Concatenate two strings str1 and str2, and print the result. 
# o	Expected Input: str1 = "Hello", str2 = "World"
# o	Expected Output: "HelloWorld"
def concat():
    str1="Hello"
    str2 = 'World'
    print(str1+str2)
#concat()
# 2.	Ask the user to enter their name and a greeting. Concatenate the name and greeting to form a personalized message and print it. 
# o	Expected Input: name = "John", greeting = "Hi"
# o	Expected Output: "Hi John"
def greeting(name,greet):
    print(greet+' '+name)
#greeting(input("Enter your name: "),input("Enter greet :"))

# 3.	Create a string word and repeat it 5 times. Print the result. 
# o	Expected Input: word = "Python"
# o	Expected Output: "PythonPythonPythonPythonPython"
def stringRepeat(word,repeat):
    print(word*repeat)
# stringRepeat("Python",5)

# 4.	Ask the user to enter a word and a number. Repeat the word as many times as the given number and print the result. 
# o	Expected Input: word = "Hello", number = 3
# o	Expected Output: "HelloHelloHello"
def stringRepeat(word,repeat):
    print(word*repeat)
# stringRepeat("Python",5)

# 5.	Create a string sentence and find its length. Print the length of the sentence. 
# o	Expected Input: sentence = "This is a sample sentence."
# o	Expected Output: 27
def Stringlen():
    print(len("I'm listening Ae Dil hai Mushkil"))
#Stringlen()

# 6.	Ask the user to input a sentence. Find the length of the sentence, and print the last character of the sentence. 
# o	Expected Output: Length of the sentence and the last character.
def lastchar(string):
    print(f'last character of String :{string[-1]}')
#lastchar(input("Enter a sentence: "))

# 7.	Create two strings str1 and str2. Find the lengths of both strings and concatenate them. Print the concatenated string. 
# o	Expected Input: str1 = "Hello", str2 = "World"
# o	Expected Output: "HelloWorld"

def concate(str1,str2):
    print(f'length of First String {len(str1)}')
    print(f'Length of second String :{len(str2)}')
    print(f'Concatination of both strings : {str1+str2}')

#concate(input("Enter string 1: "),input("Enter String 2: "))


# 8.	Ask the user to enter two words, word1 and word2. Concatenate the two words with a space in between and print the result. 
# o	Expected Input: word1 = "Hello", word2 = "Python"
# o	Expected Output: "Hello Python"
def concate(str1,str2):
    print(f'length of First String {len(str1)}')
    print(f'Length of second String :{len(str2)}')
    print(f'Concatination of both strings : {str1+" "+str2}')

#concate(input("Enter string 1: "),input("Enter String 2: "))


# 9.	Create a string pattern containing "*" character and repeat it to form a pattern. The pattern should have 5 rows. Print the resulting pattern. 
# o	Expected Output:
# o	*
# o	**
# o	***
# o	****
# o	*****
def leftTrinagle(number):
    for i in range(0,number+1):
        for j in range(0,i):
            print("*",end="")
        print()
# leftTrinagle(5)
