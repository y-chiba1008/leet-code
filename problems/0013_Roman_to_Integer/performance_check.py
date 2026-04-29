import random
import statistics
import time

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from main import Solution


def int_to_roman(num: int) -> str:
    """Helper to generate valid Roman numerals."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


# Pre-generate all valid Roman numerals grouped by length
ROMAN_BY_LENGTH = {}
for i in range(1, 4000):
    s = int_to_roman(i)
    length = len(s)
    if length not in ROMAN_BY_LENGTH:
        ROMAN_BY_LENGTH[length] = []
    ROMAN_BY_LENGTH[length].append(s)


def generate_test_case(length: int) -> str:
    """Returns a random Roman numeral of the given length."""
    if length not in ROMAN_BY_LENGTH:
        # Fallback if length not found (shouldn't happen for 1-15)
        return random.choice(ROMAN_BY_LENGTH[min(ROMAN_BY_LENGTH.keys())])
    return random.choice(ROMAN_BY_LENGTH[length])


def measure_performance(iterations: int) -> pd.DataFrame:
    solution = Solution()
    lengths = sorted(ROMAN_BY_LENGTH.keys())

    results = []

    for length in lengths:
        times = []
        for _ in range(iterations):
            s = generate_test_case(length)

            start_time = time.perf_counter()
            solution.romanToInt(s)
            end_time = time.perf_counter()

            times.append((end_time - start_time) * 1000000)  # μs (using microseconds for small inputs)

        results.append(
            {
                'Length': length,
                'Avg Time (μs)': statistics.mean(times),
                'Max Time (μs)': max(times),
                'Min Time (μs)': min(times),
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
        data=df, x='Length', y='Avg Time (μs)', marker='o', label='Average Time'
    )

    # 塗りつぶしで最大/最小の範囲を表示
    plt.fill_between(
        df['Length'],
        df['Min Time (μs)'],
        df['Max Time (μs)'],
        alpha=0.2,
        label='Min-Max Range',
    )

    ax.set_title('Roman to Integer Algorithm Performance', fontsize=15)
    ax.set_xlabel('String Length', fontsize=12)
    ax.set_ylabel('Execution Time (μs)', fontsize=12)
    ax.legend()

    plt.tight_layout()
    plt.savefig('problems/0013_Roman_to_Integer/performance_plot.png')
    print('Visualization saved to problems/0013_Roman_to_Integer/performance_plot.png')


if __name__ == '__main__':
    # Since the input is very small, we increase iterations for more stable results
    df = measure_performance(iterations=1000)
    print(df.to_string(index=False))
    visualize_performance(df)
