# 파일 불러오기 + 리스트에 각 단어들 추가
eng_list = []
kor_list = []
with open('vocabulary.txt','r',encoding='UTF-8') as f:
    for words in f:
        words = words.strip()
        words = words.split(': ')
        eng_list.append(words[0])
        kor_list.append(words[1])

# 퀴즈 내기 
for i in range(len(kor_list)):
    user_answer = input("{}:".format(kor_list[i]))

# 맞았을 경우 
    if user_answer == eng_list[i]:
        print("맞았습니다!")

# 틀렸을 경우 
    else:
        print("아쉽습니다. 정답은 {}입니다.".format(eng_list[i]))