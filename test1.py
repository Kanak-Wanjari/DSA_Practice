# nums = [11,2,15,7]

# target = 9

class LeetCode():
    # def twosum(self,nums,target):
    #     if not nums:
    #         return 0
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return i,j
                
    #     return 0
    
    def maximumsubarray(self, nums):
        cur_max = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_max + nums[i] > nums[i]:
                cur_max = cur_max + nums[i]
            else:
                cur_max = nums[i]

            if cur_max > max_sum:
                max_sum = cur_max
        return max_sum
    
    def stocksell(self,nums):
        max_profit = 0
        min_price = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < min_price:
                min_price = nums[i]
            else:
                profit = nums[i] - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return (max_profit)
    
    def twosum(self, nums):
        
        target = 9

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                targeto = nums[i] + nums[j]
                if targeto == target:
                    return i,j
                
    def bands(self,prices):

        min_price = prices[0]
        max_profit  = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return(max_profit)
    
    def maxsubarray(self, nums):
        
        v1 = nums[0]
        v2 = nums[0]

        for i in range(1, len(nums)):
            if v1 + nums[i] > nums[i]:
                v1 = v1 + nums[i]
            else:
                v1 = nums[i]

            if v1 > v2:
                v2 = v1
        
        return v2
    
    def condup(self, nums):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False



calc = LeetCode()
# max_result = calc.stocksell([7,6,4,3,1])
# print(max_result)
# result = calc.twosum([11,2,15,7],9)


# twosum = calc.twosum([11,2,15,7])

# bands = calc.bands([7,1,5,3,6,4])

# maxsubarray = calc.maxsubarray([-2,1,-3,4,-1,2,1,-5,4])

condup = calc.condup([1,2,3,4])


print(condup)