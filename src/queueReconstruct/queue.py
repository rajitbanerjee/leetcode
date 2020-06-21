class Solution:
    def reconstructQueue(self, people: list) -> list:
        # sort in ascending order of number of people in front of each person
        people.sort(key=lambda x: x[1])
        # sort in descending order of height
        people.sort(reverse=True, key=lambda x: x[0])
        ans = []
        # rearrange people according to number of people in front of each person
        for p in people:
            ans.insert(p[1], p)
        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(f"Input: {people}")
print(f"Output: {Solution().reconstructQueue(people)}")
