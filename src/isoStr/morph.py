class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = i
            if t[i] not in t_map:
                t_map[t[i]] = i
            if s_map[s[i]] != t_map[t[i]]:
                return False
        return True


if __name__ == '__main__':
    s, t = "egg", "add"
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {Solution().isIsomorphic(s, t)}")
