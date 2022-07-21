class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index=0
        hashmap={}
        sub=""
        if len(strs)==0 or strs[0]=="":
            return sub
        else:   
            while index<len(min(strs)):
                
                for i in strs:
                    hashmap[i]=i[index]
                if len(set(hashmap.values()))==1:   #
                    sub+=i[index]
                    index+=1
                else:
                    break
            return sub
                
            