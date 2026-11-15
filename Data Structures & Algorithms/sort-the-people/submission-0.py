class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        freq={}
        ans=[]
        for i in range(len(names)):
            freq[heights[i]]=names[i]
        sorted_heights=sorted(freq.keys(),reverse=True)
        for h in sorted_heights:
            ans.append(freq[h])
        return ans

        