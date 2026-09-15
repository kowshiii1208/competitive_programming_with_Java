class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n&k!=k:
            return -1
        else:
            c=0
            num = n-k
            while num:
                c += num&1
                num = num>>1
        return c
