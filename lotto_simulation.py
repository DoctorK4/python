from random import randint


# 번호 뽑기
def generate_numbers(n):
    num_list = []
    for n in range(n):
        
        pick_num = randint(1,45)
        while pick_num in num_list:
            pick_num = randint(1,45)
        num_list.append(pick_num)
    return num_list


# 당첨번호 뽑기 
def draw_winning_numbers():
    pick_all = generate_numbers(7)
    normal = []
    for i in range(5):
        normal.append(pick_all[i])
    bonus = []
    bonus.append(pick_all[6])
    normal.sort()
    final_list = normal + bonus
    return final_list


# 겹치는 번호 갯수 세기 
def count_matching_numbers(list_1, list_2):
    matching_list = []
    for i in range(len(list_1)):
        if list_1[i] in list_2:
            matching_list.append(list_1[i])
    return len(matching_list)


# 당첨번호 확인
def check(numbers, winning_numbers):
    # 1등 확인
    
    if count_matching_numbers(numbers, winning_numbers[:6]) == 6:
        return 1000000000
    
    # 2등 확인
    bonus_list = []
    bonus_list.append(winning_numbers[6])
    # 보너스번호가 있고, 5개 겹쳐야한다. 
    if count_matching_numbers(numbers, winning_numbers[:6]) == 5 and count_matching_numbers(numbers, bonus_list) == 1 :
        return 50000000
    
    # 3등 확인
    if count_matching_numbers(numbers, winning_numbers[:6]) == 5:
        return 1000000
    
    # 4등 확인
    if count_matching_numbers(numbers, winning_numbers[:6]) == 4:
        return 50000
    
    # 5등 확인
    if count_matching_numbers(numbers, winning_numbers[:6]) == 3:
        return 5000

