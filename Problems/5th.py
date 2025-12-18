# Kadane’s Algorithm (max subarray sum)
def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(arr))  # Output: 6



# Another Example
def max_subarray_prefix(arr):
    prefix_sum = 0
    min_prefix = 0
    max_sum = float('-inf')

    for num in arr:
        prefix_sum += num
        max_sum = max(max_sum, prefix_sum - min_prefix)
        min_prefix = min(min_prefix, prefix_sum)

    return max_sum


# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_prefix(arr))  # Output: 6
