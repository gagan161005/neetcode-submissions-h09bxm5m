class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # One slot for each letter a-z
            for char in s:
                # Convert char to index (0-25) using ASCII
                count[ord(char) - ord('a')] += 1
            
            # Lists can't be keys in a dict, so convert to a tuple
            ans[tuple(count)].append(s)
            
        return list(ans.values())