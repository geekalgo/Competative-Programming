import json
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def sumValue(self, v1, v2, cary):
        sumVal = v1 + v2 + cary
        remndr = 0
        digt = (sumVal % 10)
        if sumVal>=10:
            remndr = (int)(sumVal/10)
        return [digt, remndr]
        
    #l1 is small list l2 is large list
    #linkList is large length linked list To add the result.
    def addTwoList(self, l1, l2, linkList):
        carry = 0
        l1Lenth = len(l1)
        indx = len(l2) - 1
        if l1Lenth == 1:
            if l1[0] == 0:
                return linkList   
        for i in range(l1Lenth-1, -1, -1):
            #print("i={}, indx={}, carry={}".format(i, indx, carry))
            sumVal = self.sumValue(l1[i], l2[indx], carry)
            l2[indx] = sumVal[0]
            carry = sumVal[1]
            indx = indx -1
        if carry:
            for j in range(indx, -1, -1):
                sumVal = self.sumValue(l2[j], carry, 0)
                l2[j] = sumVal[0]
                carry = sumVal[1]
        p1 = linkList
        for i in range(len(l2)-1, -1, -1):
            p1.val = l2[i]
            if p1.next:
                p1 = p1.next
        if carry:
            carObj = ListNode(carry)
            p1.next = carObj
        return linkList
            
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nmbrA = []
        nmbrB = []
        p1 = l1;
        while p1.next:
            nmbrA.append(p1.val)
            p1 = p1.next
        nmbrA.append(p1.val)
        p2 = l2
        while p2.next:
            nmbrB.append(p2.val)
            p2 = p2.next
        nmbrB.append(p2.val)
        l1Lnth = len(nmbrA)
        l2Lnth = len(nmbrB)
        if l1Lnth>l2Lnth:
            return self.addTwoList(nmbrB, nmbrA, l1)
        else:
            return self.addTwoList(nmbrA, nmbrB, l2)

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
