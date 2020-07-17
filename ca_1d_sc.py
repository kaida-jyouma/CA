import random as rdm
l = [rdm.randint(0, 1) for c in range(20)] #長さ20のランダムな0と1からなる配列を生成
for c in range(20):
    print(l) #表示
    if l[-1] == 1: #①のエラー防止条件
        l[-1] = 0 #①の動作
    for i in range(len(l) - 1):
        if l[-(i+2)] == 1 and l[-(i+1)] == 0: #①の条件
            l[-(i+2)], l[-(i+1)] = l[-(i+1)], l[-(i+2)] #①の動作
print(l) #表示
