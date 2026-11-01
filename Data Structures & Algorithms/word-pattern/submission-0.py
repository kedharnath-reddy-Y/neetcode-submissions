class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(word)!=len(pattern):
            return False
        mapping={}
        used=set()
        for i in range(len(pattern)):
            ch=pattern[i]
            w=word[i]
            if ch in mapping:
                if mapping[ch]!=w:
                    return False
            else:
                if w in used:
                    return False
                used.add(w)
                mapping[ch]=w
        return True

        


        