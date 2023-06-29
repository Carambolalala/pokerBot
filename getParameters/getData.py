import cv2
import pytesseract
from PIL import Image, ImageDraw
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from fromWindow.winAutoTest import screen
from time import sleep
from cardHash import boardCardHash, handCardHash

#Вспомогательные функции
def medium(pixels):
    summary = 0
    for line in pixels:
        for column in line:
            summary += column
    return summary / 64

def hashSum(card):
    hashSuma = 0
    for line in card:
        for column in line:
            if column == 255:
                hashSuma += 1
    return hashSuma

def hashCard(x, y, x_, y_, board, rotate=False, angle=0):
    thresh = 220
    if rotate == True:
        (h, w) = board.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        board = cv2.warpAffine(board, M, (w, h))
    card = board[y:y_, x:x_]
    card = cv2.resize(card, (8, 8))
    if rotate == True:
        thresh = medium(card)
    card = cv2.threshold(card, thresh, 255, cv2.THRESH_BINARY)[1]
    
    hashSuma = hashSum(card)
    return card, hashSuma

def checkBoardCard(x, y, x_, y_, boardCards, boardCardsSuit):
    card, hashSuma = hashCard(x, y, x_, y_, boardCards)
    px = boardCardsSuit.load()
    #sliced = False
    if hashSuma == 31 or hashSuma == 38 or hashSuma == 41:
        slicedCard = card[0:8, 0:4]
        hashSuma = hashSum(slicedCard)
        #sliced = True
    #if sliced == True:
        #Номинал с учетом slice
        #pass
    #else:
        #Номинал без учета slice
        #pass
    cardNominal = boardCardHash[hashSuma]
    suitPixel = px[x+12, 289][1]
    if suitPixel == 46:
        suit = 'h'
    elif suitPixel == 36:
        suit = 's'
    elif suitPixel == 55:
        suit = 'd'
    else:
        suit = 'c'
    print(card, hashSuma, suitPixel)
    return cardNominal+suit

def checkHandCard(x, y, x_, y_, handCards, handCardsSuit):
    retrunCards = ''
    twoCards = handCards[y:y_, x:x_]
    cards = []
    hashSums = []
    suits = []
    angle = -5
    returnCardsMass = []
    for i in range(2):
        x_1 = 5 + 46*i #55
        y_1 = 5
        x_2 = x_1 + 20
        y_2 = y_1 + 20
        if i == 1:
            angle = -angle
        card, hashSuma = hashCard(x_1, y_1, x_2, y_2, twoCards, rotate=True, angle=angle)
        cards.append(card)
        hashSums.append(hashSuma)
        sliced = False
        if i == 0: #Left
            if hashSuma == 39 or hashSuma == 40:
                sliced = True
                if hashSuma == 39:
                    slicedCard = cards[i][0:8, 0:2]
                    hashSliced = hashSum(slicedCard)
                else:
                    slicedCard = cards[i][0:8, 0:4]
                    hashSliced = hashSum(slicedCard)
        else: #Right
            if hashSuma == 39 or hashSuma == 43:
                sliced = True
                slicedCard = cards[i][0:8, 0:4]
                hashSliced = hashSum(slicedCard)
        if sliced == True:
            returnCardsMass.append(handCardHash[i]['sliced'][hashSuma][hashSliced])
        else:
            returnCardsMass.append(handCardHash[i][hashSuma])
    px = handCardsSuit.load()
    for i in range(2):
        suitPixel = px[383 + 46*i, 492 - 3*i][1]
        #print(suitPixel)
        retrunCards += returnCardsMass[i]
        if suitPixel == 45:
            suits.append('h')
            retrunCards += 'h'
        elif suitPixel == 31:
            suits.append('s')
            retrunCards += 's'
        elif suitPixel == 53:
            suits.append('d')
            retrunCards += 'd'
        else:
            suits.append('c')
            retrunCards += 'c'
        #if i == 0:
         #   if hashSums[i] == 26 or hashSums[i] == 35:
          #      slicedCard = cards[i][0:8, 0:2]
           #     print(slicedCard)
            #    hashSums[i] = hashSum(slicedCard)
        #else:
         #   if hashSums[i] == 33 or hashSums[i] == 34 or hashSums[i] == 35 or hashSums[i] == 36:
          #      slicedCard = cards[i][0:8, 0:2]
           #     print(slicedCard)
            #    hashSums[i] = hashSum(slicedCard)
             #   pass
    for i in range(2):
        pass
    return retrunCards, cards, hashSums

