
'''
838. Push Dominoes
https://leetcode.com/problems/push-dominoes/

There are n dominoes in a line, and we place each domino vertically upright. 
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left. 
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:
dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."

Output: "LL.RR.LLRRLL.."

Constraints:
n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
'''

import math
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        '''
        We calculate force from left to right and right to left
        From left to right 
        If we got R we set force = max = len(dominos)
        If we got L we set force = 0
        If we got . we set force = max(force - 1, 0)
        
        From left to right 
        If we got L we set force = max = len(dominos)
        If we got R we set force = 0
        If we got . we set force = max(force - 1, 0)
        
        We compare force from left and from right
        If force_left > force_right, It got a L
        If force_left < force_right, It got a R
        If force_left = force_right, It got a .

        '''
        MAX_INT = pow(10, 5)
        right_push = []
        force = 0
        for c in dominoes:
            if c == 'R':
                force = MAX_INT
            elif c == 'L':
                force = 0
            else:
                if force != 0:
                    force -= 1
            right_push.append(force)

        left_push = []
        for idx in range(len(dominoes) - 1, -1, -1):
            if dominoes[idx] == 'L':
                force = MAX_INT
            elif dominoes[idx] == 'R':
                force = 0
            else:
                if force != 0:
                    force -= 1
            left_push.append(force)
        left_push = left_push[::-1]

        result = ''
        for idx in range(len(dominoes)):
            if right_push[idx] > left_push[idx]:
                result += 'R'
            elif right_push[idx] < left_push[idx]:
                result += 'L'
            else:
                result += '.'

        return result


Solution().pushDominoes('.L.R...LR..L..')
