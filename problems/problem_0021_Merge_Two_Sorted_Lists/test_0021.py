import pytest
from .main import ListNode, Solution


def from_list(nums: list[int]) -> ListNode | None:
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for val in nums[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def to_list(head: ListNode | None) -> list[int]:
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums


arg_names = ['list1', 'list2', 'expect']
arg_values = [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
]


@pytest.mark.parametrize(
    argnames=arg_names,
    argvalues=arg_values,
    ids=[f'case_{i}' for i in range(len(arg_values))],
)
def test_normal(list1: list[int], list2: list[int], expect: list[int]):
    solution = Solution()
    l1 = from_list(list1)
    l2 = from_list(list2)
    result = solution.mergeTwoLists(l1, l2)
    assert to_list(result) == expect
