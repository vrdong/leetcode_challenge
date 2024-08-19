from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        
        list_char = list(c.items())
        list_char.sort(key=lambda x:x[1], reverse=True)
        total_press = 0
        for i in range(len(list_char)):
            total_press += list_char[i][1] * (i // 8 + 1)
        # print(total_press)

Solution().minimumPushes("aabbccddeeffgghhiiiiii")