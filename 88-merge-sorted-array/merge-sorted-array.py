class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        del nums1[m:(m+n)]

        if len(nums2):
            pt1 = 0
            pt2 = 0

            while pt2 != len(nums2):

                if pt1 == len(nums1):
                    nums1.append(nums2[pt2])
                    pt2 += 1
                elif nums2[pt2] > nums1[pt1]:
                    pt1 += 1
                elif nums2[pt2] <= nums1[pt1]:
                    nums1.insert(pt1, nums2[pt2])
                    pt2 += 1            