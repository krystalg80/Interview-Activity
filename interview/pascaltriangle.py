# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:         #call/create our class
    def generate(self, numRows: int) -> list[list[int]]:        #create the method which will take an integer of number of rows and it will return a list of integers
        triangle = []       #this triangle is going to be our list which is empty right now but its what we will be adding our rows into
        for i in range(numRows):    #this is a loop that will iterate each row starting from 0
            row = [1] * (i + 1)     #each row is initialized as a list of one here and the 1 is our starting and the i + 1 will continue adding elements to our row, 1 row, 2 row,3 row etc
            for j in range(1, i):       #this loop will go over the element in each row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]       #j is calculatoing by adding the values from the previous row, this is where all the pascal triangle row magic happens
            triangle.append(row)        #when it is complete it is appended to the triangle list! which is what we will be returning
        return triangle
    
result = Solution()             #here we are going to call the solution class which will be a result
finishedresult = result.generate(5)     #finished result is going to call our solution class which will be result = solution and then . the method and the number of rows we will be using 
print(finishedresult)       #tie it all together and print our finished result!
