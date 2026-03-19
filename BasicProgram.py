# Multilaction Table with usre inpute# (Working)

'''
n = int(input("Enter a number: "))

for i in range (1,11,1):
    mul=n*i
    print(n, " * ",i ," = ", mul)
'''


# Even or Odd Number # (Working)

'''
n = int(input("Enter a number: "))

if n%2==0:
    print(n,"is a even number")
else:
    print(n,"is a odd number")

'''

# Reverse a Number/String: Write a program to reverse a given integer or string (e.g., 1234 to 4321).
'''
n = int(input("Enter a number: "))
rev_num = 0

while n != 0: # This loop will run till n = 0.
    digit = n % 10 # when n % 10 we get last digit seprate and we store in differt variable
    rev_num =  rev_num * 10 + digit # This line is used to add number is rev format ( if we mention rev_num as 1 then all calculation will wrong)
    n = n //10  # We remove the n variable value one by one
print("Reverse number is :" , rev_num)

'''

# Write a progtram to get second largest word fro, given string
'''
str1 = "This is the Largest Data Ever in Python"
word_list = str1.split()
large_word =""
secode_large_word = ""

for word in word_list :
    if len(word)>len(large_word):
        secode_large_word = large_word
        large_word = word

    elif len(word)>len(secode_large_word) and len(secode_large_word)<len(large_word):
        secode_large_word = word

print("Larg numbre : ",large_word)
print("Sec number : ",secode_large_word)

'''



