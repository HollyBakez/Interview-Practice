# Does the given string have all unique characters
'''
def isUnique(words = str):
    sizeString = len(words)
    reverseString = words
    count = 0
    for element in words:
        checker = 0
        for index in reverseString:
            if index == element:
                checker += 1 
        if checker > 1:
            return False
    return True
# this algorithm would be
# time complexity would be O(n^2) since it would iterate through two arrays comparing  through two for loops
# space complexity would also be O(n) where n is the length of the string
# test case
test = "Hello"
isUnique(test)
'''     

# time complexity would be O(1)
# space complexity O(1)
def isUnique(words = str):
    if len(words) > len(set(words)):
        return False
    return True

isUnique("hjkhafn=;")