class Solution:
    def makeFancyString(self, s: str) -> str:
        out=s[0:2]
        for i in range(2,len(s)):
            if s[i]==s[i-1] and s[i]==s[i-2]:
                pass
            else:
                out+=s[i]
        return out