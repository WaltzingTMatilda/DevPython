#**********************************************************#
#結果サマリ
key_num = int(input().rstrip())
key_words = []
for i in range(0,key_num):
    temp = input().rstrip()
    if (temp in key_words) == True:
        key_words.remove(temp)
    key_words.insert(0,temp)
for i in key_words:
    print(i)
#**********************************************************#
#占い
key_name = []
dic1 = {}
#input1
num = int(input().rstrip())
for iCnt in range(0,num):
    element = input().rstrip().split(" ")
    key_name.append(element[0])
    dic1.setdefault(element[0],element[1])
#input2
dic2 = {}
num = int(input().rstrip())
for iCnt in range(0,num):
    element = input().rstrip().split(" ")
    dic2.setdefault(element[0],element[1])
#output as keyword
for element in key_name:
   key_blood = dic1.get(element,0)
   print(element + str(" ") + str(dic2.get(key_blood,0)))
#**********************************************************#

#**********************************************************#
#五目並べ
import numpy as np
#---------------------------------------------#
#縦横判定関数の定義
def judgeLine(ref_list,ref_data,iflg):
    if iflg == 0 :
        arr_t = np.array(ref_list).T
    cur_list =[]
    jCnt = 0
    while jCnt < ref_data:
        if iflg == 0:
            cur_list = list(arr_t[jCnt])
        else:
            cur_list = list(ref_list[jCnt])
        #行ごとに勝敗判定
        if cur_list.count('O') == 5:
            win_data = 'O'
            break
        elif cur_list.count('X') == 5:
            win_data = 'X'
            break
        else:
            win_data = 'D'
        jCnt += 1
    #判定出力
    return win_data
#---------------------------------------------#
#斜め判定関数の定義
def judgeLeanLine(ref_list,ref_data):
    win_count1 =0
    win_count2 =0
    #１行目が.でなければ判定開始
    if ref_list[0][0] != '.' :
        win_count1 = 1
    if ref_list[0][4] != '.' :
        win_count2 = 1
    #2行目移行を判定
    for jCnt in range(1,ref_data):
        for kCnt in range(0,ref_data):
        #パターン１判定
            if jCnt == kCnt:
                if ref_list[jCnt][jCnt] == ref_list[0][0]:
                    win_count1 += 1
        #パターン2判定
            if jCnt + kCnt == 4:
                if ref_list[jCnt][kCnt] == ref_list[0][4]:
                    win_count2 += 1
    if win_count1 == 5:
        win_data = ref_list[0][0]
    elif win_count2 == 5:
        win_data = ref_list[0][4]
    else:
        win_data = 'D'
    return win_data
#---------------------------------------------#
#初期値設定
num_data = 5
ans = 'D'
data_list= []
#入力データ読み込み
for iCnt in range(0,num_data):
    data_list.append(list(input().rstrip()))
#横判定関数
ans = judgeLine(data_list,num_data,0)
#縦判定関数
if ans == 'D':
    ans = judgeLine(data_list,num_data,1)
#斜め判定関数
if ans == 'D':
   ans = judgeLeanLine(data_list,num_data)
#結果出力
print(ans)
#**********************************************************#
