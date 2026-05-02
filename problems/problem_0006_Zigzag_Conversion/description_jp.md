# 6. ジグザグ変換 (Zigzag Conversion)

文字列 "PAYPALISHIRING" は、指定された行数に応じて、次のようなジグザグパターンで記述されます（可読性を高めるために、等幅フォントで表示することをお勧めします）。

```
P   A   H   N
A P L S I I G
Y   I   R
```

これを一行ずつ読むと、"PAHNAPLSIIGYIR" となります。

文字列を受け取り、指定された行数に基づいてこの変換を行うコードを記述してください。

`string convert(string s, int numRows);`

## 例 1:
入力: s = "PAYPALISHIRING", numRows = 3
出力: "PAHNAPLSIIGYIR"

## 例 2:
入力: s = "PAYPALISHIRING", numRows = 4
出力: "PINALSIGYAHRPI"
説明:
```
P     I    N
A   L S  I G
Y A   H R
P     I
```

## 例 3:
入力: s = "A", numRows = 1
出力: "A"

## 制約事項:
- 1 <= s.length <= 1000
- s は英字（小文字および大文字）、','、'.' で構成されます。
- 1 <= numRows <= 1000
