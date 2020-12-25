# ちゃんとしたCA書くぞー！w

# ライブラリの読み込み
import math as mt
import random as rdm
import sys

# CAのルールを関数にする。
def rule_ca(rule, chr3):
    if type(chr3) == int:
        import sys
        sys.exit("Error: unexpected type")
    try:
        int(rule)
    except:
        import sys
        sys.exit("Error: unexpected number")
    else:
        if rule > 255 or rule < 0:
            sys.exit("Error: unexpected number")
    # ここからメイン
    ruleb = bin(rule)[2:].zfill(8) # ルールの番号を2進数になおして8桁0埋め処理
    # あとは頑張れ↓(もちろん完成してます)
    # print(chr3, ruleb)
    if chr3 == "000":
        n = 7
    elif chr3 == "001":
        n = 6
    elif chr3 == "010":
        n = 5
    elif chr3 == "011":
        n = 4
    elif chr3 == "100":
        n = 3
    elif chr3 == "101":
        n = 2
    elif chr3 == "110":
        n = 1
    elif chr3 == "111":
        n = 0
    else:
        import sys
        sys.exit("Error: unexpected error")
    return ruleb[n]

# 値の読み込み
rule = int(input("Rule: ")) # CAのルール => 0~255
length = int(input("Length: ")) # 配列の長さ
live_pct = int(input("Live_percent: ")) # 初期の配置割合 => 0~100
imgout = input("imgout(y/n): ") # 出力 => セルor数字

print()

if asep >= 100 or asep < 0 or rule > 255 or rule < 0:
    sys.exit("Error: unexpected number")

l = []
# 初期配置生成
for i in range(length):
    num = rdm.randrange(0, 100, 1)
    if num < live_pct:
        l.append(1)
    else:
        l.append(0)

print(" ".join([str(c) for c in l]))

ct = 0
while l.count(1) > 0 and ct < 500:
    cpl = l.copy()
    cpl.insert(0, 0)
    cpl.append(0)
    for i in range(1, len(cpl) - 1):
        rdn = rdm.randrange(0, 100, 1)
        if rdn >= asep:
            l[i - 1] = int(rule_ca(rule, "".join([str(c) for c in [cpl[i - 1], cpl[i], cpl[i + 1]]])))
    if imgout == "y":
        iml = []
        for i in range(len(l)):
            if l[i] == 0:
                iml.append("□")
            else:
                iml.append("■")
        print("".join(iml))
    else:
        print(" ".join([str(c) for c in l]))

    ct += 1
