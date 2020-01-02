# def char_in_string(s, ch):
#     count = 0
#     for i in s:
#         if i == ch:
#             count +=1
#     return count


# print(char_in_string("string string", "s"))


# txt = "welcome    to the jungle"

# x = txt.split()

# print(x)


# class Solution:
#     def shortestDistance(self, words, word1, word2):
#         ix1, ix2 = len(words), len(words)
#         minDistance = len(words)
#         for ix, word in enumerate(words):
#             if word == word1:
#                 ix1 = ix
#                 minDistance = min(minDistance, abs(ix1-ix2))
#             elif word == word2:
#                 ix2 = ix
#                 minDistance = min(minDistance, abs(ix1-ix2))
#         return minDistance

# solution = Solution()
# minDistance = solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],
#                             "coding",
#                             "practice")
# print(minDistance)


mystr = "abcabcabd"

print(mystr.count("abc"))


def count_substr(strA, substr):
    return strA.count(substr)

    count = 0 
    flag = True
    start = 0
    while flag:
        if substr in strA[start:]:
            count += 1
            start += len(substr)
        else:
            flag = False 
    return count

print(count_substr(mystr, "ab"))