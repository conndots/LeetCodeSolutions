from collections import deque

#Time Exceeded

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        ladder_graph = {}
        ladder_graph[beginWord] = self.get_next_diff_one_words(beginWord, wordList)
        for w in wordList:
            ladder_graph[w] = self.get_next_diff_one_words(w, wordList)

        results = []
        min_depth = -1
        queue = deque()
        queue.append((beginWord, [beginWord]))

        while len(queue) != 0:
            w, path = queue.popleft()

            next_words = ladder_graph[w]
            depth = len(path)
            for nw in next_words:
                if nw in path:
                    continue
                if nw == endWord:
                    if (min_depth == -1):
                        min_depth = depth + 1
                    if depth + 1 <= min_depth:
                        min_depth = depth + 1
                        results.append(path + [nw])
                elif min_depth == -1 or depth + 1 <= min_depth:
                    queue.append((nw, path + [nw]))


        return results

    def is_two_words_diff_num_equals(self, w0, w1, diff_num):
        num = 0
        for i in range(0, len(w0)):
            if w0[i] != w1[i]:
                num += 1
                if num > diff_num:
                    return False
        return num == diff_num

    def get_next_diff_one_words(self, curr_word, word_list):
        nexts = []
        for w in word_list:
            if self.is_two_words_diff_num_equals(curr_word, w, 1):
                nexts.append(w)
        return nexts
