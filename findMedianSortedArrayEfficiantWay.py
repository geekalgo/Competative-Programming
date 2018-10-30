class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1>l2:
            nums1, nums2, l1, l2 = nums2, nums1, l2, l1
        imin = 0
        imax = l1
        halfLen = (l1 + l2 + 1) // 2 
        
        while imin<=imax:
            i = (imin+imax) // 2
            j =  halfLen - i
            if i<l1 and nums1[i]<nums2[j-1]:
                imin = i + 1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    left_val = nums2[j-1]
                elif j == 0:
                    left_val = nums1[i-1]
                else:
                    left_val = max(nums2[j-1], nums1[i-1])
                    
                if (l1+l2)&1:
                    return left_val
                
                if i == l1:
                    right_val = nums2[j]
                elif j == l2:
                    right_val = nums1[i]
                else:
                    right_val = min(nums2[j], nums1[i])
                    
                return (left_val + right_val) / 2.0

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
