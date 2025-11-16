class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2:
            nums1.extend(nums2)
        c = nums1.count(0)
        for i in range(len(nums2)):
            nums1.remove(0)
        nums1.sort()
