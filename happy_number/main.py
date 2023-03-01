from collections import defaultdict


class Solution:
    def isHappy(self, n: int) -> bool:
        dd = defaultdict(bool)
        check_num = n
        while not dd[check_num] and check_num != 1:
            dd[check_num] = True
            new_num = 0
            while check_num != 0:
                new_num += pow(check_num % 10, 2)
                # print(new_num)
                check_num = check_num // 10

            check_num = new_num

        if check_num == 1:
            return True

        return False


Solution().isHappy(2)
