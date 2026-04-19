# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split()
        return " ".join(s_list[::-1])
        # edge case
            # trailing spaces
            # multiple spaces between words
        # example
            # "   the sky is     blue  "
