'''
Q1.  Write a Python program to get a string made of the first and the last 2 chars from a given string.
     If the string length is less than 2, return instead of the empty string
'''
from pdb import set_trace
from pydoc import stripid

'''
Ans :

str1='Happy End'

if len(str1)<2:
    print(True)
else:
    print(str1[:2]+str1[-2:]) # Hand
'''


#Q2. Python string program that takes a list of strings and returns the length of the longest string.
#Ans

'''
str2 = "Python string program that takes a list of strings and returns the length of the longest string"
long_str = ""
long_str_count = 0
word_list = str2.split()

for word in word_list:
    if len(word) > len(long_str):
        long_str = word
        long_str_count = len(word)
    else:
        continue
# print("longest string is : ",long_str)
print("longest string count is : ",long_str_count)

'''

# Q3. Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#Ans

'''
str3 = "Programming"
print(str3[-2:]*4)
'''

# Q4.Python string program to reverse a string if it’s length is a multiple of 4.

'''

str4 = "Programming is good."

if len(str4)%4==0:
    print(str4[::-1])
else:
    print(str4)

'''

#Q5. Python string program to count occurrences of a substring in a string.
#Ans

'''
str5 = """Python string is a sequence of characters, such as “hello”. 
        They can be used to represent text in a programming language. 
        Strings can be created by enclosing a sequence of characters between double quotes, 
        such as “hello”, or by using the str() function."""
sub_str =" as "

print(str5.count(sub_str))

'''

#Q6. Python string program to test whether a passed latter is a voewl or consonant.
#Ans

'''
str_data = str(input("Enter a data : "))
voewl= ['a','e','i','o','u']
for latter in str_data:
    if latter.lower() in voewl:
        print(latter, "is voewl")
    else:
        print(latter, "is consonant")
'''


# Q7. Find the longest and smallest word in the iput string.
#Ans

'''
string = str(input("Enter a string : "))
split_words = string.split(" ")
longest =""
smallest =""
sec_largest = ""
for word in split_words:
    if len(word) > len(longest):
        longest = word
    elif len(word) > len(sec_largest) and len(word)< len(longest):
        sec_largest = word
    elif len(word)> len(smallest) and len(word) < len(sec_largest):
        smallest = word


print("The longest string is : ",longest)
print("The smallest string is : ",smallest)
'''
# Alternate ans

'''
string = input("Enter a string: ")
words = string.split()

longest = words[0]
smallest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(smallest):
        smallest = word

print("Longest word:", longest)
print("Smallest word:", smallest)

'''
# Alternate ans
'''
string = str(input("Enter a string : "))
split_words = string.split(" ")

print("Longest word is: ", max(split_words, key=len))
print("Smallest word is: ", min(split_words, key=len))

'''

# Q8. Print most simultaneously repeated characters in a string.

'''
str="Aniket is good in studs"
most_repeated_char=''
most_repeated_char_count=0

temp = 1
for i in range(len(str)-1):
    if str[i]==str[i+1]:
        temp = temp + 1
        if temp > most_repeated_char_count:
            most_repeated_char_count = temp
            most_repeated_char = str[i]
        else:
            continue

print("most repeated char: ",most_repeated_char)
print("most repeated char count: ",most_repeated_char_count)

'''

#9). Write a Python program to calculate the length of a string with loop logic.
'''
str = "Hello aniket shinde"
count = 0
for char in str:
    count = count + 1

print("lengt of string is :", count)
'''
# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”
'''
str = "Programming"
list = ''

for char in str:
    if char in list:
        list = list + "$"
    else:
        list = list + char

print(list)

'''
# 11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”
'''
input = "SqaTool"

print(input[-1]+input[1:-1]+input[0]) #lqaTooS

'''

#12). Write a python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”
'''
str = "Its Online Learning"
split_str = str.split(" ")

for word in split_str:
    print(word[-1]+word[1:-1]+word[0], end=" ")
'''
'''
string = "Its Online I Learning"
words = string.split()

for word in words:
    if len(word) > 1:
        new_word = word[-1] + word[1:-1] + word[0]
    else:
        new_word = word
    print(new_word, end=" ")
'''
# 13). Write a python to count vowels from each word in the given string show as dictionary output.
# Input = “We are Learning Python Codding”
# output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

'''
string = "We are Learning Python Codding"
split_string = string.split(" ")
vovels = "aeiou"
dictionary = dict()
for word in split_string:
    count = 0
    for char in word:
        if char in vovels:
            count = count + 1
    dictionary[word] = count

print("Output: ",dictionary)
'''
# 14). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

'''
str = "Sqa Tools Learning"
vov = "aeiou"
output = ""

for word in str:
    if word.lower() in vov :
        output = output + (word*3)
    else:
        output = output + (word*2)

print(output)
'''

#15). Write a python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”

'''
input = "Cricket Plays Virat"
split_input = input.split(" ")
split_input.reverse()
result = " ".join(split_input)
print(result)

'''
# 16). Write a python program to get all the digits from the given string.
# Input = “””
# Sinak’s 1112 aim is to 1773 create a new generation of people who
# understand 444 that an organization’s 5324 success or failure is
# based on 555 leadership excellence and not managerial
# acumen
# “””
# Output = [1112, 5324, 1773, 5324, 555]
'''
input = """ Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
split_input = input.split(" ")
output = []

for char in split_input:
    if char.isnumeric():
        output.append(char)
    else:
        continue

print(output)

'''

# 17). Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”

'''
input1 = "JAVA is the Best Programming Language in the Market"

print(input1.replace(input("Enter old value: "),input("Enter new value: ") ))

'''

# 18). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]

'''
input = "Python efe language aakaa hellolleh"
split_list = input.split()
output = []

for char in split_list:
    if char == char[::-1]:
        output.append(char)

print(output)

'''

#19). Write a Python program to create a string with a given list of words.
#Input = [“There”, “are”, “Many”, “Programming”, “Language”]
#Output = There are many programming languages.
'''
input = ["There", "are", "Many", "Programming", "Language"]

print(" ".join(input))

'''

# 20). Write a Python program to remove duplicate words from the string.
# Input = “John jany sabi row john sabi”
# output = “John jany sabi row”
'''
input = "John jany sabi row john sabi"
word = input.lower().split()
output = []
for char in word:
    if char not in output:
        output.append(char)

print(" ".join(output).capitalize())

'''
# 21). Write a Python to remove unwanted characters from the given string.
# Input = “Prog^ra*m#ming”
# Output = “Programming”
# Input = “Py(th)#@&on Pro$*#gram”
# Output = “PythonProgram”
'''
input = "Prog^ra*m#ming"
output = ""

for char in input:
    if char.isalnum():
        output = output + char
    else:
        continue
print(output)

'''

# 22). Write a Python program to find the longest capital letter word from the string.
# Input = “Learning PYTHON programming is FUN”
# Output = “PYTHON”

'''
input = "Learning PYTHON programming is FUN "
split_list = input.split()
output = ""

for char in split_list:
    if char.isupper():
        if len(char)> len(output):
            output = char

print(output)

'''

# 23). Write a Python program to get common words from strings.
# Input String1 = “Very Good Morning, How are You”
# Input String1 = “You are a Good student, keep it up”
# Output = “You Good are”

input1 = "Very Good Morning, How are You"
input2 = "You are a Good student, keep it up"
output = []

split_input1 = input1.split()
split_input2 = input2.split()

for char in split_input1:
    if char in split_input2:
        output.append(char)

print(" ".join(output))
