class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        p1 = p2 = 0
        ansArray = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                ansArray.append(nums1[p1])
                p1 +=1
            else:
                ansArray.append(nums2[p2])
                p2 +=1
        while p1 < len(nums1):
            ansArray.append(nums1[p1])
            p1 +=1
        while p2 < len(nums2):
            ansArray.append(nums2[p2])
            p2 +=1
        if len(ansArray) % 2 == 0:
            return (ansArray[len(ansArray) // 2] + ansArray[(len(ansArray) // 2) - 1])/2
        else:
            return ansArray[(len(ansArray) // 2)]  