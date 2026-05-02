import pytest
from .main import Solution

arg_names = ['height', 'expect']
arg_values = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
]


@pytest.mark.parametrize(
    argnames=arg_names,
    argvalues=arg_values,
    ids=[f'case_{i}' for i in range(len(arg_values))],
)
def test_normal(height: list[int], expect: int):
    solution = Solution()
    result = solution.maxArea(height)
    assert result == expect
