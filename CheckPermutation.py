
def isPermutation(words1 = str, words2 = str):
    if len(words1) != len(words2):
        return False
    else:
        if sorted(words1) == sorted(words2):
            return True
        else:
            return False

# This should take O(1) time runtime and space complexity O(1)


test1 = "Hello World"
test2 = "World Hello"
isPermutation(test1, test2)