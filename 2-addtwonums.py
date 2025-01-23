# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

"""


    @type  l1: ListNode[]
    @param l1: Linked list which represents a number in reverse
    @type  l2: ListNode[]
    @param l2: Linked list which represents a number in reverse
    @rtype:   ListNode[]
    @return:  Linked list which represents the sum of l1 and l2 number in reverse


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def __init__(self):
        pass

    # Time Taken (45 Mins) Debugging (15 Mins)
    # def addTwoNumbers(self, l1, l2):
    #     carryFlag = False

    #     l1Pointer = l1
    #     l2Pointer = l2

    #     returnList = None
    #     returnListPointer = None

    #     firstNodeVal = l1Pointer.val + l2Pointer.val
    #     if (firstNodeVal >= 10):
    #         carryFlag = True
    #         firstNodeVal -=10
    #     returnList = ListNode(val = firstNodeVal)
        
    #     returnListPointer = returnList

    #     if l1Pointer != None:
    #         l1Pointer = l1Pointer.next
    #     if l2Pointer != None:
    #         l2Pointer = l2Pointer.next

    #     while l1Pointer != None or l2Pointer != None or carryFlag:

    #         if (l1Pointer != None and l2Pointer != None):
    #             l1l2Sum = l1Pointer.val + l2Pointer.val + int(carryFlag)
    #             carryFlag = False
    #             if (l1l2Sum >= 10):
    #                 l1l2Sum -= 10
    #                 carryFlag = True
    #             returnListPointer.next = ListNode(val = l1l2Sum)
    #         elif (l1Pointer != None):
    #             l1Sum = l1Pointer.val + int(carryFlag)
    #             carryFlag = False
    #             if (l1Sum >= 10):
    #                 l1Sum -= 10
    #                 carryFlag = True
    #             returnListPointer.next = ListNode(val = l1Sum)
    #         elif (l2Pointer != None):
    #             l2Sum = l2Pointer.val + int(carryFlag)
    #             carryFlag = False
    #             if (l2Sum >= 10):
    #                 l2Sum -= 10
    #                 carryFlag = True
    #             returnListPointer.next = ListNode(val = l2Sum)
    #         elif carryFlag:
    #             returnListPointer.next = ListNode(val = int(carryFlag))
    #             carryFlag = False

    #         returnListPointer = returnListPointer.next

    #         if l1Pointer != None:
    #             l1Pointer = l1Pointer.next
    #         if l2Pointer != None:
    #             l2Pointer = l2Pointer.next
        
    #     return returnList

    # Cleaned up Code (10 Mins)
    def addTwoNumbers(self, l1, l2):

        carryFlag = False

        l1Pointer = l1
        l2Pointer = l2

        returnList = ListNode(0)
        returnListPointer = returnList

        while l1Pointer != None or l2Pointer != None or carryFlag:

            if (l1Pointer != None and l2Pointer != None):
                nodeVal = l1Pointer.val + l2Pointer.val + int(carryFlag)
            elif (l1Pointer != None):
                nodeVal = l1Pointer.val + int(carryFlag)
            elif (l2Pointer != None):
                nodeVal = l2Pointer.val + int(carryFlag)
            elif carryFlag:
                nodeVal = int(carryFlag)

            carryFlag = False
            if (nodeVal >= 10):
                nodeVal -= 10
                carryFlag = True

            returnListPointer.next = ListNode(val = nodeVal)
            returnListPointer = returnListPointer.next

            if l1Pointer != None:
                l1Pointer = l1Pointer.next
            if l2Pointer != None:
                l2Pointer = l2Pointer.next
        
        return returnList.next
    

def testCases():
    testClass = Solution()

    # Test cases are a little cursed
    test1l1= ListNode(2, next=ListNode(val=4, next = ListNode(val=3)))
    test1l2= ListNode(5, next=ListNode(val=6, next = ListNode(val=4)))
    answer = testClass.addTwoNumbers(l1 = test1l1, l2 = test1l2)
    print(str(answer.val) + str(answer.next.val) + str(answer.next.next.val))

    test2l1= ListNode(0)
    test2l2= ListNode(0)
    answer = testClass.addTwoNumbers(l1 = test2l1, l2 = test2l2)
    print(str(answer.val))

    test3l1= ListNode(9, next=ListNode(val=9, next = ListNode(val=9, next = ListNode(val=9 , next= ListNode(val=9, next = ListNode(val=9, next= ListNode(val=9, next = ListNode(val=9))))))))
    test3l2= ListNode(9, next=ListNode(val=9, next = ListNode(val=9, next = ListNode(val=9))))
    answer = testClass.addTwoNumbers(l1 = test3l1, l2 = test3l2)
    print(str(answer.val) + str(answer.next.val) + str(answer.next.next.val) + str(answer.next.next.next.val) + str(answer.next.next.next.next.val) + str(answer.next.next.next.next.next.val) + str(answer.next.next.next.next.next.next.val) + str(answer.next.next.next.next.next.next.next.val)+ str(answer.next.next.next.next.next.next.next.next.val))
    
    #Expected output:
    # 708
    # 0
    # 899900001
testCases()
    