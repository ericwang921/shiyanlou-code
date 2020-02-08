# -*- coding: UTF-8 -*-

from data_structure.linked_list import Node
from data_structure.linked_list import Linked_List


def swap_nodes(linkedlist, d1, d2):
    prevD1 = None
    prevD2 = None
    if d1 == d2:
        return
    else:
        D1 = linkedlist.head
        while D1 is not None and D1.data != d1:
            prevD1 = D1
            D1 = D1.next
        D2 = linkedlist.head
        while D2 is not None and D2.data != d2:
            prevD2 = D2
            D2 = D2.next
        if D1 is None and D2 is None:
            return
        if prevD1 is not None:
            prevD1.next = D2
        else:
            linkedlist.head = D2
        if prevD2 is not None:
            prevD2.next = D1
        else:
            linkedlist.head = D1
        temp = D1.next
        D1.next = D2.next
        D2.next = temp

if __name__ == '__main__':
    list1 = Linked_List()
    list1.append(Node(1))
    list1.append(Node(2))
    list1.append(Node(3))
    list1.append(Node(4))
    list1.append(Node(5))
    list1.print_list()
    swap_nodes(list1, 2, 4)
    list1.print_list()
