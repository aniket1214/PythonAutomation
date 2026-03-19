
# 14). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”


input = "Sqa Tools Learning"
vowel = "aeiouAEIOU"
output=""
for word in input:
    if word in vowel:
        output = output + (word*3)
    else:
        output = output + (word*2)

print(output)