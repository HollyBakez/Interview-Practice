'''
1.6 String Compression
Implement a method to peform basic string compression using the counts of repeated characters
You may assume only uppercase and lowercase letters (a-z)
Ex)
Input: aabcccccaaa 
Output: a2b1c5a3

'''
# aabcccdd
# ^ 
# pivot begins at the first index of the string
# a-count +=1 
#   [] <---- append a 
def string_compression(S):
    compressed_list = [] 
    pivot = 0
    place = 0
    for c in S:
        checker = 0
        char = S[place]
        compressed_list.append(char)
        while S[place] == S[pivot]:
            checker +=1
            if (pivot+1) == len(S):
                compressed_list.append(checker)
                # if the compressed string is longer than the og
                # print the og string
                if len(compressed_list) >= len(S):
                    return print(S)
                else:
                    return print(compressed_list)
            else:
                pivot += 1
        if S[place] != S[pivot] and checker==0:
            checker +=1
        place = pivot 
        compressed_list.append(checker)
        
        

# test cases
string_compression("aaabccd")
string_compression("aabcccccaaa")
