#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        right, left = 0,0
        currSum = arr[right]
        if currSum == s:
            return (1,1)
        
        while(right < n-1):
            if (currSum + arr[right+1] <= s):
                currSum += arr[right+1]
                right += 1
            else:
                currSum -= arr[left]
                left += 1
            
            if(currSum == s and left <= right):
                return (left+1, right+1)
        return [-1]