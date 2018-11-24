
# coding: utf-8

# In[1]:


### 젓가락을 만들자
# Chopsticks game


# In[2]:


import random


# In[3]:


def gameStart(): # 게임 시작
    
    print()
    
    print("몇인용으로 게임을 하시겠습니까? > (2 or 3 or 4)")
    p = int(input())
    
    playerList = []
    
    for i in range(0,p):
        print(str(i)+"번 플레이어의 이름을 입력하시오. > ")
        playerList.append(player(input()))
    
    random.shuffle(playerList)
    
    a = ""
    for i in playerList:
        a += i.getName() + " "
    
    print("게임이 " + a + "순으로 진행됩니다.")
    turn = playerList[0]
    
    counts = 0
    print()
    
    while True:
        print()
        if playerList[int(counts%p)].canPlay() == 1:
            doTurn(playerList[(counts%p)], playerList)
            
            print()
            if showPlayerFingers(playerList):
                break
        counts += 1
 
    print()
    for i in playerList:
        if playerList[i].canPlay() == 1:
            print(i.getName() +"(이)가 승리했습니다!")
    
    print(str(int(counts/p)) + '턴 만에 끝났습니다.')


# In[4]:


def doTurn(person, playerList):
    print(person.getName(), "의 차례입니다.", sep = "")
    print("무엇을 하시겠습니까?")
    while True:
        both_fingers = person.leftHand.getFingers() + person.rightHand.getFingers()
        if both_fingers not in [2, 3, 4, 5, 6]:
            a = ""
            if person.leftHand.getFingers() > 0:
                a += "1. 왼손 공격 "
            if person.rightHand.getFingers() > 0:
                a += "2. 오른손 공격 "
            print(a)
            if do is 1:
                attackOtherPlayer(person.leftHand, person, playerList)
                break
            elif do is 2:
                attackOtherPlayer(person.rightHand, person, playerList)
                break
            else:
                print("잘못된 입력입니다.")
        else:
            a = ""
            if person.leftHand.getFingers() > 0:
                a += "1. 왼손 공격 "
            if person.rightHand.getFingers() > 0:
                a += "2. 오른손 공격 "
            print(a + "3. 바꾸기")
            do = int(input())
            if do is 1:
                attackOtherPlayer(person.leftHand, person, playerList)
                break
            elif do is 2:
                attackOtherPlayer(person.rightHand, person, playerList)
                break
            elif do is 3:
                person.reconstruct()
                break
            else:
                print("잘못된 입력입니다.")


# In[13]:


def choice(person, playerList):
    a = ""
    count = 0
    for i in playerList:
        if i != person and i.canPlay() == 1:
            a += str(count) + i.getName() + " "
        count += 1
    return a


# In[6]:


def playAgain():
    print('게임을 다시 하시겠습니까? (yes or no)')
    return input().lower().startswith('y')


# In[7]:


def attackOtherPlayer(hand, person, playerList):
    
    print("공격하고 싶은 사람을 고르시오 " + choice(person, playerList) + "  > ", end = "")
    
    otherPlayer = playerList[int(input())]
    
    b = ""
    if otherPlayer.leftHand.getFingers() > 0:
        b += "1. 왼손"
    if otherPlayer.rightHand.getFingers() > 0:
        b += "  2. 오른손"
    
    print("상대 손을 선택하시오  " + b + "  > " , end = "")
    o = int(input())
    if o == 1:
        attack(hand, otherPlayer.leftHand)
    else:
        attack(hand, otherPlayer.rightHand)
    
    
def attack(hand1, hand2):
    attacked = hand1.getFingers() + hand2.getFingers()
    if attacked >= 5:
        attacked = 0
        print("상대방의 손이 격파되었습니다.")
    else:
        print("공격받은 손의 손가락 수는", attacked, "개 입니다.")
        
    hand2.setFingers(attacked)
    return


# In[8]:


### 손 객체
### 손가락의 수를 가지고 있음

class hand:
    def __init__(self):
        self.fingers = 1
    
    def getFingers(self):
        return self.fingers

    def setFingers(self, k):
        self.fingers = k
        


# In[9]:


finger_construct_list = {2:[[0, 2], [1, 1], [2, 0]], 3:[[0, 3], [1, 2], [2, 1], [3, 0]], 4:[[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]], 5:[[1, 4], [2, 3], [3, 2], [4, 1]], 6:[[2, 4], [3, 3], [4, 2]]}


# In[10]:


### 플레이어 객체
### 플레이어 네임과 2개의 손을 가지고 있음


class player:
    def __init__(self, name="Player"):
        self.name = name
        self.leftHand = hand()
        self.rightHand = hand()
        self.can = 1
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def die(self):
        self.can = 0
    
    def canPlay(self):
        return self.can
    
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


# In[15]:


def showPlayerFingers(playerList):
    for i in playerList:
        if(i.leftHand.getFingers() == 0 and i.rightHand.getFingers() == 0):
            print(i.getName() + " 탈락!")
            i.die()

    diePerson = 0
    for i in playerList:
        if i.canPlay() == 1:
            print(i.getName() + "의 손가락 현황")
            i.showFingers()
        else:
            diePerson += 1
    
    return (diePerson + 1 == len(playerList))


# In[16]:


print("젓가락 게임을 해볼까요?")

while True:
    gameStart()
    if not playAgain():
        print("안녕!")
        break

