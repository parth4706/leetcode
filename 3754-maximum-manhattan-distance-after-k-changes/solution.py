class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        up = 0
        down = 0
        right = 0
        left = 0
        result = 0

        for i, c in enumerate(s, 1):
            match c:
                case "N":
                    up += 1
                case "S":
                    down += 1
                case "E":
                    right += 1
                case "W":
                    left += 1
            
            # print(up, down, left, right)
            if up > down:
                # max_dist += up
                min_dist = down
            else:
                # max_dist += down
                min_dist = up
            
            if right > left:
                # max_dist += right
                min_dist += left
            else:
                # max_dist += left
                min_dist += right

            if k >= min_dist:
                if i > result:
                    result = i
            else:
                dist = i - 2 * (min_dist - k)
                if dist > result:
                    result = dist
            
        return result
