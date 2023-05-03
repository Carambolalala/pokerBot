from data.picturePower import picturePower, picturePowerRev
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
        odd = abs(int(HandNoSuit[0]) - int(HandNoSuit[1]))
        if odd == 1:
            return 'connectorSuited'
    
    return 'foldHand'

def positionCategory(Position): #Выдает категорию позиции
    if Position <= 3:
        return 'EP'
    if Position <= 6:
        return 'MP'
    if Position == 7:
        return 'LP'
    return 'Blind'

def isItDouble(CardCategory):
    if CardCategory[-6:-5] == 'D':
        return 'double'
    return ''

# Флоп
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

    rowOfCard = []
    mbStreetFlash = ''
    for p in range(3):
        try:
            rowOfCard.append(int(BoardCard[p*2]))
        except Exception:
            rowOfCard.append(picturePower[BoardCard[p*2]])
    for p in range(2):
        try:
            rowOfCard.append(int(HandCard[p*2]))
        except Exception:
            rowOfCard.append(picturePower[HandCard[p*2]])
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

def handStreetDro(HandCard, BoardCard):
    rowOfCard = []
    for p in range(3):
        try:
            rowOfCard.append(int(BoardCard[p*2]))
        except Exception:
            rowOfCard.append(picturePower[BoardCard[p*2]])
    for p in range(2):
        try:
            rowOfCard.append(int(HandCard[p*2]))
        except Exception:
            rowOfCard.append(picturePower[HandCard[p*2]])
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
        findSuit = HandSuits
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