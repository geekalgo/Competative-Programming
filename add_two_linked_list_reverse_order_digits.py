# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sumValue(self, v1, v2, cary):
        sumVal = v1 + v2 + cary
        remndr = 0
        digt = (sumVal % 10)
        if sumVal>=10:
            remndr = (int)(sumVal/10)
        return [digt, remndr]
        
    def handleNonEqualLength(self, l1, cary):
        p1 = l1
        if cary:
            while l1.next:
                sumVal = self.sumValue(l1.val, 0, cary)
                l1.val = sumVal[0]
                cary = sumVal[1]
                l1 = l1.next
            if cary:
                sumVal = self.sumValue(l1.val, 0, cary)
                l1.val = sumVal[0]
                cary = sumVal[1]
                if cary:
                    l1.next = ListNode(cary)
        return p1
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        cary = 0
        p1 = l1
        while l1.next and l2.next:
            sumVal = self.sumValue(l1.val, l2.val, cary)
            l1.val = sumVal[0]
            cary = sumVal[1]
            l1 = l1.next
            l2 = l2.next
        sumList = self.sumValue(l1.val, l2.val, cary)
        sumT = sumList[0]
        cary = sumList[1]
        l1.val  = sumT
        
        if (not l1.next) and (not l2.next):
            if cary:
                l1.next = ListNode(cary)
        elif l1.next:
            l1 = l1.next
            self.handleNonEqualLength(l1, cary)
        else:
            l2 = l2.next
            l1.next = l2
            l1 = l1.next
            self.handleNonEqualLength(l1, cary)
        return p1

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
