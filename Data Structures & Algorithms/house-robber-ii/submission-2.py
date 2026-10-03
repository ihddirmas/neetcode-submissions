class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, flag):
            
            if (i, flag) in memo:
                return memo[(i,flag)]
            
            if i > len(nums)-1 :
                return 0
            if i == len(nums)-1 and flag == True :
                return 0
            
            if i == 0 :
                rob = nums[i] + dfs(i+2, flag=True)
                skip = dfs(i + 1,flag= False) 
                
            else:
                rob = nums[i] + dfs(i+2, flag)
                skip = dfs(i+ 1, flag)
                
            memo[(i,flag)] = max(rob, skip)
            return max(rob, skip)
            
        return dfs(0, False)