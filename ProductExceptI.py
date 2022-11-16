"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def productExceptValue(arr):
    product = 1
    # get product in O(n) time
    for value in arr:
        product *= value
    returnArr = []  # to store the returning array
    for value in arr:
        returnArr.append(product/value)
    return returnArr


def productExceptValueWithoutDivision(arr):
    frontToRare = []
    rareToFront = arr[:]    # copy it to avoid null ptrs exception
    for i in range(len(arr)):  # O(n)
        if i == 0:
            frontToRare.append(arr[i])
        else:
            frontToRare.append(arr[i] * frontToRare[i-1])
    for i in range(len(arr) - 1, -1, -1):  # O(n)
        if i == len(arr) - 1:
            rareToFront[i] = arr[i]
        else:
            rareToFront[i] *= rareToFront[i+1]
    returnArr = []
    for i in range(len(arr)):
        if i == len(arr) - 1:
            returnArr.append(frontToRare[i-1])
        elif i == 0:
            returnArr.append(rareToFront[i+1])
        else:
            returnArr.append(frontToRare[i-1]*rareToFront[i+1])
    return returnArr


print(productExceptValue([3, 2, 1]))
print(productExceptValue([1, 2, 3, 4, 5]))
print("----- without division ------")
print(productExceptValueWithoutDivision([3, 2, 1]))
print(productExceptValueWithoutDivision([1, 2, 3, 4, 5]))
