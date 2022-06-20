class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        print(words)
        s = ""
        for word in words:
            if word+'#' not in s:
                s += word+'#'
        print(s)
        return len(s)