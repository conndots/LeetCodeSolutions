class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None:
            return s

        s = s.strip()

        if len(s) == 0:
            return s

        slist = list(s)

        words = []

        st = 0
        is_space = False
        for idx, ch in enumerate(slist):
            if not is_space and ch == ' ':
                words.append(s[st:idx])
                is_space = True

            elif is_space and ch != ' ':
                st = idx
                is_space = False

        words.append(s[st:])

        words.reverse()
        result = ""
        for word in words:
            result += word
            result += " "

        return result[0:-1]

s = Solution()
print(s.reverseWords("a"))
