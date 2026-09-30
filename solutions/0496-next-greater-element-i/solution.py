class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        for i in nums1:
            pos=nums2.index(i)
            greater=-1
            for j in range(pos+1,len(nums2)):
                if nums2[j]>i:
                    greater=nums2[j]
                    break
            ans.append(greater)
        return ans

        
