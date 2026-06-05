class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        write_pos = len(nums1) - 1

        p1 = m - 1 #last real for n1
        p2 = n - 1 #last real for n2


        # loop backwards from p2
        while p2 >= 0:
            
            # if last real for n1 > n2 -> write n1, decrement
            # only if p1 is not exhausted
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write_pos] = nums1[p1]
                p1 -= 1
            
            # if p1 is exhausted or nums2 back is greater
            else:
                nums1[write_pos] = nums2[p2]
                p2 -= 1
            write_pos -=1


                
                




    
        

