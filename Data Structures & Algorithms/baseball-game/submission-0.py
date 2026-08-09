class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "C":
                stack.pop()
            else:
                num = int(op)
                stack.append(num)

        sum = 0
        for num in stack:
            sum+=num
        return sum
        