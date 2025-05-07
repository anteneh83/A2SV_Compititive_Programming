# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(pos, path):
            if len(path) == 4:
                if pos == len(s):
                    res.append(".".join(path))
                return

            for i in range(1, 4):
                if pos + i > len(s):
                    break

                part = s[pos:pos+i]

                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(pos + i, path + [part])

        backtrack(0, [])
        return res
