# coding: utf-8
testcase=4

for i in range(testcase):
    number = input()
    a,b,c = number.split()
    a,b,c = int(a), int(b), int(c) # a,b,c = map(int,line)
    if a!=0: # if a:
        a=1
    if b!=0:
        b=1
    
    fail=True
    if (a & b==c):
        print("AND")
        fail = False
    if (a or b==c):
        print("OR")
        fail = False
    if (a ^ b==c):
        print("XOR")
        fail = False
    if fail:
    # else:
        print("IMPOSSIBLE") # 若縮排相同 會在只判斷上一行的if情況下反應
    
