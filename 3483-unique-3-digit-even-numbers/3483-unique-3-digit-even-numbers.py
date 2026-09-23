class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f = Counter(digits)
        res = 0
        for i in range(100,1000,2):
            a,b = divmod(i,100)
            c,d = divmod(b,10)
            res += f[a] >0 and f[c]>(a==c) and f[d] >(a==d)+(c==d)
        return res