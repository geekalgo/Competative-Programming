class Solution:
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        to_return = ""
        for x in str1:
            if x==" " and len(to_return) == 0:
                pass
            elif x.isdigit():
                to_return = to_return + x
            else:
                if len(to_return) == 0:
                    if x in ["+", "-"]:
                        to_return = to_return + x
                    else:
                        return 0
                else:
                    break
        
        if len(to_return) == 0 or to_return in ["+", "-"]:
            return 0
        
        int_to_return = int(to_return)
        
        if -(2**31)<=int_to_return <=(2**31 -1):
            return int_to_return
        elif int_to_return>=(2**31 -1):
            return (2**31 -1)
        else:
            return -(2**31)

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
            str = stringToString(line);
            
            ret = Solution().myAtoi(str)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
