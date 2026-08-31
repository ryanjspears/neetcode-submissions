class Solution:
    def minOperations(self, logs: List[str]) -> int:
        pos = 0
        for log in logs:
            if log == "../" and pos > 0:
                pos-=1
            elif log != "./" and log != "../":
                pos+=1

        return pos
        