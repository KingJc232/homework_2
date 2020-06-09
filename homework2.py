"""
File: homework2.py
"""


INT_MIN = -2147483648
INT_MAX = 2147483648

#Using Divide and Conquer Time Complexity O(nlogn) 
def problem_1(arr, start, end):

    answer = [] #Contains 3 elements the BuyIndex, SellIndex, MaxProfit 

    #Base Case If only One element then we buy and sell it Giving us Zero 
    if end == start:
        answer.append(start) #Pushing the Start index since its an array of only one element 
        answer.append(end) 
        answer.append(0) #Buying and Selling Stock
        return answer 

    midIndex = int((start + end) /2)
    #Handling the First Two Cases Recursively 
    #Splitting Array To Left and Right 
    leftBest  = problem_1(arr, start, midIndex)
    rightBest = problem_1(arr, midIndex + 1,  end)

    #Handling the Third Case If the maxProfit is between the Left and Right array 

    #Calculating the MinIndex and the MinElement of the Left Array 
    tempMin = _calculateMin(arr, start, midIndex)

    minIndex = tempMin[0] #Getting the MinIndex of the Left Array
    minProfitOfLeftArray = tempMin[1] #Getting the MinElement of the Left Array 

    #Calculating the MaxIndex and the MaxElement of the Right Array 
    tempMax = _calculateMax(arr, midIndex + 1, end)

    maxIndex = tempMax[0] #Getting the MaxIndex of the Right Array 
    maxProfitOfRightArray = tempMax[1] #Getting the MaxElement of the Right Array 

    crossBest = maxProfitOfRightArray - minProfitOfLeftArray

    #Calculating the MaxProfit 
    maxProfit = max(leftBest[2], rightBest[2], crossBest)
    
    if maxProfit == 0:
        answer.append(0)
        answer.append(0)

    elif crossBest == maxProfit:
        answer.append(minIndex)
        answer.append(maxIndex)

    answer.append(maxProfit)

    return answer

#Returns an Array 
#With the MaxIndex as its First Element 
#And with the MaxElement as its Second Element 
def _calculateMax(arr, start, end):

    answer = [] 
    maxIndex = -1
    maxElement = INT_MIN #Initially its the worst case 

    for i in range(start, end+1):
        if arr[i] > maxElement:
            maxElement = arr[i]
            maxIndex = i

    answer.append(maxIndex)
    answer.append(maxElement)
    return answer 

def _calculateMin(arr, start, end):

    answer = []
    minIndex = -1
    minElement = INT_MAX #Initially its the worst case 

    for i in range(start, end + 1):
        if arr[i] < minElement:
            minElement = arr[i]
            minIndex = i

    answer.append(minIndex)
    answer.append(minElement)
    return answer 

def problem_2(arr, start, end ):


    #Base Case 
    if start == end:
        return start  

    midIndex = (start + end)// 2
    left = problem_2(arr, start, midIndex)
    right = problem_2(arr,midIndex + 1, end)

    maxElement = max(arr[left], arr[right])

    if arr[left] == maxElement:
        return left
    else:
        return right

def problem_3(arr, start, end):
    
    #BaseCase an Array of only one element 
    if start == end:
        return 0 

    midIndex = (start + end) // 2

    #Splitting the Array into a Left array and Right Array 
    left = problem_3(arr, start, midIndex)
    right = problem_3(arr, midIndex + 1, end)

    #Calculating the Sum of the Left Array 
    leftSum = sumElements(arr, start, midIndex)
    #Calculating the Sum of the Right Array
    rightSum = sumElements(arr, midIndex +1, end)

    #Calculating the Largest Difference Between the Sublist 

    difference = abs(rightSum - leftSum)

    if difference >= max(left, right):
        return difference
    else:
        return max(left, right)

def sumElements(arr, start, end):
    elementSum = 0
    for i in range(start, end+1):
        elementSum += arr[i]

    return elementSum   

#Suggesting an Algorithm With Time Complexity O(n)
def problem_3_TimeComplexity_n(arr, start, end):
    
    #Returning an Array of size Two
    answer = [] #Contains the Sum and the difference 

    #Base Case If the Array Only Has One Element
    if start == end:
        answer.append(arr[start]) #Appending the Sum of the Array 
        answer.append(0) #The Difference of the array
        return answer 

    #Calculating the MidIndex 
    midIndex = (start + end) //2
    #Spliting the Array into a Left Array and a Right Array 

    left = problem_3_TimeComplexity_n(arr, start, midIndex)
    right = problem_3_TimeComplexity_n(arr, midIndex + 1, end)

    #Calculating the Difference Between the left and right array 
    difference = abs(left[0] - right[0])

    #Calculating the Greatest Difference 
    greatestDiff = max(max(difference, right[1]), left[1])

    #Returning the Sum of the array and the Greatest Difference 
    return [left[0] + right[0], greatestDiff]

def problem_4(table, valueToFind, start, end, numberOfRows, numberOfCols):

    #First things First Find the Row the value might be in between using Binary Search

    #Base Case 
    if end < start:
        return False #Not Found 

    midRowIndex = (start + end) // 2 #Calculating the Middle Row Index of the 2D Array 

    if valueToFind >= table[midRowIndex][0] and valueToFind <= table[midRowIndex][numberOfCols -1]:
        #We found the Row Now do Binary Search On the Columns of that row
        return binarySearch(table,valueToFind,0, numberOfCols -1, midRowIndex)

    elif valueToFind < table[midRowIndex][0]:
        return problem_4(table, valueToFind, start, midRowIndex -1, numberOfRows, numberOfCols)
    else:
        return problem_4(table, valueToFind, midRowIndex + 1, end, numberOfRows, numberOfCols) 



#Does Binary Search on The Columns of the Table
def binarySearch(table,valueToFind, start, end, midRowIndex):

    #Base Case 
    if end < start:
        return False #Element Not Found 

    midColIndex = (start + end) //2 #Calculating the MidIndex

    if table[midRowIndex][midColIndex] == valueToFind:
        return True #Value Found 

    #else if ValueToFind Might Be in the Right part of the array 
    elif table[midRowIndex][midColIndex] < valueToFind:
        return binarySearch(table,valueToFind, midColIndex +1 , end, midRowIndex)

    #Else ValueToFind Might Be in the Left Part of the Array 
    else:
        return binarySearch(table,valueToFind, start, midColIndex -1, midRowIndex)


def main():

    arr = [2,1,3,6,4,5]
    #arr = [1, 2, 90, 10, 110] 
    #arr = [2,1,3]
    #arr = [5,2,10,1]
    #arr = [10, 1, 2, 5]
    #arr = [10,9,8,7]


    print(problem_1(arr, 0, len(arr) -1 ))
    #print(problem_2(arr, 0, len(arr) -1 ))
    #print(problem_3(arr, 0, len(arr) -1 ))
    #print(problem_3_TimeComplexity_n(arr, 0, len(arr) - 1 ))

    pass



if __name__ == "__main__":
    main()
