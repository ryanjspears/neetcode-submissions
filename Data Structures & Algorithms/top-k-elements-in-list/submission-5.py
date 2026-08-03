class Solution:
    #inserts numbers in order
    def insert(self, listy, num):
        if len(listy) == 0:
            listy.append(num)
        else:
            p = -1
            while p < len(listy) - 1:
                p+=1
                if listy[p] == num:
                    return
                
                if num < listy[p]:
                    listy.insert(p, num)
                    return

            listy.append(num)
        print(" ")
        print(listy)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #init count
        mappy = {}

        for num in nums:
            if mappy.get(num) is None:
                mappy[num] = 1
            else:
                mappy[num]+= 1
        
        #Counts to numbers
        count_stack = []
        count_map = {}
        for key, value in mappy.items():
            if count_map.get(value) is None:
                count_map[value] = [key]
                self.insert(count_stack, value)
            else:
                count_map[value].append(key)

        for i in count_stack:
            print(i)

        
        #Read off counts
        res = []
        for i in range(0,k):
            high_count = count_stack[-1]
            temp_nums = count_map[high_count]
            res.append(temp_nums.pop())
            if (len(temp_nums) == 0):
                count_stack.pop()

        return res


        

        
                 
        