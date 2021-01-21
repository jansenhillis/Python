#1/19/2021 - Lecture Questions
'''
Challenges
    3 challenges
    6 minute breakout room, can give longer if want to allow time for building out the functions
    SS should first create the function and parameters. Then if they have time, they can code them out


set 1 -
    1- design a function that accepts a word returns true / false indicating if the word is a vowel (has a value?)

    2- design a function accepts login credentials and returns a role based on the credentials given
        - If the caller does not provide a password, visitor role is assigned (default)
        - If the caller provides a password, admin role is assigned

    3- design a function that accepts an the following information about an animal and returns a dictionary with the data.
        - name
        - country of origin
        - is it a mammal?
        - dob
        
        - unless otherwise specified, all animals will be mammals from Africa

'''
# def is_vowel(word):
#     vowels = ["a", "e", "i", "o", "u"]
#     for character in word:
#         for vowel in vowels:
#             if (character == vowel):
#                 return True

#     return False
# print(is_vowel("Hello"))

# Total Time: 1.0046606063842773
import time
# begin =time.time()
# def is_vowel(word):
#     for character in word:
#         if (character == 'a' or 
#         character =='e' or 
#         character =='i' or
#         character =='o' or
#         character =='u'):
#             return True
#     return False
# print(is_vowel("bbbbbbbbe"))
# time.sleep(1)
# end=time.time()
# print(f"Total runtime of the program with if is {end - begin}") 

# Total Time: 1.0063855648040771
# begin = time.time()
# def is_vowel(word):
#     if "a" or "e" or "i" or "o" or "u" in word:
#         return True
#     else:
#         return False

# print(is_vowel("bbbbbbbbe"))
# time.sleep(1)
# end=time.time()
# print(f"Total runtime of the program with if is {end - begin}") 