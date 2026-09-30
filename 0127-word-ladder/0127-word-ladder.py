class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = [beginWord]
        visited = {beginWord}
        steps = 1
        head = 0

        while head < len(queue):
            for _ in range(len(queue) - head):
                word = queue[head]
                head += 1

                if word == endWord:
                    return steps

                chars = list(word)

                for i in range(len(chars)):
                    original = chars[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original:
                            continue

                        chars[i] = c
                        new_word = "".join(chars)

                        if new_word in words and new_word not in visited:
                            if new_word == endWord:
                                return steps + 1

                            visited.add(new_word)
                            queue.append(new_word)

                    chars[i] = original

            steps += 1

        return 0
