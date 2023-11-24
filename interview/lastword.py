
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.


class Solution:
    def lengthOfFirstWord(self, s: str) -> int: #this method takes the 's' as a string and returns an integer which will be the number of letters are in the last word
        stripped = s.strip() #removes any leading or trailing white spaces from the string
        strList = stripped.split(" ") #splits the word/string into a list of words and the result will be stored in the next command strList
        firstWord = strList[0] #This line will get the first word of the  strList list and it It assumes that words are separated by spaces.
        return len(firstWord) #the command len will return the length in an integer form of the last word
    
length = Solution()          #here we are going to call the solution class which will be a result
    
finishedresult = length.lengthOfFirstWord("Hi World")       #enter our word we want to call and find the length of

print(finishedresult)           #print our finished results! it should give us 2




