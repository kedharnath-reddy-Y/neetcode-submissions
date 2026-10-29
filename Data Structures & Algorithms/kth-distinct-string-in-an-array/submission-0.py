class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        newArr=[]
        freq=dict(Counter(arr))
        for word in freq:
            if freq[word]==1:
                newArr.append(word)
        if len(newArr)<k:
            return ""
        else:
            return newArr[k-1]

        


        