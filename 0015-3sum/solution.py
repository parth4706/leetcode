class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        count = {}
        unique = []
        
        for num in nums:
            if num not in count:
                count[num] = 1
                unique.append(num)
            elif count[num] < 3:
                count[num] += 1

        result = []
        u = len(unique)
        
        for i in range(u):
            a = unique[i]

            if a > 0:
                break
            
            if a == 0:
                if count[0] >= 3:
                    result.append([0, 0, 0])
                break  

            for j in range(i, u):
                b = unique[j]
                c = -(a + b)
                
                if c < b:
                    break
            
                if c in count:
                    if a == b and count[a] < 2:
                        continue
                    if b == c and count[b] < 2:
                        continue 
                    if a <= b <= c:
                        result.append([a, b, c])
        
        return result
