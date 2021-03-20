# 2次元CAモデルver3.0.0
import matplotlib.pyplot as plt
from google.colab import drive
from time import sleep
import time as tm
import random as rdm
import numpy as np
import sys
if input("drive y/n: ") == "y":
    drive.mount('/content/drive')
def mkim(ls, xlen, ylen, blk=[], ttl=None):
    # ↓に配列をコピペ
    # ls = [[0, 3], [1, 3], [1, 5], [1, 7], [1, 9], [1, 10], [2, 3], [2, 5], [2, 7], [2, 9], [2, 10], [2, 11], [3, 3], [3, 5], [3, 7], [3, 9], [3, 10], [4, 3], [4, 5], [4, 7], [4, 9], [4, 11], [5, 3], [5, 5], [5, 7], [5, 9], [5, 11], [6, 3], [6, 5], [6, 7], [6, 9]]
    lx = []
    ly = []
    fig = plt.figure(figsize=(6, 4))
    l1 = [c for c in range(xlen)]
    l2 = [c for c in range(ylen)]
    plt.tick_params(labelbottom=False,
                    labelleft=False,
                    labelright=False,
                    labeltop=False)
    plt.tick_params(bottom=False,
                    left=False,
                    right=False,
                    top=False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    for i in l1:
        for j in l2:
            plt.scatter(i, -j, marker="$□$", s=270, zorder=1, c="#000000")
    for i in range(len(ls)):
        if i != (len(ls) - 1):
            plt.scatter(ls[i][1], -(ls[i][0]), marker="$■$", s=250, zorder=2, c="#000000")
        else:
            im = plt.scatter(ls[i][1], -(ls[i][0]), marker="$■$", s=250, zorder=2, c="#000000")
            if ttl != None:
                plt.savefig(ttl)
            return im
def print2d(listname):
    print("\n".join(list(map(str, listname))))
    return
def print2djoin(listname):
    da = [""]
    for d1 in listname:
        for d2 in d1:
            da.append(d2)
        da.append("\n")
    print(" ".join(list(map(str, da))))
    return ""
def mkim_fld(arr2d, aspect=(10, 10), ttl=None):
    import matplotlib.pyplot as plt
    import numpy as np
    try:
        str(arr2d[0][0] + 1)
    except:
        import sys
        sys.exit("The element type must be int, other was found...")
    else:
        plt.figure(figsize=aspect)
        plt.tick_params(labelbottom=False,
                        labelleft=False,
                        labelright=False,
                        labeltop=False)
        plt.tick_params(bottom=False,
                        left=False,
                        right=False,
                        top=False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
    im = None
    for i in range(len(arr2d)):
        for j in range(len(arr2d[i])):
            elm = "o"
            if arr2d[i][j] == 0:
                elm = chr(9633)
                col = "black"
            elif arr2d[i][j] == 1:
                elm = chr(9632)
                col = "blue"
            elif arr2d[i][j] == 2:
                elm = chr(9632)
                col = "darkorange"
            elif arr2d[i][j] == 9:
                elm = chr(9641)
                col = "saddlebrown"
            im = plt.plot(j, 0 - i, marker="$"+elm+"$", color=col, markersize=15)
    if ttl != None:
        plt.savefig(ttl)
    return im
def join2darr(arr2d):
    l = []
    for i in range(len(arr2d)):
        l.extend(arr2d[i])
    return l
# check~~: ln=list, x/y=place
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
        return True
    else:
        return False
def checkul(ln, x, y): #下に行けるかどうか
    if ln[x + 1][y - 1] == lv:
        return False
    else:
        return True
def floor(x):
    d3 = 0
    while d3 < x:
        d3 += 1
    return int(d3 - 1)


def retdirec(flds, i, j):
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
            return True
        else:
            return False
    # フォーマット: [right(0), bottom(1), top(2), left(3)]
    movel = [None, None, None, None]
    # ここから条件分岐
    if i == 0: # 上端
        movel[2] = False # 上
        movel[1] = checkbtm(flds, i, j) # 下
        
        if j == 0: # 左端
            movel[3] = False # 左
            movel[0] = checkrit(flds, i, j) # 右
            # print("a")
        
        else:
            if j == (len(flds[i]) - 1): # 右端
                movel[0] = False # 右
                movel[3] = checklft(flds, i, j) # 左
                # print("b")
            
            else: # それ以外
                movel[0] = checkrit(flds, i, j) # 右
                movel[3] = checklft(flds, i, j) # 左
                # print("c")
        
    
    
    elif i == (len(flds) - 1): # 下端
        movel[1] = False # 下
        movel[2] = checktop(flds, i, j) # 上
    
        if j == 0: # 左端
            movel[3] = False # 左
            movel[0] = checkrit(flds, i, j) # 右
            # print("d")
        
        else:
            if j == (len(flds[i]) - 1): # 右端
                movel[0] = False # 右
                movel[3] = checklft(flds, i, j) # 左
                # print("e")
            
            else: # それ以外
                movel[0] = checkrit(flds, i, j) # 右
                movel[3] = checklft(flds, i, j) # 左
                # print("f")
    
    
    elif j == 0: # 左端
        movel[0] = checkrit(flds, i, j) # 右
        movel[1] = checkbtm(flds, i, j) # 下
        movel[2] = checktop(flds, i, j) # 上
        movel[3] = False # 左
        # print("g")
    
    
    elif j == (len(flds[i]) - 1): # 右端
        movel[0] = False # 右
        movel[1] = checkbtm(flds, i, j) # 下
        movel[2] = checktop(flds, i, j) # 上
        movel[3] = checklft(flds, i, j) # 左
        # print("h")
        
    
    else:
        movel[0] = checkrit(flds, i, j) # 右
        movel[1] = checkbtm(flds, i, j) # 下
        movel[2] = checktop(flds, i, j) # 上
        movel[3] = checklft(flds, i, j) # 左
        # print("i")
    
    # print(i, j, movel)
    return movel


rom = [[0 for c in range(13)] for d in range(12)]
lv = chr(0x25a0)
nn = chr(0x25a1)
bl = chr(0x25a9)
lv = 1 #chr(0x25a0)
nn = 0 #chr(0x25a1)
bl = 9 #chr(0x25a9)
bll = [
       [7, 10], [7, 11], [7, 12],
       [8, 10], [8, 11], [8, 12],
       [9, 10], [9, 11], [9, 12],
       [10, 10], [10, 11], [10, 12],
       [11, 10], [11, 11], [11, 12]
]
fig = plt.figure(figsize=(int(len(rom[0])/2), int(len(rom)/2)))
ims = []

for i in bll:
    rom[i[0]][i[1]] = 9


# mkim_fld(rom, (int(len(rom[0])/2), int(len(rom)/2)), ("/content/drive/My Drive/col-imgs/img" + str(0).zfill(3)))
mkim_fld(rom, (7, 5), ("/content/drive/My Drive/col-imgs/img" + str(0).zfill(3)))
# mkim_fld(rom, (7, 5))

mkim_fld(rom, (7, 5))

# print2d(rom)
print2djoin(rom)
print("--------")
# x枚表示
octr = 0
# ims.append(mkim_fld())
# fire = int(input())
# pct = [1, 0, 1, 2, 2, 1, 0] # 出口までの距離
# for i in range()
print(rom)
ctr = 0
# print(join2darr(rom))
while True:
    ctr += 1
    if ctr > 30:
        sys.exit("The number of trials has exceeded " + str(ctr))
    # ドアから出す
    if rom[0][4] == 1:
        rom[0][4] = 0
        octr += 1
    if rom[0][5] == 1:
        rom[0][5] = 0
        octr += 1
    if rom[0][6] == 1:
        rom[0][6] = 0
        octr += 1
    if rom[0][7] == 1:
        rom[0][7] = 0
        octr += 1
    if rom[0][8] == 1:
        rom[0][8] = 0
        octr += 1        
    # 人を入れる
    if rdm.randrange(0, 100, 1) < 75:
        if rdm.randrange(0, 100, 1) < 50:
            rom[10][0] = 1
        else:
            rom[11][0] = 1
    if rdm.randrange(0, 100, 1) < 75:
        if rdm.randrange(0, 100, 1) < 50:
            rom[11][8] = 1
        else:
            rom[11][9] = 1
    # print2djoin(rom)
    mkim_fld(rom, (7, 5))
    nxt = [[0 for c in range(13)] for d in range(12)] #romと同じ要素数の空配列にすること。
    for i in bll:
        nxt[i[0]][i[1]] = 9
    lvl = []
    mvl = []
    for i in range(len(rom)):
        for j in range(len(rom[i])):
            if rom[i][j] == 1:

                k01 = [i, j]
                lvl.append(k01)

                # 関数行き。取ってくる。
                movel = retdirec(rom, i, j)

                mvl.append(movel)

                #行き先決定
                if j > 7:
                    if movel[2]:
                        nxt[i-1][j] += 1
                    elif movel[3]:
                        nxt[i][j-1] += 1
                else:
                    if movel[2]:
                        nxt[i-1][j] += 1
                    elif movel[3]:
                        nxt[i][j+1] += 1
    
    # print()
    # print("---")
    # print("rom")
    # print2djoin(rom)
    # print()
    # print("nxt")
    # print2djoin(nxt)
    # print()


    for i in range(len(lvl)):
        movels = mvl[i]
        p, q = lvl[i]
        # print("p", p)
        # print("q", q)
        rom[p][q] = 0
        if q < 6:
            if movels[2]:
                rom[p - 1][q] = 1
            elif movels[0]:
                rom[p][q + 1] = 1
        elif 6 < j:
            if movels[2]:
                rom[p - 1][q] = 1
            elif movels[3]:
                rom[p][q - 1] = 1
        else:
            if movels[2]:
                rom[p - 1][q] = 1

    
    mkim_fld(rom, (7, 5), ("/content/drive/My Drive/col-imgs/img" + str(ctr).zfill(3)))
    # mkim_fld(rom, (7, 5))
    
    """for i in range(len(nxt)):
        for j in range(len(nxt[i])):
            # print()
            # print("---")
            # print("rom")
            # print2djoin(rom)
            # print()
            # print("nxt")
            # print2djoin(nxt)
            # print()
            if nxt[i][j] > 1 and nxt[i][j] != 9:
                sk = [None, checkbtm(rom, i, j), None]
                if j == 0:
                    sk[0] = True
                    sk[-1] = checkrit(rom, i, j)
                elif j == len(rom[i]) - 1:
                    sk[-1] = True
                    sk[0] = checklft(rom, i, j)
                rdmn = rdm.randrange(0, 100, 1)
                # この辺の条件分岐でエラー出る。
                # if nxt[i][j] == 9:
                #     print(i, j, "stp")
                # else:
                #     # None
                nxt[i][j] = 1
                
                
                if rdmn < 33:
                    if not sk[0]: #左から
                        # nxt[i][j] = 1
                        nxt[i-1][j] = rom[i-1][j]
                        nxt[i][j+1] = rom[i][j+1]
                    else: #下から
                        # nxt[i][j] = 1
                        nxt[i][j-1] = rom[i][j-1]
                        nxt[i][j+1] = rom[i][j+1]
                elif rdmn < 50:
                    if sk[2]: #左から
                        # nxt[i][j] = 1
                        nxt[i-1][j] = rom[i-1][j]
                        nxt[i][j+1] = rom[i][j+1]
                    else: #下から
                        # nxt[i][j] = 1
                        nxt[i][j-1] = rom[i][j-1]
                        nxt[i][j+1] = rom[i][j+1]
                elif rdmn < 66:
                    if sk[0]: #右から
                        # nxt[i][j] = 1
                        nxt[i][j-1] = rom[i][j-1]
                        nxt[i-1][j] = rom[i-1][j]
                    else: #下から
                        # nxt[i][j] = 1
                        nxt[i][j-1] = rom[i][j-1]
                        nxt[i][j+1] = rom[i][j+1]
                else:
                    # print(i, j, ctr, sk, rdmn)
                    if sk[2]: #下から
                        # nxt[i][j] = 1
                        nxt[i][j-1] = rom[i][j-1]
                        nxt[i][j+1] = rom[i][j+1]
                    else: #右から
                        # nxt[i][j] = 1
                        nxt[i][j-1] = rom[i][j-1]
                        nxt[i-1][j] = rom[i-1][j]
            

            if nxt[i][j] == 1:
                rom[i][j] = 1
                nxt[i][j] = 0
            print2djoin(rom)"""




# 1.43, 5
