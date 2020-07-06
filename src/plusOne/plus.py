class Solution:
    def plusOne(self, digits: list) -> list:
        return list(map(int, list(str\
            (int("".join(map(str, digits))) + 1))))


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(f"Input: {digits}")
    print(f"Output: {Solution().plusOne(digits)}")
