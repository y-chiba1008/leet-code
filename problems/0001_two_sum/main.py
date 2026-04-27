from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idxs: dict[int, list[int]] = {}
        for idx, val in enumerate(nums):
            if val in val_to_idxs:
                val_to_idxs[val].append(idx)
            else:
                val_to_idxs[val] = [idx]

        nums = sorted(nums)
        idx_small = 0
        idx_large = len(nums) - 1
        while idx_small < idx_large:
            sum_temp = nums[idx_small] + nums[idx_large]
            if sum_temp > target:
                idx_large -= 1
            elif sum_temp < target:
                idx_small += 1
            else:
                break

        val_1 = nums[idx_small]
        val_2 = nums[idx_large]

        idx_1 = val_to_idxs[val_1].pop()
        idx_2 = val_to_idxs[val_2].pop()

        return [idx_1, idx_2]
