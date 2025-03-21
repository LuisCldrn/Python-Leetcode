def lengthOfLongestSubstring(s: str):
    start = 0
    highest = 0
    unique = set()
    for i in range(len(s)):
        if s[i] not in unique:
            highest = max(highest, i - start +1)
        else: 
            while s[i] in unique:
                unique.remove(s[start])
                start += 1
        unique.add(s[i])
    return highest


lengthOfLongestSubstring(s='abcabcbb')