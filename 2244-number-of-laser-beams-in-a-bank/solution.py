from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        prev = 0  # number of devices in the last non-empty row

        for row in bank:
            devices = row.count('1')
            if devices > 0:
                count += prev * devices
                prev = devices  # update for next non-empty row

        return count
