
import cv2
import numpy
import time
import random
import os

global n
global pc_win
global you_win
you_win = pc_win = 0
n = 0

def process( ):
    # This processes what just happened in the game
    #create 3x3 array
    # rock: 0
    # scissors: 1
    # paper: 2
    print 'processing'
    img = cv2.imread("wif.jpg",0)
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))
    dilate = cv2.dilate(img, element)
    erode = cv2.erode(img, element)
    result = cv2.absdiff(dilate,erode);
    retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY);

    #get the anti-color
    result = cv2.bitwise_not(result);
    result =cv2.medianBlur(result,23)
    a=[]
    posi =[]
    width =[]
    count = 0
    area = 0
    for i in range(result.shape[1]):
        for j in range(result.shape[0]):
            if(result[j][i] == 0):
                area += 1
    for i in range(result.shape[1]):
        if(result[5*result.shape[0]/16][i] == 0 and result[5*result.shape[0]/16][i-1]!= 0 ):
            count += 1
            width.append(0)
            posi.append(i)
        if(result[5*result.shape[0]/16][i] == 0):
            width[count-1] += 1
    #time juged
    width_length = 0
    width_jiandao = True
    for i in range(count):
        if width[i] > 45:
            #paper
	    return 2;

        if width[i] <= 20 or width[i] >= 40:
            width_jiandao = False
        width_length += width[i]
    if width_jiandao == True and count == 2:
        #SCISSORS
	return 1;

    if(area < 8500):
        #ROCK
        return 0;
    print "width_leng",width_length
    if(width_length<35):
        #re-determaintion
        a = []
        posi =[]
        width =[]
        count = 0
        for i in range(result.shape[1]):
            if (result[ 11 * result.shape[0]/16][i] == 0 and result[ 11 * result.shape[0]/16][i-1] != 0 ):
                count += 1
                width.append(0)
                posi.append(i)
            if (result[11*result.shape[0]/16][i] == 0):
                width[count-1] += 1

    width_length=0
    width_jiandao = True
    for i in range(count):
        if width[i] > 45:
            #paper
            return 2;
        if width[i] <= 20 or width[i] >= 40:
            width_jiandao= False
        width_length += width[i]
    if width_jiandao == True and count == 2:
        #scissors!!!
	return 1;
    if(area > 14000 or count >= 3):
        #paper
        return 2;
    if(width_length < 110):
        #scissssors
        return 1;
    else:
        #paper
        return 2;

def game():
    global n
    move =[]
    move.append("Rock")
    move.append("scissors")
    move.append("paper")
    move.append("errorgestures")
    capture = cv2.VideoCapture(0)
    cv2.namedWindow("camera",1)
    start_time = time.time()
    print("set your hands in top right square!\n")
    while(1):
        (ha,img) = capture.read()
        end_time = time.time()
        cv2.rectangle(img,(426,0),(640,250),(170,170,0))
        cv2.putText(img,str(int((10-(end_time- start_time)))), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        cv2.imshow("camera",img)
        if(end_time-start_time>10):
            break
        if(cv2.waitKey(30)>=0):
            break
    ha,img = capture.read()
    capture.release()
    img = img[0:210,426:640]
    cv2.imwrite("wif.jpg",img)
    p1 = process()

    print "your move was: ",move[p1],"\n"
    
    #generate what move PC did
    pcNum = random.randint(0,3)
    print "pc move was: ", move[pcNum],"\n"
    scoreCalc(pcNum, p1)     

    cv2.imshow("camera",img)
    cv2.destroyAllWindows()
    return 1

def scoreCalc(pc, userMove):
    global pc_win
    global you_win

    if( (pc == 0  and userMove == 1 ) or (pc == 1 and userMove == 2) or (pc == 2 and userMove ==0)):
        print "PC wins this round!"
        pc_win += 1

    if((userMove == 0 and pc == 1) or (userMove == 1 and pc == 2) or (userMove == 2 and pc == 0)):
        print "Player wins this round!"
        you_win += 1

    if((userMove == 0 and pc == 0) or (userMove == 1 and pc == 1) or (userMove == 2 and pc ==2)):
    #if tie function prints out its a tie
        print "Its a tie!" #Print in GUI
    return  



#This is the main 
print("Press enter to start :-)\n")
s = raw_input()
global you_win
global pc_win
while(you_win < 4 or pc_win < 4):
#since it's a best of 3 game
    print "You vs PC: ",you_win,":",pc_win,'\n'
    #os.system('clear') #kinda annoying
    game()
if (you_win < 4):
    print 'You won!'
if (pc_win < 4):
    print 'PC won!'
