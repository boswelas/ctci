from collections import defaultdict


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# Ch 1-2
class Solution:
    
    def isUnique(self, s):
        #O(nlogn)
        """Implement an algorithm to determine if all characters in a string are unique. 
        What if you cannot use additional data structures?"""
        s=''.join(sorted(s))
        print(s)
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False
        return True
    
    def checkPermutation(self, s1, s2):
        #O(nlogn)
        """Given two strings, write a moethod to decide if one is a permutation of the other."""
        if len(s1) != len(s2):
            return False
        
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        if s1 != s2:
            return False
        return True
    
    def checkPermutation2(self, s1, s2):
        #O(n)
        """Given two strings, write a method to decide if one is a permutation of the other."""
        if len(s1) != len(s2):
            return False
        
        # Create a dictionary to count the occurrences of each character in s1
        char_count = {}
        for char in s1:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Decrease the count based on characters in s2
        for char in s2:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
        
        # If all counts are zero, then s1 is a permutation of s2
        return all(count == 0 for count in char_count.values())

    def URLify(self, s, s_len):
        #O(n)
        """Write a method to replace all spaces in a string with '%20'. You may assume that the string
        has sufficient space at the end to hold the additional characters, and that you are given the 
        'true' length of the string. """
        url = []
        for i in range(s_len):
            if s[i] == " ":
                url.append("%20")
            else:
                url.append(s[i])
        return ''.join(url)
    
    def palindrome_permutation(self, s):
        #O(n)
        """Given a string, write a fucntion to check if it a permutation of a palindrome.
        A palindrome is a word or phrase that is the same forwards and backwards. A permutation
        is a rearrangement of letters. The palindrome does not need to be limited to just dictionary
        words. You can ignore casing and non-letter characters."""
        char_dict = {}
        for char in s:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
                
        odd_chars = 0
        
        for key in char_dict:
            value = char_dict[key]
            if value % 2 != 0:
                odd_chars += 1
                
        if odd_chars <= 1:
            return True

        return False
    
    def one_away(self, s1, s2):
        #O(n)
        """There are three types of edits that can be performed on strings: insert a character, remove
        a character, or replace a character. Given two strings, write a function to check if they are 
        one edit (or zero edits) away"""
        
        if abs(len(s1) - len(s2)) > 1:
            return False
        
        if len(s1) == len(s2):
            difference = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    difference+=1
                    if difference > 1:
                        return False
            return True
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
    
        i = 0 
        j = 0  
        difference = 0
        
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                difference += 1
                if difference > 1:
                    return False
                j += 1
            else:
                i += 1
                j += 1
        
        return True
    
    def string_compression(self, s):
        """Implement a method to perform basic string compression using the counts of repeated 
        characters. For example, the string 'aabcccccaaa' would become 'a2b1c5a3'. If the 
        compressed string would not become smaller than the original string, your method should 
        return the original string. You can assume the string has only upper/lowercase letters."""
        return_string = ""
        count = 1
        i = 0
        
        while i < len(s):
            return_string += s[i]
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
                count += 1
                
            return_string += str(count)
            count = 1
            i += 1
            
            if len(return_string) > len(s):
                return s
            
        
        return return_string if len(return_string) < len(s) else s
    
    def rotate_matrix(self, matrix):
        #O(n^2)
        """Given an image represented by an NxN matrix, where each pixel in the image is
        represented by an integer, write a method to rotate the image by 90 degrees. Can you
        do this in place?"""
        l = 0
        r = len(matrix) - 1
        while l < r:
            for i in range(r - l):
                t, b = l, r
                #top left
                curr = matrix[t][l + i]
                next = matrix[t + i][r]
                matrix[t + i][r] = curr
                curr = next
                #top right
                next = matrix[b][r - i]
                matrix[b][r - i] = curr
                curr = next
                #bottom right
                next = matrix[b - i][l]
                matrix[b - i][l] = curr
                curr = next
                #bottom left
                matrix[t][l + i] = curr
                
            r -= 1
            l += 1
        return matrix
    
    def zero_matrix(self, matrix):
        #O(M×N)
        """Write an algorithm such that if an element in an MxN matrix is 0, its entire row
        and column are set to 0"""
        m, n = len(matrix), len(matrix[0])
        row,col = [1]*m, [1]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        
        for i in range(m):
            if row[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(n):
            if col[j] == 0:
                for i in range(m):
                    matrix[i][j]= 0
                    
        return matrix
    
    def string_rotation(self, s1, s2):
        #O(n)
        """Assume you have a method isSubstring which checks if one word is a substring 
        of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of
        s1 using only one call to isSubstring. (eg 'waterbottle' is a rotation of 'erbottlewat')"""
        
        if len(s1) != len(s2):
            return False
        
        concatenated = s1 + s1
        if s2 in concatenated:
            return True
        else:
            return False
        
    def remove_dups(self, ll):
        """Write code to remove duplicates from an unsorted linked list. How would you solve this 
        problem if a temporary buffer is not allowed?"""
        if not ll.head:
            return

        visited = set()
        current = ll.head
        previous = None

        while current:
            if current.data in visited:
                previous.next = current.next
            else:
                visited.add(current.data)
                previous = current
            current = current.next
        
        return ll
    
    def remove_dups2(self, ll):
        """Write code to remove duplicates from an unsorted linked list. How would you solve this 
        problem if a temporary buffer is not allowed?"""
        if not ll.head:
            return ll

        current = ll.head

        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

        return ll
    
    def return_kth_to_last(self, ll, k):
        """Implement an algorithm to find the kth to last element of a singly linked list."""
        count = 0
        curr = ll.head
        
        while curr:
            curr = curr.next 
            count += 1
        
        if k >= count or k < 0:
            return None
        
        curr = ll.head
        diff = count - k - 1
        while diff > 0:
            curr = curr.next
            diff -= 1
            
        return curr
    
    def delete_middle_node(self, n):
        """Implement an algorithm to delete a node in the middle of it (ie any
        node but the first and last node, not necessarily the exact middle) of a 
        singly linked list, given only access to that node."""
        
        if n is None or n.next is None:
            return None
        
        next_node = n.next
        n.data = next_node.data 
        n.next = next_node.next 
                
        return
    
    def partition(self, ll, n):
        """ Write code to partition a linked list around a value x, such that all
        nodes less than x come before all nodes greater than or equal to x. 
        Important: the partition element x can appear anywhere in the 'right 
        partition'; it does not need to appear between the left and right
        partitions. The additional spacing the example below indicates the partition"""
        if not ll.head or ll.head.next is None:
            return
        
        r, l = None, None

        if ll.head.data < n:
            l = ll.head
            while l.next and l.next.data < n:
                l = l.next
            r = l.next 
        else:
            r = ll.head
            l = ll.head
            while l.next and l.next.data >= n:
                l = l.next
            if l.next is None:
                return
            curr = l.next 
            r.next = curr.next 
            curr.next = ll.head
            ll.head = curr 
            l = curr
        
        
        while r and r.next:
            if r.next.data >= n:
                r = r.next 
            else:
                curr = r.next 
                r.next = curr.next
                l.next = curr 
                curr.next = r 
                l = curr

        return 
    
    def sum_lists_backward(self, ll1, ll2):
        """You have two numbers represented by a linked list, where each node contains a
        single digit. The digits are stored in reverse order, such that the 1's digit is at
        the head of the list. Write a function that adds the two numbers and returns the sum 
        as a linked list. (You are not allowed to 'cheat' and just convert the linked list
        to an integer)"""
        p1, p2 = ll1.head, ll2.head
        carry = 0
        result_ll = LinkedList()

        while p1 or p2 or carry:
            val1 = p1.data if p1 else 0
            val2 = p2.data if p2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            result_ll.append(total % 10)

            if p1: p1 = p1.next
            if p2: p2 = p2.next

        return result_ll
         

    def sum_lists_forward(self, ll1, ll2):
        """You have two numbers represented by a linked list, where each node contains a
        single digit. The digits are stored in reverse order, such that the 1's digit is at
        the head of the list. Write a function that adds the two numbers and returns the sum 
        as a linked list. (You are not allowed to 'cheat' and just convert the linked list
        to an integer)"""
        stack1, stack2 = [], []
        
        val = ll1.head        
        
        while val:
            stack1.append(val.data)
            val = val.next 
            
        val = ll2.head
        
        while val:
            stack2.append(val.data)
            val = val.next 
        
        carry = 0
        result_ll = LinkedList()

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            node = Node(total % 10)
            node.next = result_ll.head
            result_ll.head = node

        return result_ll
    
    def palindrome(self, ll):
        """Implement a function to check if a linked list is a palindrome"""
        
        if ll.head is None:
            return True
        
        stack = []
        
        for node in ll:
            stack.append(node.data)
        
            
        reversed_ll = LinkedList()
        while stack:
            reversed_ll.append(stack.pop())
            
        node1 = ll.head
        node2 = reversed_ll.head
        
        while node1 and node2:
            if node1.data != node2.data:
                return False
            node1 = node1.next 
            node2 = node2.next 
        
        return True
    
    def intersection(self, ll1, ll2):
        """Given two linked lists, determine if the two lists intersect. Return the 
        intersecting node. Note that the intersection is defined based on reference, 
        not value. That is, if the kth node of the first linked list is the exact same
        node (by ref) as the jth node in the second linked list, then they are intersecting."""
        if not ll1.head or not ll2.head:
            return None

        stack1 = []
        stack2 = []
        
        curr = ll1.head
        while curr:
            stack1.append(curr)
            curr = curr.next

        curr = ll2.head
        while curr:
            stack2.append(curr)
            curr = curr.next 
        
        
        intersect = None
        
        while stack1 and stack2:
            v1 = stack1.pop()
            v2 = stack2.pop()
            if v1 == v2:
                intersect = v1
            else:
                return intersect
        
        return intersect
    
    def loop_detection(self, head):
        """Given a linked list which might contain a loop, implement an algorithm that
        returns the node at the beginning of the loop (if one exists)"""
        
        if not head or not head.next:
            return
        visited = set()
        node = head
        while node.next:
            if node not in visited:
                visited.add(node)
                node = node.next
            else:
                return node
        return 
    
    def loop_detection_optimized(self, head):
        if not head or not head.next:
            return None
        
        slow = fast = head
        
        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle
        
        # Phase 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

# Ch 3
class Three_In_One:
    """Describe how you could use a single array to implement three stacks"""
    
    def __init__(self, capacity=2, stacks=3):
        length = capacity * stacks
        self.stack = [None] * length
        self.start = [0, length//stacks, (2 * (length//stacks))]
        self.end = [length//stacks - 1, (2 * (length//stacks)) - 1, length -1]
        
    def push(self, stack, value):
        i = self.start[stack]
        while i <= self.end[stack]:
            if self.stack[i]!=None:
                i += 1
            else:
                self.stack[i] = value
                return stack
        return 
        
    
    def pop(self, stack):
        i = self.end[stack]
        while i >= self.start[stack]:
            if self.stack[i] == None:
                i -= 1
            else:
                val = self.stack[i]
                self.stack[i] = None
                return val
        return 
    
    def peek(self, stack):
        i = self.end[stack]
        while i >= self.start[stack]:
            if self.stack[i] == None:
                i -= 1
            else:
                return self.stack[i]
        return None        
        
    def print_stack(self):
        print(self.stack)

class Min_Stack:
    
    def __init__(self):
        self.stack = []
        self.minVal = []
        
    def push(self, val):
        self.stack.append(val)
        if len(self.minVal) == 0 or val <= self.minVal[-1]:
            self.minVal.append(val)
        return self.stack
    
    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.minVal[-1]:
            self.minVal.pop()
        return self.stack
    
    def get_min(self):
        if not self.minVal:
            return None
        return self.minVal[-1]

class Stack_of_Plates:
    
    def __init__(self, cap=2):
        self.max_capacity = cap
        self.stacks = [[]]
        self.number_of_stacks = 1
        
    def return_stacks(self):
        return self.stacks
    
    def push(self, val):
        if len(self.stacks[-1]) < self.max_capacity:
            self.stacks[-1].append(val)
        else:
            self.stacks.append([])
            self.number_of_stacks += 1
            self.stacks[-1].append(val)
        return self.stacks[-1]
    
    def pop(self):
        if self.stacks[-1]:
            self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0 and len(self.stacks) >1:
                self.stacks.pop()
        return self.stacks[-1] 
    
    def pop_at(self, stack, index):
        
        if stack >= self.number_of_stacks or index >= self.max_capacity:
            return None
        
        if self.stacks[stack][index]:
            i = stack
            j = index
            while i < self.number_of_stacks:
                if j+1 < self.max_capacity:
                    #if next val in same stack
                    self.stacks[i][j] = self.stacks[i][j+1]
                    j += 1
                elif j >= self.max_capacity - 1 and i+1 < self.number_of_stacks:
                    #if reached end of stack, need to grab first from next stack
                    self.stacks[i][j] = self.stacks[i+1][0]
                    i += 1
                    j = 0
                elif i == self.number_of_stacks - 1 and self.stacks[i][j] == self.stacks[-1][-1]:
                    #reached the very end of the stacks
                    self.stacks[i].pop()
                    return self.stacks
        return self.stacks
    
class Queue_via_Stacks:
    """Implement a MyQueue class which implements a queue using two stacks"""

    def __init__(self):
        self.queue = []
        self.stack = []

    def return_q_and_s(self):
        print("Queue: ", self.queue)
        print("Stack: ", self.stack)
        return

    def push(self, val):
        self.queue.append(val)
        return 
    
    def pop(self):
        if not self.stack and not self.queue:
            return None
        if not self.stack:
            while len(self.queue) > 0:
                self.stack.append(self.queue.pop())            
        return self.stack.pop()
    
    def peek(self):
        if not self.stack and not self.queue:
            return None
        if not self.stack:
            return self.queue[0]
        return self.stack[-1]
    
    def empty(self):
        return not self.stack and not self.queue
    
class Sorted_Stack:
    """Write a program to sort a stack such that the smallest items are on the top. You can
    use an additional temporary stack, but you may not copy the elements into any other data 
    structure (such as an array). The stack supports the following operations: push, pop, peek,
    and isEmpty"""
    
    def __init__(self):
        self.stack = []
        
    def return_stack(self):
        return self.stack
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None
    
    def isEmpty(self):
        return not self.stack
    
    def push(self, val):
        if not self.stack or val <= self.stack[-1]:
            self.stack.append(val)
        else:
            temp = []
            while self.stack and self.stack[-1] < val:
                temp.append(self.stack.pop())
            self.stack.append(val)
            while temp:
                self.stack.append(temp.pop())
        
class Animal_Shelter:
    """An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis.
    People must adopt either the 'oldest' (based on arrival time) of all animals in the shelter,
    or they can select whether they would prefer a dog or a cat (and will receive the oldest 
    animal of that type). Create the data structures to maintain that system and implement 
    operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
    LinkedList data structure."""
    
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.count = 0       
    
    def return_animals(self):
        print("cat: ", self.cats)
        print("dog: ", self.dogs)
    
    def enqueue(self, type, name):
        self.count += 1
        animal = {"name": name, "order": self.count}
        if type == "cat":
            self.cats.append(animal)
        elif type == "dog":
            self.dogs.append(animal)
        return None
    
    def dequeueDog(self):
        if not self.dogs:
            return None          
        return self.dogs.pop(0)
    
    def dequeueCat(self):
        if not self.cats:
            return None          
        return self.cats.pop(0)
    
    def dequeueAny(self):
        if not self.cats and not self.dogs:
            return None
        elif not self.cats:
            return self.dequeueDog()
        elif not self.dogs:
            return self.dequeueCat()
        if self.cats[0]["order"] < self.dogs[0]["order"]:
            return self.dequeueCat()
        else:
            return self.dequeueDog()

# Ch 4
class DirectedGraph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def printGraph(self):
        print(self.graph)
    
    def bfs(self, start, end):
        """Given a directed graph and two nodes (S and E), design an algorithm to
        find out whether there is a route from S to E"""
        visited = [False] * self.V
        queue = []
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            # Visiting first in queue = checking top nodes first
            current = queue.pop(0)
            if current == end:
                return True
            
            for neighbor in self.graph[current]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor] == True

        return False
    
   
    
    def dfs(self, start, end):
        """Given a directed graph and two nodes (S and E), design an algorithm to
        find out whether there is a route from S to E"""
        visited = [False] * self.V
        stack = [start]
        
        while stack:
            # Visiting last node in stack = continuing down path before checking all top nodes
            current = stack.pop()
            if current == end:
                return True
            if not visited[current]:
                visited[current] = True
                for neighbor in self.graph[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        
        return False

class TreeNode:
    def __init__(self, data=None):
        self.data = data 
        self.l = None
        self.r = None

class MinimalTree:
    """Given a sorted (inc order) array with unique integer elements, write an
    algorithm to create a binary search tree with minimal height"""
    
    def __init__(self, values):
        self.head = self.make_tree(values)
    
        
    def make_tree(self, values):
        if not values:
            return None
        
        mid_index = len(values) // 2
        node = TreeNode(values[mid_index])
        
        node.l = self.make_tree(values[:mid_index])
        node.r = self.make_tree(values[mid_index + 1:])
        
        return node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.l is None:
                node.l = TreeNode(data)
            else:
                self._insert(data, node.l)
        else:
            if node.r is None:
                node.r = TreeNode(data)
            else:
                self._insert(data, node.r)
    
    def to_array(self):
        if self.root is None:
            return []
        queue = [self.root]
        array = []
        while queue:
            node = queue.pop(0)
            array.append(node.data)
            if node.l is not None:
                queue.append(node.l)
            if node.r is not None:
                queue.append(node.r)
        return array
        
    def list_of_depths(self):
        """Given a binary tree, design an algorithm which creates a linked list of all the nodes
        at each depth (e.g. if you have a tree with depth D, you'l have D linked lists)"""
        # heads = []
        queue = []
        count = 1
        
        queue.append(self.root)
        
        while queue:
            i = 0
            ll = LinkedList()
            while i < count and queue:
                current = queue.pop(0)
                if current.l:
                    queue.append(current.l)
                if current.r:
                    queue.append(current.r)
                ll.append(current)
                i += 1
            # heads.append(ll)
            count = count * 2
            
            # for index, linked_list in enumerate(heads):
            #     print(f"Depth {index}: ", end="")
            #     current_node = linked_list.head
            # while current_node:
            #     print(current_node.data.data, end=" -> ")
            #     current_node = current_node.next
            
    def check_balanced(self):
        """Implement a function to check if a binary tree is balanced. For the purpose of 
        this question, a balanced tree is defined to be a tree such that the heights of the two 
        subtrees of any node never differ by more than one."""
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.l), dfs(root.r)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, 1 + max(left[1], right[1])]
        
        root = self.root
        return dfs(root)
            
    def validate_bst(self):
        """Implement a function to check if a binary tree is a binary search tree."""       
        def valid(node, left, right):
            if not node:
                return True
            
            if not node.data < right and node.data > left:
                return False
            
            return (valid(node.l, left, node.data) and 
                    valid(node.r, node.data, right))
            
        node = self.root
        return valid(node, float("-inf"), float("inf"))
    
    def successor(self, node):
        """Write an algorithm to find the 'next' node (ie in-order successor) of a given node 
        in a binary search tree. You may assume that each node has a link to its parent."""
        successor = None
        current = self.root
        
        while current:
            if node.data >= current.data:
                current = current.r
            else:
                successor = current
                current = current.l
                
        return successor.data
            
                    
                
        
        
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)
print(tree.to_array())
# print(tree.successor(3))



