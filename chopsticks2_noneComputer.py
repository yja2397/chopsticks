
# coding: utf-8

# In[13]:


### 젓가락을 만들자
# Chopsticks game


# In[14]:


import random


# In[15]:


def gameStart(): # 게임 시작
    
    # 사람 두명 만들기
    player1 = player("세공사")
    player2 = player("땜장이")
    playerList = [player1, player2]
    
    random.shuffle(playerList)
    
    print("" + playerList[0].getName() + "(이)가 선입니다.")
    turn = playerList[0]
    
    counts = 0
    print()
    
    while True:
        print()
        if turn == player1:
            doTurn(player1, player2)
            turn = player2
        else:
            doTurn(player2, player1)
            turn = player1
        counts += 1
        
        print()
        if showPlayerFingers(playerList) == False:
            break
    
    print()
    print(str(counts/2) + '턴 만에 끝났습니다.')


# In[ ]:


def doTurn(person, otherPerson):
    print(person.getName(), "의 차례입니다.", sep = "")
    print("무엇을 하시겠습니까?")
    while True:
        both_fingers = person.leftHand.getFingers() + person.rightHand.getFingers()
        if both_fingers not in [2, 3, 4, 5, 6]:
            attackOtherPlayer(person, otherPerson)
            break
        else:
            print("1. 공격  2. 바꾸기")
            do = int(input())
            if do is 1:
                attackOtherPlayer(person, otherPerson)
                break
            elif do is 2:
                person.reconstruct()
                break
            else:
                print("잘못된 입력입니다.")


# In[ ]:


def isValidHit(leftHand, rightHand):
    if(leftFinger == 1 and rightFinger == 0):
        return False
    if(leftFinger == 0 and rightFinger == 1):
        return False
    if(leftFinger == 4 and rightFinger == 4):
        return False
    if(leftFinger == 4 and rightFinger == 3):
        return False
    if(leftFinger == 3 and rightFinger == 4):
        return False


# In[18]:


def whoGoesFirst(A, B):
    if random.randint(0,1) == 0:
        return A
    else:
        return B
    


# In[19]:


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# In[20]:


def attackOtherPlayer(player , otherPlayer):
    a = ""
    if player.leftHand.getFingers() > 0:
        a += "1. 왼손"
    if player.rightHand.getFingers() > 0:
        a += "  2. 오른손"
        
    print("자기 손을 선택하시오  " + a + "  > " , end = "")
    m = int(input())
    if m == 1:
        hand1 = player.leftHand
    else:
        hand1 = player.rightHand
    
    b = ""
    if otherPlayer.leftHand.getFingers() > 0:
        b += "1. 왼손"
    if otherPlayer.rightHand.getFingers() > 0:
        b += "  2. 오른손"
    
    print("상대 손을 선택하시오  " + b + "  > " , end = "")
    o = int(input())
    if o == 1:
        attack(hand1, otherPlayer.leftHand)
    else:
        attack(hand1, otherPlayer.rightHand)
    
    
def attack(hand1, hand2):
    attacked = hand1.getFingers() + hand2.getFingers()
    if attacked >= 5:
        attacked = 0
        print("상대방의 손이 격파되었습니다.")
    else:
        print("공격받은 손의 손가락 수는", attacked, "개 입니다.")
        
    hand2.setFingers(attacked)
    return


# In[21]:


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
        


# In[22]:


finger_construct_list = {2:[[0, 2], [1, 1], [2, 0]], 3:[[0, 3], [1, 2], [2, 1], [3, 0]], 4:[[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]], 5:[[1, 4], [2, 3], [3, 2], [4, 1]], 6:[[2, 4], [3, 3], [4, 2]]}


# In[23]:


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
            if (k-1) in [self.leftHand.getFingers(), self.rightHand.getFingers()]:
                print("해당 조합은 선택 못해")
            elif (k-1) in list(range(len(finger_list))):
                self.leftHand.setFingers(finger_list[k-1][0])
                self.rightHand.setFingers(finger_list[k-1][1])
                break
            else:
                print("손가락이 참 많으시군요")
    
    def showFingers(self):
        print("왼손 :", self.leftHand.getFingers(), " 오른손 :", self.rightHand.getFingers())


# In[24]:


def showPlayerFingers(A):
    for i in A:
        if(i.leftHand.getFingers() == 0 and i.rightHand.getFingers() == 0):
            print(i.getName() + " 탈락!")
            return False
        
    for i in A:
        print(i.getName() + "의 손가락 현황")
        i.showFingers()
    return True


# In[ ]:


print("젓가락 게임을 해볼까요?")

while True:
    gameStart()
    if not playAgain():
        print("안녕!")
        break
        


# In[35]:





# In[38]:





# In[40]:





# In[46]:





# In[43]:




