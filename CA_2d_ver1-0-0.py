# 2次元CAモデルver1.0.1
def print2d(listname):
    print("\n".join(list(map(str, cll))))
    return
def print2djoin(listname):
    da = [""]
    for d1 in listname:
        for d2 in d1:
            da.append(d2)
        da.append("\n")
    print(" ".join(list(map(str, da))))
    return("")
def checklv(ln, x, y):
    if ln[x][y] == lv:
        return(True)
    else:
        return(False)
def checktop(ln, x, y):
    if ln[x - 1][y] == nn:
        return(True)
    else:
        return(False)
def checkbtm(ln, x, y):
    if ln[x + 1][y] == nn:
        return(True)
    else:
        return(False)
def checkrit(ln, x, y):
    if ln[x][y + 1] == nn:
        return(True)
    else:
        return(False)
def checklft(ln, x, y):
    if ln[x][y - 1] == nn:
        return(True)
    else:
        return(False)
def floor(x):
    d3 = 0
    while d3 < x:
        d3 += 1
    return(int(d3 - 1))
cll = [
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
]
lv = chr(9632)
nn = chr(9633)
fi = chr(9635)
for a in range(len(cll)):
    for b in range(len(cll[a])):
        if cll[a][b] == 1:
            cll[a][b] = lv
        else:
            cll[a][b] = nn
# print2d(cll)
print2djoin(cll)
print("--------")
# 10枚表示
octr = 0
for z in range(28):
    lvlist = []
    # 延焼

    # ドア
    if cll[1][-1] == lv:
        cll[1][-1] = nn
        octr += 1
    if cll[-1][-1] == lv:
        cll[-1][-1] = nn
        octr += 1
    for c in range(len(cll)):
        for d in range(len(cll[c])):
            if checklv(cll, c, d): # その座標が生きたセルであれば(比較演算子不要)
                lvlist.append([c, d])
    # print(lvlist) # 生存座標の出力
    for e in lvlist:
        # フォーマット: [right(0), bottom(1), top(2), left(3)]
        movel = [None, None, None, None]
        # ここから条件分岐
        if e[0] == 0: # 上端
            movel[2] = False # 上
            movel[1] = checkbtm(cll, e[0], e[1]) # 下
            
            if e[1] == 0: # 左端
                movel[3] = False # 左
                movel[0] = checkrit(cll, e[0], e[1]) # 右
            
            else:
                if e[1] == (len(cll[e[0]]) - 1): # 右端
                    movel[0] = False # 右
                    movel[3] = checklft(cll, e[0], e[1]) # 左
                
                else: # それ以外
                    movel[0] = checkrit(cll, e[0], e[1]) # 右
                    movel[3] = checklft(cll, e[0], e[1]) # 左


        elif e[0] == (len(cll) - 1): # 下端
            movel[1] = False # 下
            movel[2] = checktop(cll, e[0], e[1]) # 上

            if e[1] == 0: # 左端
                movel[3] = False # 左
                movel[0] = checkrit(cll, e[0], e[1]) # 右
            
            else:
                if e[1] == (len(cll[e[0]]) - 1): # 右端
                    movel[0] = False # 右
                    movel[3] = checklft(cll, e[0], e[1]) # 左
                
                else: # それ以外
                    movel[0] = checkrit(cll, e[0], e[1]) # 右
                    movel[3] = checklft(cll, e[0], e[1]) # 左


        elif e[1] == 0: # 左端
            movel[0] = checkrit(cll, e[0], e[1]) # 右
            movel[1] = checkbtm(cll, e[0], e[1]) # 下
            movel[2] = checktop(cll, e[0], e[1]) # 上
            movel[3] = False # 左


        elif e[1] == (len(cll[e[0]]) - 1): # 右端
            movel[0] = False # 右
            movel[1] = checkbtm(cll, e[0], e[1]) # 下
            movel[2] = checktop(cll, e[0], e[1]) # 上
            movel[3] = checklft(cll, e[0], e[1]) # 左


        else:
            movel[0] = checkrit(cll, e[0], e[1]) # 右
            movel[1] = checkbtm(cll, e[0], e[1]) # 下
            movel[2] = checktop(cll, e[0], e[1]) # 上
            movel[3] = checklft(cll, e[0], e[1]) # 左

        # フォーマット: [right(0), bottom(1), top(2), left(3)]
        # print("", movel, end=",")
        # print()
        
        # 進行方向で条件分岐
        if movel[0]:
            cll[e[0]][e[1] + 1] = lv
            cll[e[0]][e[1]] = nn
        elif movel[1]:
            cll[e[0] + 1][e[1]] = lv
            cll[e[0]][e[1]] = nn
        elif movel[2]:
            cll[e[0] - 1][e[1]] = lv
            cll[e[0]][e[1]] = nn
    
    
    print(print2djoin(cll), "octr:", octr, "| move:", z + 1)
    print("--------")
