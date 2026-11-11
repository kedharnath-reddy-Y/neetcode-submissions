class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq={}

        for ch in chars:
            freq[ch]=freq.get(ch,0)+1

        total=0

        for word in words:
            freq_word={}
            for ch in word:
                freq_word[ch]=freq_word.get(ch,0)+1

            valid=True

            for ch,count in freq_word.items():
                if freq.get(ch,0)<count:
                    valid=False
                
            if valid:
                total+=len(word)
        return total
        