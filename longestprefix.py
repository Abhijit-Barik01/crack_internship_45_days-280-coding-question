class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word=min(strs)
        pfx=""
        i=0
        while i <len(word):
            for x in strs:
                if x[i]==word[i]:
                    continue;
                elif len(pfx)==0:
                    return ""
                else:
                    return pfx
            pfx=pfx+word[i]
            i+=1
        return pfx
            
            
        
                
            
