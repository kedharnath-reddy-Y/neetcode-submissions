class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        res=[]
        
        for i in words:
            for j in range(len(words)):

                if i != words[j] and i in words[j]:
                    if i not in res:
                        res.append(i)
        return res