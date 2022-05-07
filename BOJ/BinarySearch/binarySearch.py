from typing import List
class Solution:
    def binarySearchIte(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                end = mid - 1
            
            else:
                start = mid + 1
                
        return -1


    def binarySearchRec(self, nums: List[int], start, end, target: int) -> int:
    
        # Check base case
        if end >= start:
    
            mid = start + (end - start) // 2
    
            # If element is present at the middle itself
            if nums[mid] == target:
                return mid
    
            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif nums[mid] > target:
                return binarySearchRec(nums, start, mid-1, target)
    
            # Else the element can only be present
            # in right subarray
            else:
                return binarySearchRec(nums, mid + 1, end, target)
    
        else:
            # Element is not present in the array
            return -1
