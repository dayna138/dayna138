# coding: utf-8
from random import sample
# '''大字串'''
words='''妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
newwords=words.split('\n')
from random import randint
for j in range(randint(2,7)):
    sentence=sample(newwords, randint(2,5))
    print(' '.join(sentence))
    
