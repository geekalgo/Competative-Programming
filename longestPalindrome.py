class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        strLnth = len(s)
        if strLnth <= 0:
            return ""
        
        strt = 0
        end  = 0
        
        for i in range(strLnth):
            ln1 = self.expandCenter(s, i, i)
            ln2 = self.expandCenter(s, i, i+1)
            lnth = max(ln1, ln2)
            if lnth > end - strt:
                strt = i - ((lnth - 1)//2)
                end  = i + (lnth//2)
        return s[strt:end+1]
            
    def expandCenter(self, s, L, R):
        strt = L
        end  = R
        lnth = len(s)
        while strt>=0 and end<lnth and s[strt] == s[end]:
            strt = strt - 1
            end  = end  + 1
        return end - strt -1

def stringToString(input):
    import json

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
            s = stringToString(line);
            
            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
