from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = {val: idx for idx, val in enumerate(nums)}
        for idx, n in enumerate(nums):
            rest = target - n
            if rest in val_to_idx and val_to_idx[rest] != idx:
                return [idx, val_to_idx[rest]]

        return []
