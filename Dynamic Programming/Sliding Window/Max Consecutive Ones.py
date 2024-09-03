class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_win_size = 0
        cur_win_size = 0
        for right in range(len(nums)):
            #expand window size if current number is 1
            if nums[right]==1:
                cur_win_size += 1
                max_win_size = max(max_win_size, cur_win_size)
            else:
                #if current number is 0 then we need to start a new window
                cur_win_size = 0
        return max_win_size
