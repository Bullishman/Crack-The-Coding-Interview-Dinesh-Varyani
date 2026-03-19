class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Helper function to expand from a center and find the longest palindrome.
        def expand(l: int, r: int) -> str:
            # Expand as long as pointers are in bounds and characters match.
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # When the loop ends, l and r are one position outside the palindrome.
            # Return the slice s[l+1:r] to get the actual palindrome.
            return s[l + 1:r]
        
        # A quick optimization: if the string is short or already a palindrome, return it.
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # Iterate through every character of the string.
        for i in range(len(s)):
            # Find the longest odd-length palindrome with center at i.
            # Find the longest even-length palindrome with center between i and i+1.
            odd_palindrome, even_palindrome = expand(i, i), expand(i, i + 1)
            
            # Keep the longest string found so far.
            # max() with a key=len correctly compares the strings by their length.
            result = max(result, odd_palindrome, even_palindrome, key=len)
            
        return result