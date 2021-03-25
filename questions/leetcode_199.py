# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
TreeNode{
    val:1,
        left: TreeNode{
            val: 2,
            left: None,
            right: TreeNode{
                val: 5,
                left: None,
                right: None,
            }
        ...
    }
}
'''

# 1차. list라고 생각하고 풀어서
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        # 초반에 root가 list로 잘못 알고 풀어서 실패
        binary tree
        - nodes are incresing with 2**n: 1, 2, 4, 8 ...
        - Get tree length and "n": len(root)
        
        # solution 1: greedy searching
        - for loop for the root and add stack
        - add count for the power of 2 (2**n)
        - if the index is power of 2 -> add to index and make count to 0
        - repeat till the end
        - time complex: O(n) becuase it search all root
        
        # solution 2:
        - return indexs are 0, 2, 6, 14, ... -> 2**n / += 2**(n+1) += 2**(n+2)
        - find all indexes of them
        - and return all from root
        - time complex: O(logn) because it search for power of 2
        
        # solution
        '''
        # solution 2:
        # find largest 2**n number: 
        n = 0
        result = []
        q = [root]
        print(q)
        index = 0
        while True:
            power = 2 ** n
            index =+ 2 ** n
            if index + 1 == len(root):
                break
            result.append(q[index])
        return result

# 2차. root로 풀었는데 실패 -> 이런건 면접관에게 물어볼 수 있으면 물어보면 좋을듯?
 class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        # 초반에 root가 list로 잘못 알고 풀어서 실패
        # root -> TreeNode object
        
        # solution 1: finding right only
        find right treenode till the end
        -> 이 방식으로는 오른쪽게 아닌데 왼쪽에만 있는 경우를 잡지 못함
        ex. [1, 2] -> 2가 왼쪽이 아니고 right side로 취급됨
        '''
        # If no root, return empty list
        if not root:
            return []
        
        result = []
        while True:
            # add first value
            if not result:
                result.append(root.val)
            if not root.right:
                break
            result.append(root.right.val)
            root = root.right
                
        return result
        
# 3차. solution 3으로 풀었는데 마지막 rightest value를 찾지 못해서 실패
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        # 초반에 root가 list로 잘못 알고 풀어서 실패
        # root -> TreeNode object
        
        # solution 1: finding right only
        find right treenode till the end
        -> 이 방식으로는 오른쪽게 아닌데 왼쪽에만 있는 경우를 잡지 못함
        ex. [1, 2] -> 2가 왼쪽이 아니고 right side로 취급됨
        
        # solution 2: greddy
        전체 tree를 모두 읽어서 리스트 형태로 만들고 푸는 방식
        O(n**2) -> 비효율적임
        tree를 한 번 읽어서 바로 처리해야 O(n) 형태가 나옴
        
        # solution 3: read tree and find power of 2
        - read tree sequentially (left -> right -> left-left -> left-right ...)
        - memorize the order (index)
        - if the index is 1, 3, 7, 15 ... (2**n += 2**(n+1) ...)
        - add it to result
        - if end before complete 2**n -> add last tree value
        - O(n) because it read all the nodes
        
        # solution 4: find right tree + if not exist, return left
        - if right tree exits, the whole tree till now must be comopleted
        - if right tree not exits, the tree is ended: add the most rightest value
            - find rightest value: is it impossible without read whole tree??

        # solution 5: find rightest value from all floor
        - add node for specific floor
        - add rightest value to result per floor (last input)
        '''
        # solution 3:
        result = []
        # indexes list
        indexes = []
        index = 0
        # number of nodes in the tree is range [0..100] -> max index will be 2**100
        for i in range(100):
            index += 2**i
            indexes.append(index)
        
        prev = None
        next_node = None
        left = True
        index = 1
        while True:
            # First node
            if index == 1:
                prev = current
                current = root
                left = False
                
            # find next root
            if left:
                current = root.left
                next_node = root.right
            # if right
            else:
                current = root.right
                next_node = 
            nex
            
                
            if index in indexes:
                result.append(current.val)
                
            prev = current
            index += 1

# 5번째 풀이
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        # 초반에 root가 list로 잘못 알고 풀어서 실패
        # root -> TreeNode object
        
        # solution 1: finding right only
        find right treenode till the end
        -> 이 방식으로는 오른쪽게 아닌데 왼쪽에만 있는 경우를 잡지 못함
        ex. [1, 2] -> 2가 왼쪽이 아니고 right side로 취급됨
        
        # solution 2: greddy
        전체 tree를 모두 읽어서 리스트 형태로 만들고 푸는 방식
        O(n**2) -> 비효율적임
        tree를 한 번 읽어서 바로 처리해야 O(n) 형태가 나옴
        
        # solution 3: read tree and find power of 2
        - read tree sequentially (left -> right -> left-left -> left-right ...)
        - memorize the order (index)
        - if the index is 1, 3, 7, 15 ... (2**n += 2**(n+1) ...)
        - add it to result
        - if end before complete 2**n -> add last tree value
        - O(n) because it read all the nodes
        
        # solution 4: find right tree + if not exist, return left
        - if right tree exits, the whole tree till now must be comopleted
        - if right tree not exits, the tree is ended: add the most rightest value
            - find rightest value: is it impossible without read whole tree??

        # solution 5: find rightest value from all floor
        - add node for specific floor
        - add rightest value to result per floor (last input)
        '''
        # solution 5:
        # if no root, return []
        if not root:
            return []
        
        result = []
        
        # create floor with root node
        floor = deque([[root]])
        # loop till the end
        while floor:
            current_floor = floor.popleft()
            print(current_floor)
            
            # append rightest value from the floor -> last value from queue
            result.append(current_floor[-1].val)
            
            next_floor = []
            for node in current_floor:
                # append left -> right to next floor
                if node.left:
                    next_floor.append(node.left)
                if node.right:
                    next_floor.append(node.right)
                    
            # add next_floor to floor
            if next_floor:
                floor.append(next_floor)
            
        return result
