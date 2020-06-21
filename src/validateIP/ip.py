class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.ipv4(IP):
            return "IPv4"
        if self.ipv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def ipv4(self, IP: str) -> bool:
        groups = IP.split('.')
        if len(groups) != 4:
            return False
        try:
            for g in groups:
                # leading zeroes
                if len(g) != len(str(int(g))):
                    return False
                # number range check
                if int(g) not in range(0, 256):
                    return False
            return True
        except ValueError:
            # if any group contains str which isn't an int base 10
            return False

    def ipv6(self, IP: str) -> bool:
        groups = IP.split(':')
        if len(groups) != 8:
            return False
        try:
            for g in groups:
                if len(g) == 0 or len(g) > 4:
                    return False
                if not g[0].isalpha() and not g[0].isdigit():
                    return False
                # try to convert hex to int
                int(g, base=16)
            return True
        except ValueError:
            # if any group contains str which isn't an int base 16
            return False


if __name__ == '__main__':
    ip = input("Input: ")
    print(f"Output: {Solution().validIPAddress(ip)}")
