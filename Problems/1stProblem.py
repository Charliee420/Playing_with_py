# Easy Level Problems
''' 1st Question 
Write a program to count vowels and consonants in a given string '''
# ANSWER
def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example usage
input_string = "Hello, World!"
vowels, consonants = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")


def count_vo_con(str):
    vowels="aeiou"
    vo=0
    co=0
    for char in str:
        if char.isalpha():
            if char in vowels:
                vo+=1
            else:
                co+=1
    return vo,co
str=input("ENTER ANY STRING: ")
vo,co=count_vo_con(str)
print(f"vowels:{vo} \n consonants:{co}")