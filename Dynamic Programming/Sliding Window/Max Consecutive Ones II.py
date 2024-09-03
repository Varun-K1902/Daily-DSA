# 487. Max Consecutive Ones II
# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# Example 1:
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.

def max_con_ones(nums, n):
    max_win_size = cur_win_size = 0
    count_zeros = 0
    left = right = 0
    while right < n:
        cur_win_size += 1 #we will inc current window size irresp of 0 or 1.
        if nums[right]==0:
            count_zeros += 1 #if current element is 0 inc count_zeros
            
        if count_zeros == 2: #since we are incrementing cur_win_size irresp of 0 or 1, there might be a case where the window as 2 zeros and we should not use that window to calculate max_win_size, so decrease window size to count_zero=1
            while count_zeros == 2:
                if nums[left]==0:
                    count_zeros -= 1
                left+=1
                cur_win_size -= 1
        max_win_size = max(max_win_size, cur_win_size)
        right += 1 #increment right after processing it, ex: right starts at 0, process right = 0 first and inc it at end
        
    return max_win_size

arr = [1, 0, 1, 1, 0]
arr1 = [1, 0, 0, 1, 1, 1, 1, 1]
print(max_con_ones(arr, len(arr)))
print(max_con_ones(arr1, len(arr1)))

