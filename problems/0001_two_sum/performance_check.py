import random
import statistics
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from main import Solution


def generate_test_case(length: int = 10**4) -> tuple[list[int], int]:
    """
    Two Sumの制約を満たすランダムなテストケースを生成する。
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - 解は必ず1つだけ存在する
    """
    if length < 2:
        length = 2

    # 1. 確実に解となる2つの数を選択
    val1 = random.randint(-5 * 10**8, 5 * 10**8)
    val2 = random.randint(-5 * 10**8, 5 * 10**8)
    target = val1 + val2

    nums = [val1, val2]
    seen = {val1, val2}

    # 2. 残りの要素を埋める（他のペアがtargetにならないように制御）
    while len(nums) < length:
        x = random.randint(-(10**9), 10**9)

        if x not in seen and (target - x) not in seen:
            nums.append(x)
            seen.add(x)

    random.shuffle(nums)
    return nums, target


def measure_performance(iterations: int, num_points: int = 4) -> pd.DataFrame:
    solution = Solution()
    lengths = np.logspace(1, 4, num_points, dtype=int)

    results = []

    for length in lengths:
        times = []
        for _ in range(iterations):
            nums, target = generate_test_case(length)

            start_time = time.perf_counter()
            solution.twoSum(nums, target)
            end_time = time.perf_counter()

            times.append((end_time - start_time) * 1000)  # ms

        results.append(
            {
                'Length': length,
                'Avg Time (ms)': statistics.mean(times),
                'Max Time (ms)': max(times),
                'Min Time (ms)': min(times),
                'Std Dev': statistics.stdev(times) if len(times) > 1 else 0,
            }
        )

    return pd.DataFrame(results)


def visualize_performance(df: pd.DataFrame):
    """
    Performanceの結果をseabornで可視化し、画像として保存する。
    """
    sns.set_theme(style='whitegrid')
    plt.figure(figsize=(10, 6))

    # 実行時間の推移をプロット
    ax = sns.lineplot(
        data=df, x='Length', y='Avg Time (ms)', marker='o', label='Average Time'
    )

    # 塗りつぶしで最大/最小の範囲を表示
    plt.fill_between(
        df['Length'],
        df['Min Time (ms)'],
        df['Max Time (ms)'],
        alpha=0.2,
        label='Min-Max Range',
    )

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title('Two Sum Algorithm Performance', fontsize=15)
    ax.set_xlabel('Input Size (n)', fontsize=12)
    ax.set_ylabel('Execution Time (ms)', fontsize=12)
    ax.legend()

    plt.tight_layout()
    plt.savefig('problems/0001_two_sum/performance_plot.png')
    print('Visualization saved to problems/0001_two_sum/performance_plot.png')


if __name__ == '__main__':
    df = measure_performance(iterations=30, num_points=20)
    print(df.to_string(index=False))
    visualize_performance(df)
