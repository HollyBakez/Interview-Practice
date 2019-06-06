#URLify problem 1.3
# given the true length of the string
# assume that the given string has sufficient space at the end for additional characters (ie, when  %20 is inserted in the whitespace)
#  ex) 'Hello there Mr foo--extra space for when %20 is inserted---', 18 characters including the white spaces in-between

def urlify(words1 = str, length_string = int):
    list_of_words = []
    count = 0
    for c in words1[:length_string]:
        list_of_words.append(c)
        if list_of_words[count] == " ":
            list_of_words[count] = "%20"
        print(list_of_words[count], end=" ")
        count += 1  
    print("\n")

# test cases
urlify("Hello there Mr foo", 18)
urlify("Mr John Smith     ", 13)
urlify("hey =_0 9bro wtf   ", 16)

# time and space complexity explaination 
# space complexity of this program would be O(n)
# since we would be allocation n space in our array 
# where n is the amount of characters and whitespaces in 
# our given string input

# our time complexity would also be O(n) where n is the 
# length of our given strength 
# we wouldn't be able to get O(1), since strings are immutable 
