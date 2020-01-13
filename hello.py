print('Hello world!')
print('What is your name?')
my_name = input()
print('It is good to meet you,' + my_name)
------------------------------------------------------------------------------
def day_string(day,first_saturday):
    if (day - first_saturday) % 7 == 0:
        return '土'
    elif(day - first_saturday) % 7 == 1:
        return '日'
    return str(day)
    
def day_strings(first_saturday, end_date):
    return[day_string(day, first_saturday) for day in range(1, end_date + 1)]

print('\n'.join(day_strings(7,31)))
------------------------------------------------------------------------------
input_data = input().rstrip().split(" ")
input_data = [int(i)** 3 for i in input_data]
print(str(input_data[0] - input_data[1]))
------------------------------------------------------------------------------
def calcFizzBuzz(cur_num):
	if cur_num % 15 == 0:
		return 'FizzBuzz'
	elif cur_num % 3 == 0:
		return 'Fizz'
	elif cur_num % 5:
		return 'Buzz'
	else:
		return str(cur_num)

def funcFizzBuzz(first_num,last_num):
	return[calcFizzBuzz(num) for num in range(first_num,last_num)]

print('\n'.join(funcFizzBuzz(1,31)))

print("\n".join(["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n) for n in range(1,31)]))

------------------------------------------------------------------------------
win_num = int(input().rstrip())
key_num = int(input().rstrip())
results = []
for i in range(0,key_num):
    temp = int(input().rstrip())
    temp1 = str(win_num - temp)
    if temp == win_num:#１等
        results.append("first")
    elif (temp == (win_num + 1)) or (temp == (win_num -1 )): #前後賞
        results.append("adjacent")
    elif temp1[4:] == "0000":#２等
        results.append("second")
    elif temp1[3:] == "000":#３等
        results.append("third")
    else:
        results.append("blank")

#---------データ入力----------------#
players = []
words_stck = []
words_log = []
in_data = input().rstrip().split(" ")
for i in range(1,int(in_data[0])+1):
    players.append(i)
for i in range(0,int(in_data[1])):
    words_stck.append(input().rstrip())
for i in range(0,int(in_data[2])):
    words_log.append(input().rstrip())
#---------結果出力----------------#
print(len(players))
for element in players:
    print(element)
#*************************************#

#---------データループ----------------#
def roop_data(in_list):
    return[str(element) for element in in_list]
#---------結果出力----------------#
print(len(players))
print('\n'.join(roop_data(players)))

#***********************************************************#
#---------データ入力----------------#
def input_word(stat_num,end_num):
    return[input().rstrip() for i in range(stat_num,end_num)]
#---------データループ----------------#
def roop_data(in_list):
    return[str(element) for element in in_list]
#---------次のプレーヤーを探す----------------#
def srch_nextplayer(xplayers,xcur_player):
    if xcur_player > max(xplayers):
    	xcur_player = min(xplayers)
    while xcur_player not in xplayers:
        xcur_player += 1
    return xcur_player
#---------しりとり判定----------------#
def judge_words(xplayers,xwords_stck,xwords_log):
    words_chk = []
    cur_player = 1
    restart_flg  = 1
    pre_word = xwords_log[0]

    for cur_word in xwords_log:
    #判定1:候補語彙にあるか
        if cur_word not in xwords_stck:
            xplayers.remove(cur_player)
            restart_flg  = 0
    #判定2：最後と最初の文字が同じ（開始、再開時は判定しない）
        elif (restart_flg != 1) and (cur_word[0] != pre_word[-1]):
            xplayers.remove(cur_player)
            restart_flg  = 0
    #判定3:前に答えた単語か
        elif cur_word in words_chk:
            xplayers.remove(cur_player)
            restart_flg  = 0
    #判定4:最後の文字がzでないか
        elif cur_word[-1] == "z":
            xplayers.remove(cur_player)
            restart_flg  = 0
    #次のプレーヤーに交代
        restart_flg += 1
        cur_player += 1
        cur_player = srch_nextplayer(xplayers,cur_player)
        pre_word = cur_word
        words_chk.append(pre_word)

players = []
words_stck = []
words_log = []
in_data = input().rstrip().split(" ")
players = [i for i in range(1,int(in_data[0])+1)]
words_stck = input_word(0,int(in_data[1]))
words_log =  input_word(0,int(in_data[2]))
judge_words(players,words_stck,words_log)
#---------結果出力----------------#
print(len(players))
print('\n'.join(roop_data(players)))

#******************************************************************#
#---------データ入力----------------#
def input_word(stat_num,end_num):
    return[input().rstrip().split(" ") for i in range(stat_num,end_num)]

chair_data = {}
cus_data = []
in_data = input().rstrip().split(" ")
chair_data = {i:0 for i in range(1,int(in_data[0])+1)}
cus_data = input_word(0,int(in_data[1]))
cus_data = [[int(i) for i in j] for j in cus_data]
#---------座席判定----------------#
for i in cus_data:
    #席順リストを作成
    #cur_custmer = [ min(chair_data)  if j > max(chair_data) else j for j in range(i[1],i[1]+i[0])]
    m = 0
    cur_custmer = []
    for j in range(i[1],i[1]+i[0]):
        if j <= max(chair_data):
            cur_custmer.append(j)
        else:
            cur_custmer.append(min(chair_data) + m)
            m += 1
    #全員座れるか一度チェック
    chk_flg = 0
    for k in cur_custmer:
       if chair_data[k] != 0:
           chk_flg = 1
    #全員座れるなら、フラグを１
    if chk_flg == 0:
        for l in cur_custmer:
           if chair_data[l] == 0:
                chair_data[l] = 1
#---------結果出力----------------#
print(list(chair_data.values()).count(1))
#******************************************************************#
