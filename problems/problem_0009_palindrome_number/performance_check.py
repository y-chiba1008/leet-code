import random
import statistics
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from main import Solution


def generate_test_case(magnitude: int) -> int:
    """
    Palindrome Numberの制約を満たすランダムなテストケースを生成する。
    - -2^31 <= x <= 2^31 - 1
    magnitude: xの桁数の目安 (10^magnitude)
    """
    if magnitude == 0:
        return random.randint(0, 9)

    lower = 10 ** (magnitude - 1)
    upper = 10**magnitude - 1

    # 上限 2^31 - 1 (2,147,483,647) を超えないように調整
    upper = min(upper, 2**31 - 1)
    if lower > upper:
        lower = upper // 10

    x = random.randint(lower, upper)

    # 負の数も一定の確率で混ぜる
    if random.random() < 0.2:
        x = -x

    return x


def measure_performance(iterations: int, num_points: int = 4) -> pd.DataFrame:
    solution = Solution()
    # 桁数 (10^0 から 10^9 程度まで)
    magnitudes = np.linspace(0, 9, num_points, dtype=int)

    results = []

    for mag in magnitudes:
        times = []
        for _ in range(iterations):
            x = generate_test_case(mag)

            start_time = time.perf_counter()
            solution.isPalindrome(x)
            end_time = time.perf_counter()

            times.append((end_time - start_time) * 1000)  # ms

        results.append(
            {
                'Magnitude (10^n)': mag,
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
        data=df, x='Magnitude (10^n)', y='Avg Time (ms)', marker='o', label='Average Time'
    )

    # 塗りつぶしで最大/最小の範囲を表示
    plt.fill_between(
        df['Magnitude (10^n)'],
        df['Min Time (ms)'],
        df['Max Time (ms)'],
        alpha=0.2,
        label='Min-Max Range',
    )

    ax.set_title('Palindrome Number Algorithm Performance', fontsize=15)
    ax.set_xlabel('Magnitude (Digits)', fontsize=12)
    ax.set_ylabel('Execution Time (ms)', fontsize=12)
    ax.legend()

    plt.tight_layout()
    plt.savefig('problems/0009_palindrome_number/performance_plot.png')
    print('Visualization saved to problems/0009_palindrome_number/performance_plot.png')


if __name__ == '__main__':
    # 測定実行
    df = measure_performance(iterations=100, num_points=10)
    print(df.to_string(index=False))
    visualize_performance(df)
