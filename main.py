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
        
                   
                
            

solution = Solution()
s1 = "waterbottle"
s2 = "erbottlewat"
test1 = solution.string_rotation(s1, s2)
print(test1)
