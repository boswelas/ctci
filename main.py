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
        """There are three types of edits that can be performed on strings: insert a character, remove
        a character, or replace a character. Given two strings, write a function to check if they are 
        one edit (or zero edits) away"""
        if len(s1) == len(s2):
            difference = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    difference+=1
                    if difference > 1:
                        return False
            return True
        
        # need to finish this part :)
        elif len(s1) - len(s2) == 1:
            return True
        
        elif len(s2) - len(s1) == 1:
            return True
        
        return False
                    
        
                
            

solution = Solution()
s1 = "pale"
s2 = "pise"
test1 = solution.one_away(s1, s2)
print(test1)
