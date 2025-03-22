from typing import List


def findWordsContaining(words: List[str], x: str):
    ind = []
    for i in range(len(words)):
        if x in words[i]:
            ind.append(i)
    return ind

print(findWordsContaining(["leet","code"], "e"))