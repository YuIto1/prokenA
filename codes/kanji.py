import csv #csvファイル入力と過程
import unicodedata #符号化文字集合をunicodeとする 便利ライブラリ

def is_kanji(char):
    try:
        return 'CJK UNIFIED IDEOGRAPH' in unicodedata.name(char, '')  #unicode.nameにて漢字ならCJK ~~ が出力される

    except Exception:
        print("Value Error", char) 
        return False
         
    
total = 0 #全体の文字数を測定する
ktotal = 0 #漢字の文字数を測定する
with open("kanji.csv", mode = "r", encoding = 'utf-8') as f: #with open
    reader = csv.reader(f) #各行に関するイテレータreader 
    for row in reader: # 各行をリスト化して対応
        for cell in row: #各リストを文字列化
            for char in cell: # 文字列を一文字ずつ読む
                total += 1
                ktotal = ktotal + int(is_kanji(char)) 
    
    print("全体文字数:", total,"漢字文字数", ktotal, "漢字割合", round(ktotal / total,4))
