class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        t = 0
        t += requests[0]
        for i in range(1,len(requests)):
                t+=abs(requests[i-1]-requests[i])
        return t