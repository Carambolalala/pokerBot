from data.picturePower import picturePower, picturePowerRev

#Универсальные функции
def rowForStreet(Card, countCard):
    rowOfCard = []
    for p in range(countCard):
        try:
            rowOfCard.append(int(Card[p*2]))
        except Exception:
            rowOfCard.append(picturePower[Card[p*2]])
    return rowOfCard

def boardCombination(BoardCard, countCardsOnBoard): #Находит комбу на столе 
    Cards = []
    returnBoardCombination = ''
    for p in range(countCardsOnBoard):
        Cards.append(BoardCard[p*2])
    Cards.sort()
    i = 1
    for p in range(countCardsOnBoard):
        if p != 0:
            if Cards[p] == Cards[p-1]:
                i+=1
            else:
                if i == 2:
                    returnBoardCombination += 'double'
                elif i == 3:
                    returnBoardCombination += 'set'
                elif i == 4:
                    returnBoardCombination += 'kare'
                i = 1
    if i == 2:
        returnBoardCombination += 'double'
    elif i == 3:
        returnBoardCombination += 'set'
    elif i == 4:
        returnBoardCombination += 'kare'
    return returnBoardCombination

def handCombination(HandCard, BoardCard, BoardCombination, countCardsOnBoard): #Находит комбу с учетом карт на руке
    i = 0
    r = 0
    for p in range(countCardsOnBoard):
        if HandCard[0] == BoardCard[p*2]:
            i += 1
    if HandCard[0] == HandCard[2]:
        i += 1
    else:
        for p in range(countCardsOnBoard):
            if HandCard[2] == BoardCard[p*2]:
                r += 1
    returnCombination = ''
    if i == 1:
        returnCombination += 'double'
    elif i == 2:
        returnCombination += 'set'
    elif i == 3:
        returnCombination += 'kare'
    if r == 1:
        returnCombination += 'double'
    elif r == 2:
        returnCombination += 'set'
    elif r == 3:
        returnCombination += 'kare'

    if (returnCombination == 'double' or returnCombination == 'set') and (BoardCombination == 'double' or BoardCombination == 'set'):
        returnCombination += BoardCombination
    
    if returnCombination == 'setset':
        returnCombination = 'set'

    mbStreetFlash = ''
    rowOfCard = rowForStreet(BoardCard, countCardsOnBoard)
    rowOfHandCard = rowForStreet(HandCard, 2)
    for el in rowOfHandCard:
        rowOfCard.append(el)
    rowOfCard.sort()
    i = 1
    for p in range(countCardsOnBoard+2):
        if p != 0:
            if abs(rowOfCard[p] - rowOfCard[p-1]) == 1:
                i += 1
    if i == 5:
        mbStreetFlash += 'street'
    i = 0
    if HandCard[1] == HandCard[3]:
        i += 1
    Suits = []
    for p in range(countCardsOnBoard):
        Suits.append(BoardCard[p*2+1])
    Suits.sort()
    r = 1
    r_max = 0
    for p in range(countCardsOnBoard):
        if p != 0:
            if Suits[p] == Suits[p-1]:
                r += 1
                if r > r_max:
                    r_max = r
                    flashSuit = Suits[p-1]
            else:
                r = 1
    if HandCard[1] == HandCard[3]:
        if r_max >= 3:
            if HandCard[1] == flashSuit:
                mbStreetFlash += 'flash'
    else:
        if r_max >= 4:
            if HandCard[1] == flashSuit or HandCard[3] == flashSuit:
                mbStreetFlash += 'flash'
    if mbStreetFlash == 'street' or mbStreetFlash == 'flash' or mbStreetFlash == 'streetflash':
        if mbStreetFlash != 'streetflash':
            if returnCombination != 'kare' and returnCombination != 'doubleset' and returnCombination != 'setdouble':
                returnCombination = mbStreetFlash
        else:
            returnCombination = mbStreetFlash

    return returnCombination

def boardFlashDro(BoardCard, countBoardCards):
    Suits = []
    for p in range(countBoardCards):
        Suits.append(BoardCard[p*2+1])
    Suits.sort()
    i = 0
    i_max = 1
    for p in range(countBoardCards):
        if Suits[p] == Suits[p-1]:
            i += 1
        else:
            if i > i_max:
                i_max = i
            i = 1
    if i > i_max:
        i_max = i
    if i_max == 2:
        return 'flashdro'
    elif i_max == 3:
        return 'flash'
    return ''

def boardStreetDro(BoardCard, countBoardCard):
    rowOfCard = rowForStreet(BoardCard, countBoardCard)
    rowOfCard.sort()
    i = 1
    i_max = 1
    for p in range(countBoardCard):
        if p != 0:
            if rowOfCard[p] - rowOfCard[p-1] == 1:
                i += 1
            else:
                if i > i_max:
                    i_max = i
                i = 1
    if i >= 3:
        return 'street'
    return ''

