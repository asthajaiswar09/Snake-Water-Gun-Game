'''snake water gun game
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
# print(f" the computer entered {computer}" )

yourstr=input("enter your choice:")
youDic={"s":1,"g":0,"w":-1}
you=youDic[yourstr]
reverseDic={1:"s",0:"g",-1:"w"}
print(f"computer choice {reverseDic[computer]}")

if(computer==you):
    print("its a draw")
else:
 
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you loose!")
    elif(computer==1 and you==-1):
        print("you loose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==1):
        print("you loose!")
    elif(computer==0 and you==-1):
        print("you win!")
    else:
        print("something went wrong")