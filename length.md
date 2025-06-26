# 文の長さを測定するためのプログラム
## アルゴリズム
。や！の間に含まれる形態素の数を数え上げます。
## 問題点
「」が出現したときの動作が現在だと下のようになります。

例: 今日はお母さんに、「今日は夕ご飯いらない。」と伝えると、「まあ残念。今日は刺身だったのに。」と言われました。
→今日はお母さんに、「今日は夕ご飯いらない　/　」と伝えると、「まあ残念。今日は刺身だったのに / 」と言われました

「」で文章を切ることも考えたのですが、単語の強調のための「」なども一文として含まれてしまうので悩みどころです。

## コード
```python
from pyknp import Juman
from pathlib import Path

juman = Juman()
input_path = Path("sample_in.txt")

with input_path.open("r", encoding = "utf-8")as f:
    
    end_letters = ["。", "？", "！", ".", "?", "!"] #この文字が来たら文の終わりと認識
    ignore = ["「", "」", "（", "）", "、", ",", "・", "(", ")", "{", "}", "[", "]", "\""] #単語数に含めない文字群
    
    #end_letters館に含まれる形態素の数をword_countで数える
    word_count = 0
    total_words = 0
    total_sentences = 0
    for line in f:
        result = juman.analysis(line)
        for mrph in result.mrph_list():
            if mrph.midasi in end_letters:
                print(f"sentence ends. word_count={word_count}")
                total_words += word_count
                total_sentences += 1
                word_count = 0
            elif mrph.midasi in ignore:
                continue
            else:
                #print(mrph.midasi)     #オプション
                word_count += 1
                
    print(f"平均単語数={total_words/total_sentences}")
```
