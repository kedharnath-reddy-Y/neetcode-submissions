class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransome={}
        for ch in ransomNote:
            freq_ransome[ch]=freq_ransome.get(ch,0)+1
        freq_mag={}
        for ch in magazine:
            freq_mag[ch]=freq_mag.get(ch,0)+1
        for ch,count in freq_ransome.items():
            if freq_mag.get(ch,0)<count:
                return False
        return True

        
        