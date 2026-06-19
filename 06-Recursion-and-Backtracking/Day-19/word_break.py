class Solution:
    def wordBreak(self, n, dict_words, s):
        result = []
        word_set = set(dict_words)
        
        def backtrack(index, current_sentence):
            if index == len(s):
                result.append(" ".join(current_sentence))
                return
                
            for i in range(index, len(s)):
                word = s[index:i+1]
                if word in word_set:
                    current_sentence.append(word)
                    backtrack(i + 1, current_sentence)
                    current_sentence.pop()
                    
        backtrack(0, [])
        return result
