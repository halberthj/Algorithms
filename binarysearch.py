#Leet Code 'Binary Search' submission : https://leetcode.com/problems/binary-search/submissions/866948345/?envType=study-plan&id=algorithm-i
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        i = 0
        j = len(nums)-1
            
        while i <= j:
            mid = (i+j)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                j = mid-1
                
            else:
                i = mid+1
            
        return -1
