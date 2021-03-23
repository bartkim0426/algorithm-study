# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.stack) == 0 else False


# https://leetcode.com/problems/valid-parentheses/
import re

class Solution:
    def isValid(self, s: str) -> bool:
        # stack에 쌓으면서 매칭이 되는 순간 제거
        stack = ''
        for c in s:
            stack += c
            stack = re.sub(r'\(\)|\{\}|\[\]', '', stack)
        return stack == ''

# string 말고 stack으로 풀기
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        for c in s:
            # 비교해야될 텍스트가 있으면
            if c in ['}', ']', ')']:
                try:
                    last = stack.pop()
                except IndexError:
                    last = ''
                # 마지막 값이 매칭되지 않으면 false
                if d[c] != last:
                    return False
            # 없으면 그냥 stack에 추가
            else:
                stack.append(c)
        return not stack


# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
from collections import Counter
        
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        방법1: set(s)를 만들어 해당 s*k 만큼 있는걸 연속적으로 제거 -> 재귀로 가능할까?
        
        방법2: using stack
        stack에 넣다가 k개가 되는 순간 제거 -> time limit 이 걸림
        '''
        # 우선 k만큼 있는게 없으면 그냥 s 반환
        if max(Counter(s).values()) < k:
            return s
        
        stack = []
        for c in s:
            # stack에 개수가 k-1개 이하면 무조건 넣기
            if len(stack) < k-1:
                stack.append(c)
                continue
                
            # stack에서 값을 k개수만큼 빼고 순서대로 tmp에 넣어줌
            # 해당 값이 모두 같으면 넘어감
            # 아니면 c까지 순차적으로 다시 넣기
            tmp = []
            tmp.append(c)
            for i in range(k-1):
                tmp.append(stack.pop())
            tmp.reverse()  # 반대로 들어가니깐 바꿔줌
            # c도 넣어줌
            # 모든 값이 같으면 pass
            if len(set(tmp)) == 1:
                continue
            # 다르면 다시 쭉 넣어줌
            for x in tmp:
                stack.append(x)
        return ''.join(stack)


from collections import Counter
        
# 2번째 for문이 아니라 slicing으로 풀어도 exceed
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            # stack에 개수가 k-1개 이하면 무조건 넣기
            if len(stack) < k-1:
                stack.append(c)
                continue
            # for문이 아니고 slicing으로 제거
            # stack의 마지막부터 k-1까지
            # 무조건 넣고 시작
            n = len(stack)
            stack.append(c)
            tmp = stack[n-k:]
            
            # 모든 값이 같으면 pass
            if len(set(tmp)) == 1:
                # 같으면 빼줌
                stack = stack[:n-k]
                continue
                
        return ''.join(stack)

# 처음에 생각헀던 방법 (string set에서 제거하는 방법)으로 풀어봄
# 이거 말고 stack으로 푸는 방법을 알고싶음
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # 다시 방법1로 풀어봄
        # 미리 제거
        # set을 만들고 제거해봄
        sets = set(s)
        ss = [c*k for c in sets]
        
        # 지워야할 애들을 먼저 지움
        def delete_duplicate(x, s):
            return s.replace(x, '')
            
        while True:
            original = s
            for x in ss:
                if x in s:
                    s = delete_duplicate(x, s)
            if original == s:
                return original
