import random

# 코드를 작성하세요.

answer = random.randint(1, 20)
for i in range(5, 0, -1):
    user_try = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:".format(i)))
    i -= 1
    if user_try == answer:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(5 - i))
        break
    elif user_try != answer:
        
        if i > 0:
            if user_try > answer:
                print("Down")    
            elif user_try < answer:
                print("Up")

        else:
            print("아쉽습니다. 정답은 {}입니다.".format(answer))