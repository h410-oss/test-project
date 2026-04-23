import random

def play_game():
    num = random.randint(1, 10)
    guess = int(input("1〜10で当てて: "))

    if guess == num:
        print("当たり！")
    else:
        print("ハズレ！ 正解:", num)
