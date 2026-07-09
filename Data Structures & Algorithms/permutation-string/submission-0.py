from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False  # Base case: s1 can't fit in s2
            
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        
        # Step 1: Initialize the maps for the first window of size len(s1)
        for i in range(n1):
            count1[s1[i]] += 1
            count2[s2[i]] += 1
            
        if count1 == count2:
            return True
            
        # Step 2: Slide the fixed window across the rest of s2
        for r in range(n1, n2):
            # Add the new character entering the right side of the window
            count2[s2[r]] += 1
            
            # Remove the old character leaving the left side of the window
            l = r - n1
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]  # Clean up empty keys so comparison works perfectly
                
            # Check if our sliding window matches s1's profile
            if count1 == count2:
                return True
                
        return False