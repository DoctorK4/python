# 파일 불러오기 + 리스트에 각 단어들 추가
import random

eng_list = []
kor_list = []
with open('vocabulary.txt','r',encoding='UTF-8') as f:
    for words in f:
        words = words.strip()
        words = words.split(': ')
        eng_list.append(words[0])
        kor_list.append(words[1])

# 퀴즈 내기 
while True:
    q_num = random.randint(0, len(kor_list)-1)
    user_answer = input("{}:".format(kor_list[q_num]))

# 맞았을 경우 
    if user_answer == eng_list[q_num]:
        print("맞았습니다!")

# 'q'를 입력했을 경우
    elif user_answer == 'q':
        break

# 틀렸을 경우 
    else:
        print("아쉽습니다. 정답은 {}입니다.".format(eng_list[q_num]))