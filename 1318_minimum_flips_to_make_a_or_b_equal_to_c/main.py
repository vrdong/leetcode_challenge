class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bin = format(a, 'b')
        b_bin = format(b, 'b')
        c_bin = format(c, 'b')

        if len(a_bin) < len(b_bin):
            a_bin, b_bin = b_bin, a_bin

        max_len = max(len(a_bin), len(b_bin), len(c_bin))
        print(a_bin, b_bin, c_bin)
        # print(max_len)

        while len(a_bin) < max_len:
            a_bin = '0' + a_bin
        while len(b_bin) < max_len:
            b_bin = '0' + b_bin
        while len(c_bin) < max_len:
            c_bin = '0' + c_bin

        #  1 1 => 1
        #  1 0 => 1
        #  0 1 => 1
        #  0 0 => 0
        count = 0
        for i in range(max_len):
            if c_bin[i] == '0':
                if a_bin[i] == '1':
                    count += 1
                if b_bin[i] == '1':
                    count += 1
            else:
                if a_bin[i] == b_bin[i] == '0':
                    count += 1
        return count


print(Solution().minFlips(1, 2, 3))
# 1 0 0
# 0 1 0
# 1 1 1
