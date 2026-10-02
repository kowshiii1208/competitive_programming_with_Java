class Solution:
    
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        curr = []
        def backtrack(oc,cc):
            if oc == n and cc == n:
                ans.append("".join(curr))
                return 
            if oc<n:
                curr.append("(")
                backtrack(oc+1,cc)
                curr.pop()
            if cc<oc:
                curr.append(")")
                backtrack(oc,cc+1)
                curr.pop()
        backtrack(0,0)
        return ans
        