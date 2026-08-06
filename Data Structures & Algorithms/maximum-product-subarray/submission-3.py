class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            number = nums[i]

            # A negative number can turn the current minimum
            # product into the new maximum product.
            if number < 0:
                current_max, current_min = current_min, current_max

            # Starting over at the current number also handles zero.
            current_max = max(number, current_max * number)
            current_min = min(number, current_min * number)

            max_product = max(max_product, current_max)

        return max_product