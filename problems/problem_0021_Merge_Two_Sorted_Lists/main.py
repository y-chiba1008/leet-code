# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def update_nodes(
    head: ListNode | None, curr: ListNode | None, target: ListNode
) -> tuple[ListNode, ListNode, ListNode | None]:
    if head is None or curr is None:
        head = ListNode(target.val)
        curr = head
        return (head, curr, target.next)
    else:
        curr.next = ListNode(target.val)
        curr = curr.next
        return (head, curr, target.next)


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        head = None
        curr = None

        while True:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    head, curr, list1 = update_nodes(head, curr, list1)
                else:
                    head, curr, list2 = update_nodes(head, curr, list2)
            elif list1 is not None and list2 is None:
                head, curr, list1 = update_nodes(head, curr, list1)
            elif list1 is None and list2 is not None:
                head, curr, list2 = update_nodes(head, curr, list2)
            else:
                break

        return head
