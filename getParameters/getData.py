import pytesseract
from PIL import Image, ImageDraw
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

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
    preFlopDesk = Image.open('fromWindow/scad1.png')
    D_0 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_0.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'LP'
    D_1 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_1.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'MP'
    D_2 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_2.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'MP'
    D_3 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_3.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'EP'
    D_4 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_4.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'Blind'
    D_5 = preFlopDesk.crop((176, 402, 187, 413))
    px = D_5.load()
    if px[6, 6][1] > 179 and px[6, 6][1] < 201:
        return 'Blind'
def startHand():
    preFlopDesk = Image.open('fromWindow/scad1.png')
    card_1 = preFlopDesk.crop((269, 289, 400, 336))
    isItHere = pytesseract.image_to_string(card_1, 'rus')
    print(isItHere)

#Флоп
def flopCards():
    return input('Flop cards withot spaces: ')

#Терн и ривер
def ternRiverCard():
    return input('New card: ')
startHand()