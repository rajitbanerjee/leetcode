class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = ans = 0
        seen = set()

        # sliding window
        while right < len(s):
            if s[right] not in seen:
                # expand to the right
                seen.add(s[right])
                ans = max(ans, len(seen))
                right += 1
            else:
                # contract from the left
                seen.remove(s[left])
                left += 1

        return ans


if __name__ == '__main__':
    s = input("Input: ")
    print(f"Output: {Solution().lengthOfLongestSubstring(s)}")
