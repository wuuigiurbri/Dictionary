#activity 1
#count of the occurences of vowels in the string entered by the user
# string1= input("Enter a string ")
# vowels= {'a':0, 
#          'e':0,
#          'i':0,
#          'o':0,
#          'u':0}

# for i in string1:
#     if i in vowels:
#         vowels[i] +=1
# print (vowels)

#activity 2
#count the occurences of each letter in the alphabet entered by the user
string2= input("Enter a string ")
letters= {}


for i in string2:
    if i.isalpha():
        if i in letters:
            letters[i] +=1
        else:
            letters = 1
print (letters)