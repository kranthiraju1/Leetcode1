from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        if beginWord == endWord:
            return 1

        front = {beginWord}
        back = {endWord}
        words.discard(beginWord)
        words.discard(endWord)

        length = 1

        while front and back:
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            length += 1

            for word in front:
                chars = list(word)

                for i in range(len(chars)):
                    original = chars[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original:
                            continue

                        chars[i] = c
                        candidate = "".join(chars)

                        if candidate in back:
                            return length

                        if candidate in words:
                            next_front.add(candidate)
                            words.remove(candidate)

                    chars[i] = original

            front = next_front

        return 0