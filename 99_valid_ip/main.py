from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def is_valid_sub_ip(s):
            if len(s) == 0:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            if int(s) <= 255:
                return True

        def backtrack(s, n, current_ip):
            if n == 1:
                if is_valid_sub_ip(s):
                    current_ip.append(s)
                    result.append('.'.join(current_ip))
                    current_ip.pop()
                return

            sub_ip_len = 1
            while is_valid_sub_ip(s[:sub_ip_len]) and sub_ip_len <= len(s):
  
                current_ip.append(s[:sub_ip_len])
                backtrack(s[sub_ip_len:], n - 1, current_ip)
                current_ip.pop()
                sub_ip_len += 1

        backtrack(s, 4, [])
        return result


print(Solution().restoreIpAddresses('101023'))
