class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        flow=set()

        for path in paths:
            flow.add(path[0])
        
        for path in paths:
            if path[1] not in flow:
                return path[1]
