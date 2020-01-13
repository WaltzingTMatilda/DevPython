#**************************************************#
#同単語をカウントし、表示
input_words = []
master_words = []
input_words = input().rstrip().split(" ")
master_words = list(dict.fromkeys(input_words))
for i in master_words:
    print(i + " " + str(input_words.count(i)))
#**************************************************#

#**************************************************#
#文字列の重複カウント
ans_count = 0
key_words = input().rstrip()
len_words= len(key_words)
#read line&lenth
line = input().rstrip()
num_words = len(line)
for iCnt in range(0,num_words):
    if line[iCnt] == key_words[0]:
        comp_words = line[iCnt:iCnt+len_words]
        if comp_words == key_words:
            ans_count += 1
print(str(ans_count))
#**************************************************#
