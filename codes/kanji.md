# 文章中の漢字の個数と割合を表示するプログラム

このプログラムは、CSVファイルに記載された日本語テキストに対して、  
全体の文字数と漢字の文字数、そしてその割合を計算して表示するものです。  
漢字の判定には、`unicodedata`ライブラリを使い、Unicodeの名前に`CJK UNIFIED IDEOGRAPH`を含むかで判断しています。

## ソースコード

```python
import csv  # csvファイル入力と過程
import unicodedata  # 符号化文字集合をunicodeとする便利ライブラリ

def is_kanji(char):
    try:
        return 'CJK UNIFIED IDEOGRAPH' in unicodedata.name(char, '')  # unicode.nameにて漢字ならCJK ~~ が出力される
    except Exception:
        print("Value Error", char)
        return False

total = 0  # 全体の文字数を測定する
ktotal = 0  # 漢字の文字数を測定する

with open("kanji.csv", mode="r", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        for cell in row:
            for char in cell:
                total += 1
                ktotal = ktotal + int(is_kanji(char))

    print("全体文字数:", total, "漢字文字数", ktotal, "漢字割合", round(ktotal / total, 4))
