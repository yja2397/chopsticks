
# coding: utf-8

# In[1]:

### 젓가락을 만들자
# Chopsticks game


# In[44]:

import random


# In[45]:

def gameStart():
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')
    # 사람 두명 만들기
    counts = 0
    player1 = player("세공사")
    player2 = player("땜장이")
    playerList = [player1, player2]
    while True:
        if turn == 'A':
            doTurn(player1)
        else:
            doTurn(player2)
        counts += 1
        
    print('Over at ' + counts + 'times. ' + person + 'win!')


# In[ ]:

def doTurn(person):
    print(person.getname(), "'s turn", sep = "")
    print("What will you do?")
    while True:
        print("1. attack  2. reconstruct")
        do = int(input())
        if do is 1:
            attackOtherPlayer(person)
            break
        elif do is 2:
            person.reconstruct()
            break
        else:
            print("Wrong command")
            


# In[ ]:

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'A'
    else:
        return 'P'
    


# In[ ]:

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

def attackOtherPlayer(player):
    pList = playerList
    pList.remove(player)
    print("Choose my hand  1. Left  2. Right > " , end = "")
    m = int(input())
    print("Choose opponent hand  1. Left  2. Right > " , end = "")
    o = int(input())
    pList[0]
    ### 여기 만드는 중
    
def attack(hand1, hand2):
    attacked = hand1.getFingers() + hand2.getFingers()
    if attacked >= 5:
        attacked = 0
    hand2.setFingers(attacked)
    print("공격받은 손의 손가락 수는", attacked, "개 입니다.")
    return


# In[37]:

### 손 객체
### 손가락의 수를 가지고 있음

class hand:
    def __init__(self):
        self.fingers = 1
    
    def getPlayer(self):
        return self.player
    
    def getFingers(self):
        return self.fingers

    def setFingers(self, k):
        self.fingers = k
        


# In[32]:

### 플레이어 객체
### 플레이어 네임과 2개의 손을 가지고 있음


class player:
    def __init__(self, name="Player"):
        self.name = name
        self.leftHand = hand()
        self.rightHand = hand()
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def reconstruct(self, finger_construct=finger_construct_list):
        both_fingers = self.leftHand.getFingers() + self.rightHand.getFingers()
        if both_fingers not in [2, 3, 4, 5, 6]:
            print("손가락을 바꿀 수 없습니다.")
            return
        finger_list = finger_construct[both_fingers]
        print("바꿀 조합 선택")
        print("0 : 돌아가기")
        for i in range(1, len(finger_list)+1):
            print(i, ":", finger_list[i-1])
        while True:
            print(">", end = " ")
            k = int(input())
            if k == 0:
                # 다시 자기 턴을 시작 하는 함수
                break
            elif (k-1) in [self.leftHand.getFingers(), self.rightHand.getFingers()]:
                print("해당 조합은 선택 못해")
            elif (k-1) in list(range(len(finger_list))):
                self.leftHand.setFingers(finger_list[k-1][0])
                self.rightHand.setFingers(finger_list[k-1][1])
                break
            else:
                print("손가락이 참 많으시군요")
    
    def showFingers(self):
        print("현재 손가락")
        print("왼손 :", self.leftHand.getFingers(), " 오른손 :", self.rightHand.getFingers())


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

print("Let's play chopsticks game!")

while True:
    gameStart()
    if not playAgain():
        print("Bye bye!")
        break
        


# In[33]:

finger_construct_list = {2:[[0, 2], [1, 1], [2, 0]], 3:[[0, 3], [1, 2], [2, 1], [3, 0]], 4:[[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]], 5:[[1, 4], [2, 3], [3, 2], [4, 1]], 6:[[2, 4], [3, 3], [4, 2]]}


# In[34]:




# In[35]:




# In[38]:




# In[40]:




# In[46]:




# In[43]:




# In[ ]:




# In[ ]:



