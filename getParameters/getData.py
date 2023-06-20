import cv2
import pytesseract
from PIL import Image, ImageDraw
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from fromWindow.winAutoTest import screen
from time import sleep
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
    preFlopDesk = cv2.imread('fromWindow/scad3.png', cv2.IMREAD_GRAYSCALE)
    x = 470
    y = 259
    x_ = 491
    y_ = 280
    #x = 373
    #y = 462
    #x_ = 394
    #y_ = 483
    thresh = 128
    firstCard = preFlopDesk[y:y_, x:x_]
    firstCard = cv2.resize(firstCard, (8, 8))
    firstCard = cv2.threshold(firstCard, thresh, 255, cv2.THRESH_BINARY)[1]
    hashSum = 0
    for line in firstCard:
        for column in line:
            if column == 255:
                hashSum += 1
    print(hashSum)
    print(firstCard)

#Флоп
def flopCards():
    return input('Flop cards withot spaces: ')

#Терн и ривер
def ternRiverCard():
    return input('New card: ')
startHand()