def handStreetDro(HandCard, BoardCard, countBoardCard):
    rowOfCard = rowForStreet(BoardCard, countBoardCard)
    rowOfHandCard = rowForStreet(HandCard, 2)
    for el in rowOfHandCard:
        rowOfCard.append(el)
    rowOfCard.sort()
    i = 0
    r_1 = 0
    r_2 = 0
    for el in rowOfCard:
        if i != 0:
            if el - rowOfCard[i-1] == 1:
                r_1 += 1
                match r_1:
                    case 1:
                        mbCard_1 = rowOfCard[i-1] - 1
            elif el - rowOfCard[i-1] == 2:
                r_2 += 1
                match r_2:
                    case 1:
                        mbCard_2 = rowOfCard[i] - 1
        i += 1
    if r_1 == 3:
        if mbCard_1 == 1:
            return 'minstreetdro', '6'
        elif mbCard_1 == 10:
            return 'minstreetdro', 'T'
        else:
            mbCard_2 = mbCard_1 + 5
            if mbCard_2 >= 10:
                mbCard_2 = picturePowerRev[mbCard_2]
            else:
                mbCard_2 = str(mbCard_2)
        return 'streetdro', str(mbCard_1)+mbCard_2
    elif r_2 == 1 and r_1 == 2:
        if mbCard_2 >= 10:
            mbCard_2 = picturePowerRev[mbCard_2]
        else:
            mbCard_2 = str(mbCard_2)
        return 'minstreetdro', mbCard_2
    return '', ''

def handFlashDro(HandCard, BoardCard, countBoardCard):
    i = 1
    if HandCard[1] == HandCard[3]:
        HandSuits = HandCard[1]
        i += 1
    else:
        HandSuits = HandCard[1] + HandCard[3]
    BoardSuits = ''
    for p in range(countBoardCard):
        BoardSuits += BoardCard[p*2+1]
    for handEl in HandSuits:
        for boardEl in BoardSuits:
            if handEl == boardEl:
                i += 1
            if i == 4:
                return 'flashdro', handEl
    return '', ''

def outsCount(HandCombination, Dro):
    outs = 0
    match Dro:
        case 'flashdro':
            outs += 9
        case 'minstreetdro':
            outs += 4
        case 'streetdro':
            outs += 8
        case 'flashdrominstreetdro':
            outs += 12
        case 'flashdrostreetdro':
            outs += 15
    match HandCombination:
        case 'double':
            outs += 2
        case 'set':
            outs += 1
        case 'doubledouble':
            outs += 4
    return outs

#Функции анализа
# Префлоп
def cardCategory(Hand): #Анализирует категорию стартовой руки
    HandNoSuit = Hand[:1] + Hand[2:3]
    if HandNoSuit[0] == HandNoSuit[1]: # Пары
        if HandNoSuit[0] == 'A' or HandNoSuit[0] == 'K' or HandNoSuit[0] == 'Q':
            return 'highDouble'
        elif HandNoSuit[0] == 'J' or HandNoSuit[0] == 'T':
            return 'middleDouble'
        else:
            return 'juniorDouble'
    if HandNoSuit.find('A') != -1: # Тузы
        other = HandNoSuit.replace('A', '')
        if other == 'K':
            return 'highAces'
        elif other == 'Q' or other == 'J' or other == 'T':
            return 'middleAces'
        else:
            if Hand[1] == Hand[3]:
                return 'juniorAcesSuited'
    if (HandNoSuit.find('T') != -1) or (HandNoSuit.find('J') != -1) or (HandNoSuit.find('Q') != -1): # Картинки
        ia = HandNoSuit.replace('K', '')
        ib = ia.replace('Q', '')
        ic = ib.replace('J', '')
        if ic == 'T' or ic == '':
            if Hand[1] == Hand[3]:
                return 'picturesSuited'
            else:
                return 'picturesOfsuited'
    if Hand[1] == Hand[3]:
        try:
            Hand_1 = int(HandNoSuit[0])
        except Exception:
            Hand_1 = picturePower[HandNoSuit[0]]
        try:
            Hand_2 = int(HandNoSuit[1])
        except Exception:
            Hand_2 = picturePower[HandNoSuit[1]]
        odd = abs(Hand_1-Hand_2)
        if odd == 1:
            return 'connectorSuited'
    
    return 'foldHand'

def positionCategory(): #Выдает категорию позиции
    return input('Position category: ')

def isItDouble(CardCategory):
    if CardCategory[-6:-5] == 'D':
        return 'double'
    return ''

