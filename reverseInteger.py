import sys
class Solution:        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INTMAX = 2**31 - 1
        INTMIN = -2**31
        
        if x>=INTMAX or x<=INTMIN:
            return 0
        
        result = 0
        isnegative = 1
        
        if x<0:
            isnegative = isnegative * -1
            x = abs(x)
        result = int(str(x)[::-1]) * isnegative
        if result>INTMAX or result<INTMIN:
            result = 0
        return result

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
            x = int(line);
            
            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
