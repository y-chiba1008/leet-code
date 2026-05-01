import random
import statistics
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from main import Solution


def generate_test_case(length: int = 10**3) -> list[int]:
    """
    Container With Most Waterの制約を満たすランダムなテストケースを生成する。
    - 2 <= height.length <= 10^5
    - 0 <= height[i] <= 10^4
    """
    if length < 2:
        length = 2

    return [random.randint(0, 10**4) for _ in range(length)]


def measure_performance(iterations: int, num_points: int = 4) -> pd.DataFrame:
    solution = Solution()
    # O(n^2)の実装であるため、最大サイズを調整（10^3.5 ≒ 3162）
    lengths = np.logspace(1, 3.5, num_points, dtype=int)

    results = []

    for length in lengths:
        times = []
        for _ in range(iterations):
            height = generate_test_case(length)

            start_time = time.perf_counter()
            solution.maxArea(height)
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

    ax.set_title('Container With Most Water Performance', fontsize=15)
    ax.set_xlabel('Input Size (n)', fontsize=12)
    ax.set_ylabel('Execution Time (ms)', fontsize=12)
    ax.legend()

    plt.tight_layout()
    plt.savefig('problems/0011_Container_With_Most_Water/performance_plot.png')
    print(
        'Visualization saved to problems/0011_Container_With_Most_Water/performance_plot.png'
    )


if __name__ == '__main__':
    # O(n^2)の実装を考慮し、繰り返し回数とデータポイントを調整
    df = measure_performance(iterations=5, num_points=10)
    print(df.to_string(index=False))
    visualize_performance(df)
