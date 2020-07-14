class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle = minutes * 6
        h_angle = (hour + (minutes / 60)) * 30
        diff = abs(m_angle - h_angle)
        return min(diff, 360 - diff)


if __name__ == '__main__':
    h, m = 12, 30
    print(f"Input: hour = {h}, minutes = {m}")
    print(f"Output: {Solution().angleClock(h, m)}")
