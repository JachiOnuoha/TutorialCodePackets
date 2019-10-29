# Reversing a Linked List in one-pass
# Lightning Code
# Created by Jachimike Onuoha.
# Copyright © 2019 Jachimike Onuoha. All rights reserved.


# Node Class definition
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class definition
class LList:
    def __init__(self):
        self.head = None


# Node creation
first = node(1)
second = node(2)
third = node(3)
myList = LList()
myList.head = first
first.next = second
second.next = third
third.next = node(4)
third.next.next = node(5)


def Reverse(list):
    # Initialize pointers
    prev = None
    curr = list.head

    # Iterate over linked list until curr pointer hits None thus
    # signifying the end of the Linked List
    while curr:
        # next pointer points to the node after the current node
        next = curr.next
        # curr.next pointer of curr node points to previous node
        curr.next = prev
        # Previous node pointer points to curr node
        prev = curr
        # curr node pointer points to the node after it
        curr = next

    # After completing reversal, the previous pointer is now the new head of the List
    # since it is at the very last node which has now become the first node
    list.head = prev
    printLList(list)


# This is driver code to print the Linked List
def printLList(list):
    string = " "
    p = list.head
    while p is not None:
        string = string + str(p.data)
        p = p.next
    print(string)


printLList(myList)
Reverse(myList)
