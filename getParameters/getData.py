import cv2
import pytesseract
from PIL import Image, ImageDraw
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from fromWindow.winAutoTest import screen
from time import sleep

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

def hashCard(x, y, x_, y_, board):
    card = board[y:y_, x:x_]
    angle = 1.3
    #if rotate:
    #    (h, w) = card.shape[:2]
    #    center = (w / 2, h / 2)
    #    M = cv2.getRotationMatrix2D(center, 4, 1.0)
    #    card = cv2.warpAffine(card, M, (w, h))
    card = cv2.resize(card, (8, 8))
    thresh = medium(card)
    card = cv2.threshold(card, thresh, 255, cv2.THRESH_BINARY)[1]
    hashSuma = hashSum(card)
    return card, hashSuma

def checkBoardCard(x, y, x_, y_, boardCards, boardCardsSuit, hand=False):
    card, hashSuma = hashCard(x, y, x_, y_, boardCards)
    px = boardCardsSuit.load()
    sliced = False
    if hand == False:
        if hashSuma == 25 or hashSuma == 24:
            slicedCard = card[0:8, 0:4]
            hashSuma = hashSum(slicedCard)
            sliced = True
        if sliced == True:
            if hashSuma == 11:
                hashSuma = hashSum(card)
                #Номинал без учета slice
            #Номинал с учетом slice
        else:
            #Номинал без учета slice
            pass
    else:
        pass
    cardNominal = 'A'
    suitPixel = px[x_+10, 265][1]
    if suitPixel == 17:
        suit = 'h'
    elif suitPixel == 134:
        suit = 'c'
    elif suitPixel == 77:
        suit = 'd'
    else:
        suit = 's'
    print(card, hashSuma, suitPixel)
    return cardNominal+suit


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
    returnCards = ''
    boardCards = cv2.imread('fromWindow/scad4.png', cv2.IMREAD_GRAYSCALE)
    boardCardsSuit = Image.open('fromWindow/scad5.png')
    x = 373
    y = 461
    x_ = 392
    y_ = 480
    for i in range(2):
        returnCards += checkBoardCard(x + 46*i, y - 4*i, x_ + 46*i, y_ - 4*i, boardCards, boardCardsSuit, True)
    return returnCards

#Флоп
def flopCards():
    return input('Flop cards withot spaces: ')

#Терн и ривер
def ternRiverCard():
    return input('New card: ')
def newCard(stage):
    returnCards = ''
    boardCards = cv2.imread('fromWindow/scad1.png', cv2.IMREAD_GRAYSCALE)
    boardCardsSuit = Image.open('fromWindow/scad1.png')
    x = 253
    y = 258
    x_ = 272
    y_ = 277
    plusPixels = 72
    if stage == 'Flop':
        for i in range(3):
            returnCards += checkBoardCard(x + plusPixels*i, y, x_ + plusPixels*i, y_, boardCards, boardCardsSuit)
    elif stage == 'Tern':
        returnCards += checkBoardCard(x + plusPixels*3, y, x_ + plusPixels*3, y_, boardCards, boardCardsSuit)
    else:
        returnCards += checkBoardCard(x + plusPixels*4, y, x_ + plusPixels*4, y_, boardCards, boardCardsSuit)
    return returnCards
    

print(startHand())