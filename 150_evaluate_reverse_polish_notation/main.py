from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = deque()
        
        for token in tokens:
            print(queue)
            if token not in ['+', '-', '*', '/']:
                queue.append(int(token))
                continue

            second_element = queue.pop()
            first_element = queue.pop()

            if token == '+':
                queue.append(first_element + second_element)
                continue

            if token == '-':
                queue.append(first_element - second_element)
                continue

            if token == '*':
                queue.append(first_element * second_element)
                continue

            if token == '/':
                queue.append(int(first_element / second_element))
                continue

        return queue.pop()


s = Solution()
print(s.evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(s.evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
