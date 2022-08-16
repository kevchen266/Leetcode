class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        l = len(nums)
        for i , a in enumerate(nums):
            if i == 0 or nums[i] > nums[i-1]:
                left,right = i+1, l-1
                
              
                while right > left:
                    s = nums[left] + nums[right] + a
                    if s > 0:
                        right -= 1
                    if s < 0:
                        left += 1
                    if s == 0:
                        while right > left and nums[left] == nums[left+1]:
                            left += 1
                        while right > left and nums[right-1] == nums[right]:    
                            right -= 1
                        res.append([nums[right],a, nums[left]])
                        left += 1
                        right -= 1

        
        return res
            
        
        # [-4, -1, -1, 0, 1, 2]