"""
def flopBoardCombination(BoardCard): #Находит комбу на столе (пара или сет)
    if BoardCard[0] == BoardCard[2] or BoardCard[0] == BoardCard[4] or BoardCard[2] == BoardCard[4]:
        if BoardCard[0] == BoardCard[2] and BoardCard[2] == BoardCard[4]:
            return 'set'
        else:
            return 'double'
    return ''


def flopHandCombination(HandCard, BoardCard, HandCombination): #Находит комбу с учетом карт на руке
    i = 0
    r = 0
    for p in range(3):
        if HandCard[0] == BoardCard[p*2]:
            i += 1
    if HandCombination == 'double':
        i += 1
    else:
        for p in range(3):
            if HandCard[2] == BoardCard[p*2]:
                r += 1
    returnCombination = ''
    if i == 1:
        returnCombination += 'double'
    elif i == 2:
        returnCombination += 'set'
    elif i == 3:
        returnCombination += 'kare'
    if r == 1:
        returnCombination += 'double'
    elif r == 2:
        returnCombination += 'set'
    elif r == 3:
        returnCombination += 'kare'

    mbStreetFlash = ''
    rowOfCard = rowForStreet(BoardCard, 3)
    rowOfHandCard = rowForStreet(HandCard, 2)
    for el in rowOfHandCard:
        rowOfCard.append(el)
    rowOfCard.sort()
    i = 1
    while i <= 4:
        if abs(rowOfCard[i] - rowOfCard[i-1]) != 1:
            break
        i += 1
    if i == 5:
        mbStreetFlash += 'street'
    if HandCard[1] == HandCard[3]:
        if HandCard[1] == BoardCard[1] and BoardCard[1] == BoardCard[3] and BoardCard[3] == BoardCard[5]:
            mbStreetFlash += 'flash'
    if mbStreetFlash == 'street' or mbStreetFlash == 'flash' or mbStreetFlash == 'streetflash':
        if mbStreetFlash != 'streetflash':
            if returnCombination != 'kare' and returnCombination != 'doubleset' and returnCombination != 'setdouble':
                returnCombination = mbStreetFlash
        else:
            returnCombination = mbStreetFlash

    return returnCombination

    
def boardFlashDro(BoardCard):
    suits = BoardCard[1] + BoardCard[3] + BoardCard[5]
    i = 0
    if suits[0] == suits[1]:
        i += 1
    if suits[1] == suits[2]:
        i += 1
    if suits[2] == suits[0]:
        i += 1
    if i == 1:
        return 'flashdro'
    elif i == 3:
        return 'flash'
    return ''


def boardStreetDro(BoardCard):
    rowOfCard = rowForStreet(BoardCard, 3)
    p = 0
    r = 0
    for el in rowOfCard:
        if p != 0:
            if el - rowOfCard[p-1] == 1:
                r += 1
        p += 1
    if r == 2:
        return 'street'
    return ''

def handStreetDro(HandCard, BoardCard):
    rowOfCard = rowForStreet(BoardCard, 3)
    rowOfHandCard = rowForStreet(HandCard, 2)
    for el in rowOfHandCard:
        rowOfCard.append(el)
    rowOfCard.sort()
    i = 0
    r_1 = 0
    r_2 = 0
    for el in rowOfCard:
        if i != 0:
            if el - rowOfCard[i-1] == 1:
                r_1 += 1
                match r_1:
                    case 1:
                        mbCard_1 = rowOfCard[i-1] - 1
            elif el - rowOfCard[i-1] == 2:
                r_2 += 1
                match r_2:
                    case 1:
                        mbCard_2 = rowOfCard[i] - 1
        i += 1
    if r_1 == 3:
        if mbCard_1 == 1:
            return 'minstreetdro', '6'
        elif mbCard_1 == 10:
            return 'minstreetdro', 'T'
        else:
            mbCard_2 = mbCard_1 + 5
            if mbCard_2 >= 10:
                mbCard_2 = picturePowerRev[mbCard_2]
            else:
                mbCard_2 = str(mbCard_2)
        return 'streetdro', str(mbCard_1)+mbCard_2
    elif r_2 == 1 and r_1 == 2:
        if mbCard_2 >= 10:
            mbCard_2 = picturePowerRev[mbCard_2]
        else:
            mbCard_2 = str(mbCard_2)
        return 'minstreetdro', mbCard_2
    return '', ''

def handFlashDro(HandCard, BoardCard):
    p = 0
    if HandCard[1] == HandCard[3]:
        HandSuits = HandCard[1]
        p += 1
    else:
        HandSuits = HandCard[1] + HandCard[3]
    BoardSuits = BoardCard[1] + BoardCard[3] + BoardCard[5]
    for handEl in HandSuits:
        f = p
        for boardEl in BoardSuits:
            if handEl == boardEl:
                f += 1
            if f == 3:
                return 'flashdro', handEl
    return '', ''
"""



