import pytest
from .main import Solution

arg_names = ['nums', 'target', 'expect']
arg_values = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize(
    argnames=arg_names,
    argvalues=arg_values,
    ids=[f'case_{i}' for i in range(len(arg_values))],
)
def test_normal(nums: list[int], target: int, expect: list[int]):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert sorted(result) == expect
