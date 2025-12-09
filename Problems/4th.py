# Reverse a string without using slicing.
def reverse_string(s: str) -> str:
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str
str=input("enter the string:")
print(reverse_string(str))