def search(arr, x):
    n = len(arr)
    
    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
arr=[1,2,3,4,5]
x=int(input("enter target:"))
print(search(arr,x))
