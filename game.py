# coding: utf-8
from random import randint
def game():
    password=randint(1,99)
    guess=-1
    _min=1
    _max=99

    while guess!=password:
        guess=int(input('請輸入數字:'))
        if guess>password:
            _max = guess
            print('答案介於',_min,'~',_max,'之間')
        elif guess<password:
            _min = guess
            print('答案介於',guess,'~',_max,'之間')
            
    print('恭喜你猜對囉！')
play= True

while play:
    game()
    print('^_____^')
    again=input('再玩一次？')
    if again=='no':
        play = False
