class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in range(len(details)):
            age=""
            for j in range(11,13):
                age+=details[i][j]
            if int(age)>60:
                    count+=1
        return count           
        