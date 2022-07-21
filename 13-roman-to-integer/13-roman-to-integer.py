class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result=hashmap[s[0]]
        for i in range(1,len(s)):
            if hashmap[s[i]]>hashmap[s[i-1]]:
                num=hashmap[s[i]]-hashmap[s[i-1]]-hashmap[s[i-1]]
                result+=num
            else:
                num=hashmap[s[i]]
                result+=num
        return result
                