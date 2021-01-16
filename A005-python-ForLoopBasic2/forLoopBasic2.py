# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(lst):
    newList = ['big' if item > 0 else item for item in lst]
    return newList

# print(biggie_size([-1, 3, 5, -5]))
# print(biggie_size([-1, -3, 5, -0]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of 
# positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(lst):
    numPos = 0

    if len(lst) < 2:
        return False

    for item in lst:
        if item > 0:
            numPos += 1
        
    lst[len(lst) - 1] = numPos
    return lst

# print(count_positives([-1, 1, 1, 1]))
# print(count_positives([1,6,-4,-2,-7,-2]))
# print(count_positives([1, 1]))
# print(count_positives([1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(lst):
    totalSum = 0

    for item in lst:
        totalSum += item
    
    return totalSum

# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(lst):
    totalSum = 0

    for item in lst:
        totalSum += item
    
    return totalSum / len(lst)

# print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(lst):
    return len(lst)

# print(length([37, 2, 1, -9]))
# print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(lst):
    if not lst:
        return False

    minVal = lst[0]
    for item in lst:
        if minVal > item:
            minVal = item
    
    return minVal

# print(minimum([37, 2, 1, -9]))
# print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(lst):
    if not lst:
        return False
    
    maxVal = lst[0]
    for item in lst:
        if maxVal < item:
            maxVal = item

    return maxVal

# print(maximum([37,2,1,-9]))
# print(maximum([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has 
# the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}
def ultimate_analysis(lst):
    if not lst:
        return false

    dict = { 
        'sumTotal': sum_total(lst), 
        'average': average(lst), 
        'minimum': minimum(lst), 
        'maximum': maximum(lst),
        'length': length(lst)}

    return dict

# print(ultimate_analysis([37, 2, 1, -9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(lst):
    mid = round(len(lst) / 2)

    for i in range(mid):
        temp = lst[i]
        lst[i] = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = temp
    
    return lst

# print(reverse_list([37, 2, 1, -9]))
# print(reverse_list([1, 2]))
# print(reverse_list([1, 2, 3]))
# print(reverse_list([1, 2, 3, 4]))
# print(reverse_list([1, 2, 3, 4, 5]))