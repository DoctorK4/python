from random import randint


def generate_numbers():
    numbers = []
    for i in range(1, 4):
        num = randint(1, 9)
        while num in numbers:
            num = randint(1, 9)
        numbers.append(num)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    
    # 숫자입력
    while len(new_guess) < 3 :
        num = input("{}번째 숫자를 입력하세요:".format(len(new_guess)+1))

        # 범위 체크
        if not 0 < int(num) <= 9 : 
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
            
        # 중복 체크
        elif int(num) in new_guess:
            print("중복되는 숫자입니다.다시 입력하세요")
        
        else: 
            new_guess.append(int(num))
    
    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(guesses)):
        if guesses[i] in solution:
            if guesses[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1
    
    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True :
    user_input = take_guess()
    strike, ball = get_score(user_input, ANSWER)
    print("{}S, {}B".format(strike, ball))
    tries += 1
    if strike == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

