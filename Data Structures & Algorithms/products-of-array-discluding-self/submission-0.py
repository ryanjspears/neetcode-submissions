class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        zero_index = -1
        i = -1
        for num in nums:
            i += 1
            if num == 0:
                count_zero+=1
                zero_index = i 
        
        if count_zero > 1:
            res = []
            for i in range(len(nums)):
                res.append(0)

            return res

        if count_zero == 1:
            res = []
            for i in range(len(nums)):
                res.append(0)
            total = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    total *= nums[i]
            
            res[zero_index] = total

            return res

        #Total Count
        total = 1
        for num in nums:
            total *= num

        res = []
        for num in nums:
            res.append(int(total/num))

        return res