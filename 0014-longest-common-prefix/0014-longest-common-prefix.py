class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = sorted(strs) # if we sort it we only need to check first and last one
        print(strs)

        ans = ''
        for char in strs[0]:
            if strs[-1].startswith(ans + char):
                ans += char
            else:
                break
        return ans



