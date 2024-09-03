def LIS(nums):
  n = len(nums)
  dp = [1]*n #initializing dp array
  for i in range(n): #consider each element as last of subsequence
    maxL=0
    for j in range(i): #finding which element to come before the last element
      if nums[j]<nums[i]:  #considering the element if its only less than the last element
        maxL = max(maxL, dp[j]) #finding the element which gives maximum length
    dp[i]+=maxL

  return max(dp)

nums = [7,7,7,7,7,7,7]
print(LIS(nums))
