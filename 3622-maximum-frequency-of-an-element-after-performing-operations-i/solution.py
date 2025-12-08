class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxVal = max(nums) + 1
        maxFreq = 0
        freq = [0] * maxVal
        for num in nums:
            freq[num] += 1
        
        curr = sum(freq[:k])
        prev = 0
        increment = 0

        for target in range(maxVal):
            curr -= freq[target]
            if target < maxVal - k:
                curr += freq[target + k]
            if target > 0:
                prev += freq[target - 1]
            if target > k + 1:
                prev -= freq[target - k - 1]
            
            if curr + prev < numOperations:
                increment = curr + prev
            else:
                increment = numOperations
            
            if freq[target] + increment > maxFreq:
                maxFreq = freq[target] + increment
        
        return maxFreq
