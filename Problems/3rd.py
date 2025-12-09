# Given a list of numbers, remove duplicates without using set().
import pandas as pd
li=[1,2,3,4,5,6,7,8,9,8,3,5,6,2,6,8,0,1,0,33,44,44,7,87,]
def remove(num):
    uniqe=[]
    for n in num:
        if n not in uniqe:
            uniqe.append(n)
    return uniqe

ab=remove(li)
print(ab)
