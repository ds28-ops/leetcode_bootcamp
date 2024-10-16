class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize the result list
        result = []
        # Lengths of s and p
        len_s, len_p = len(s), len(p)
        
        # Early return if p is longer than s
        if len_p > len_s:
            return result
        
        # Create frequency counters for p and the initial window in s
        p_count = Counter(p)
        window_count = Counter(s[:len_p])
        
        # Check if the initial window is an anagram
        if p_count == window_count:
            result.append(0)
        
        # Slide the window across s
        for i in range(len_p, len_s):
            # Add the new character to the window
            window_count[s[i]] += 1
            # Remove the character that is no longer in the window
            window_count[s[i - len_p]] -= 1
            
            # Clean up the counter to remove keys with zero count
            if window_count[s[i - len_p]] == 0:
                del window_count[s[i - len_p]]
            
            # Check if the current window is an anagram
            if window_count == p_count:
                result.append(i - len_p + 1)
        
        return result
