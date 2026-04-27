import pytest
from main import Solution


@pytest.mark.parametrize(
    'nums, target, expect',
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_normal(nums: list[int], target: int, expect: list[int]):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert sorted(result) == expect
