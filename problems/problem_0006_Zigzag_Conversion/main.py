class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]

        row_idx = 0
        step = 1
        for char in s:
            zigzag[row_idx].append(char)
            if row_idx == numRows - 1:
                step = -1
            elif row_idx == 0:
                step = 1

            row_idx += step

        result = ''.join([''.join(row) for row in zigzag])
        result = result.replace(' ', '')

        return result
