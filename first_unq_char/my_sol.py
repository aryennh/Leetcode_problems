class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hmap = {}
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = 1
            else:
                hmap[s[i]] +=1
        
        for x in hmap : 
            if hmap[x] == 1 : 
                return s.index(x)
        return -1
            
