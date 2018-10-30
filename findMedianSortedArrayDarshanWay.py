class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 == 0) and (l2 == 0):
            return None
        if l1 == 0:
            center = (int) (l2 / 2)
            if not l2&1:
                if l2 == 1:
                    return nums2[0]
                else:
                    return (sum(nums2[center-1:center+1])/2.0)
            else:
                return nums2[center]
            
        if l2 == 0:
            center = (int) (l1 / 2)
            if not l1&1:
                if l1 == 1:
                    return nums1[0]
                else:
                    return (sum(nums1[center-1:center+1])/2.0)
            else:
                return nums1[center]
        sumLength = l1 + l2
        center = (int)(sumLength/2)
        i = 0
        j = 0
        lnth = -1
        fiSt = False
        num1 = 0
        num2 = 0
        while (i<l1) and (j<l2):
            v1 = nums1[i]
            v2 = nums2[j]
            if v1<v2:
                temp = num1
                num1 = v1
                num2 = temp
                i = i + 1
                lnth = lnth + 1
                fiSt = True
            else:
                temp = num1
                num1 = v2
                num2 = temp
                j = j + 1
                lnth = lnth + 1
                fiSt = False
            if lnth == center:
                if not sumLength&1:
                    return ((num1 + num2) / 2.0)
                else:
                    return num1
                
        while i<l1:
            if lnth == center:
                if not sumLength&1:
                    return ((num1 + num2) / 2.0)
                else:
                    return num1
            lnth = lnth + 1
            temp = num1
            num1 = nums1[i]
            num2 = temp
            i = i+1
         
        while j<l2:
            if lnth == center:
                if not sumLength&1:
                    return ((num1 + num2) / 2.0)
                else:
                    return num1
            lnth = lnth + 1
            temp = num1
            num1 = nums2[j]
            num2 = temp
            j = j + 1
        if not sumLength&1:
            return ((num1+num2)/2.0)
        else:
            return num1

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