#До Игры
def blind():
    return float(input('Blind: '))
def bank():
    return float(input('Bank: '))

#Универсальные функции
def Raise():
    return float(input('Raise before: '))
def opponentOptions():
    preFlopDesk = Image.open('fromWindow/scad2.png')
    player_2 = preFlopDesk.crop((209, 234, 245, 254))
    drawD_1 = ImageDraw.Draw(player_2)
    drawD_1.text(
        (player_2.width/2+8, player_2.height/2-3),
        'AA'
    )
    player_2.show()
    print(pytesseract.image_to_string(player_2))
def pot():
    return float(input('Pot: '))

#Префлоп
#НАДО БУДЕТ ПРОПИСАТЬ СОЗДАНИЕ СКРИНА ВСЕГО СТОЛА НА ПРЕФЛОПЕ (ДЕЛАЕМ СКРИН СТОЛА, ПОКА НЕ НАСТУПИТ ОЧЕРЕДЬ НАШЕГО ХОДА)
def players():
    preFlopDesk = Image.open('fromWindow/scad2.png') # Переписать, позже он будет называться preFlopDesk.png
    player_3 = preFlopDesk.crop((370, 40, 470, 140))
    isItHere = pytesseract.image_to_string(player_3, 'rus')
    print(isItHere)
def position():
    #D_0 - 185, other - 195
    screen()
    sleep(1)
    preFlopDesk = Image.open('preFlopDesk.png')
    D_0 = preFlopDesk.crop((361, 428, 372, 439))
    px = D_0.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'LP'
    D_1 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_1.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'MP'
    D_2 = preFlopDesk.crop((183, 214, 194, 225))
    px = D_2.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'MP'
    D_3 = preFlopDesk.crop((394, 176, 405, 187))
    px = D_3.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'EP'
    D_4 = preFlopDesk.crop((659, 214, 670, 225))
    px = D_4.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'Blind'
    D_5 = preFlopDesk.crop((666, 403, 677, 414))
    px = D_5.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'Blind'
    return 'EP'
def startHand():
    for i in range(25, 40):
        screen(i) #ченуть, куда сохранит скрин
        sleep(0.5)
        try:
            print('spoq ' + str(i))
            handCards = cv2.imread('spoq' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
            handCardsSuit = Image.open('spoq' + str(i) + '.png')
            x = 367
            y = 450
            x_ = 485
            y_ = 499
            returnCards, cards, hashSums = checkHandCard(x, y, x_, y_, handCards, handCardsSuit)
            for i in range(2):
                print(cards[i])
            print(returnCards)
        except KeyError:
            for i in range(2):
                print(cards[i])
            for i in range(2):
                print(hashSums[i])
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

#Флоп
def flopCards():
    return input('Flop cards withot spaces: ')

#Терн и ривер
def ternRiverCard():
    return input('New card: ')
def newCard(stage):
    returnCards = ''
    boardCards = cv2.imread('fromWindow/spoq24.png', cv2.IMREAD_GRAYSCALE)
    boardCardsSuit = Image.open('fromWindow/spoq24.png')
    x = 252
    y = 258
    x_ = 270
    y_ = 276
    plusPixels = 72
    if stage == 'Flop':
        for i in range(3):
            returnCards += checkBoardCard(x + plusPixels*i, y, x_ + plusPixels*i, y_, boardCards, boardCardsSuit)
    elif stage == 'Tern':
        returnCards += checkBoardCard(x + plusPixels*3, y, x_ + plusPixels*3, y_, boardCards, boardCardsSuit)
    else:
        returnCards += checkBoardCard(x + plusPixels*4, y, x_ + plusPixels*4, y_, boardCards, boardCardsSuit)
    return returnCards
    

startHand()