from data.comboStartHand import comboStartHand
from data.outRate import outRate
from data.optionByDro import optionByDro

from getParameters import getData
import analyse

def flopTernRiver(Hand, Bank, BoardCards, countBoardCard, nextStage, Distance):
    Scare = ''
    BoardCombination = analyse.boardCombination(BoardCards, countBoardCard)
    HandCombination = analyse.handCombination(Hand, BoardCards, BoardCombination, countBoardCard)
    FlashDro = ''
    StreetDro = ''
    if HandCombination != 'doubleset' and HandCombination != 'setdouble' and HandCombination != 'kare':
        if HandCombination != 'flash':
            if countBoardCard != 5:
                FlashDro, FlashSuit = analyse.handFlashDro(Hand, BoardCards, countBoardCard)
            if FlashDro != 'flashdro':
                Scare += analyse.boardFlashDro(BoardCards, countBoardCard)
        if HandCombination != 'street' and HandCombination != 'flash':
            if countBoardCard != 5:
                StreetDro, StreetCards = analyse.handStreetDro(Hand, BoardCards, countBoardCard)
            if StreetDro != 'streetdro' and StreetDro != 'minstreetdro':
                Scare += analyse.boardStreetDro(BoardCards, countBoardCard)
    Dro = FlashDro + StreetDro
    print('Hand combination: ', HandCombination, ' // Dro: ', Dro)
    Outs = analyse.outsCount(HandCombination, Dro)

    OpponentOptions = getData.opponentOptions() # str 'Raise' - raise, 'Fold' - all fold, 'Call' - some call, 'Check' - check
    Option = optionByDro[HandCombination][Scare][OpponentOptions]
    if OpponentOptions == 'Raise' or OpponentOptions == 'Call':
        Bet = getData.Raise()
    if Option == 'Cheap':
        Pot = getData.pot()
        if Pot / Bet >= outRate[nextStage][Outs]:
            Option = 'Call'
        else:
            Option = 'Fold'
    elif Option == 'Call20':
        if Bank / (3 * Bet) >= Distance:
            Option = 'Call'
            Bank -= Bet
        else:
            Option = 'Fold'
    return Bank, Option

#доПрефлоп
Distance = 10 # Изменяемо
Blind = getData.blind() # float
Bank = getData.bank() # float

#ОСНОВНОЙ ЦИКЛ ИГРЫ
while True:
    # Префлоп
    FoldOption = False
    #Players = getData.players() # int
    #Position = getData.position() #int
    Hand = getData.startHand() # str

    CardCategory = analyse.cardCategory(Hand)
    PositionCategory = analyse.positionCategory()
    HandCombination = analyse.isItDouble(CardCategory)
    while True:
        OpponentOptions = getData.opponentOptions() # str 'Raise' - raise, 'Fold' - all fold, 'Call' - some call
        Option = comboStartHand[CardCategory][OpponentOptions][PositionCategory]
        if Option == 'Call20':
            Bet = getData.Raise()
            if Bank / Bet >= Distance:
                Option = 'Call'
                Bank -= Bet
            else:
                Option = 'Fold'
        if Option == 'Fold':
            FoldOption = True
        print('Required option:  ' + Option)
        Continue = input('Continiue? (y/n): ')
        if Continue == 'y':
            break
    print('#######################################################')
    if FoldOption:
        continue
    # Флоп
    BoardCards = getData.flopCards() # str
    while True:
        Bank, Option = flopTernRiver(Hand, Bank, BoardCards, 3, 'Tern', Distance)
        print('Required option: ', Option)
        if Option == 'Fold':
            FoldOption = True
        Continue = input('Continue? (y/n): ')
        if Continue == 'y':
            break
    print('#######################################################')
    if FoldOption:
        continue
        
    # Терн
    NewCard = getData.ternRiverCard()
    BoardCards += NewCard
    while True:
        Bank, Option = flopTernRiver(Hand, Bank, BoardCards, 4, 'River', Distance)
        print('Required option: ', Option)
        if Option == 'Fold':
            FoldOption = True
        Continue = input('Continue? (y/n): ')
        if Continue == 'y':
            break
    print('#######################################################')
    if FoldOption:
        continue

    # Ривер
    NewCard = getData.ternRiverCard()
    BoardCards += NewCard
    while True:
        Bank, Option = flopTernRiver(Hand, Bank, BoardCards, 5, '', Distance)
        print('Required option: ', Option)
        if Option == 'Fold':
            FoldOption = True
        Continue = input('Continue? (y/n): ')
        if Continue == 'y':
            break
    print('#######################################################')
    if FoldOption:
        continue
####################################

"""
    Scare = ''
    BoardCards = getData.flopCards() # str
    FlopBoardCombination = analyse.boardCombination(BoardCards)
    HandCombination = analyse.handCombination(Hand, BoardCards, FlopBoardCombination, 3)
    if HandCombination != 'flash':
        FlashDro, FlashSuit = analyse.handFlashDro(Hand, BoardCards)
        if FlashDro != 'flashdro':
            Scare += analyse.boardFlashDro(Hand, BoardCards, 3)
    if HandCombination != 'street' and HandCombination != 'flash':
        StreetDro, StreetCards = analyse.handStreetDro(Hand, BoardCards)
        if StreetDro != 'streetdro' or StreetDro != 'minstreetdro':
            Scare += analyse.boardStreetDro(BoardCards, 3)
    Dro = FlashDro + StreetDro
    Outs = analyse.outsCount(HandCombination, Dro)

    OpponentOptions = getData.opponentOptions() # str 'Raise' - raise, 'Fold' - all fold, 'Call' - some call, 'Check' - check
    Option = optionByDro[HandCombination][Scare][OpponentOptions]
    if OpponentOptions == 'Raise' or OpponentOptions == 'Call':
        Bet = getData.Raise()
    if Option != 'Cheap' and Option != 'Call20':
        print(Option)
    elif Option == 'Cheap':
        Pot = getData.pot()
        if Pot / Bet >= outRate['Tern'][Outs]:
            print('Call')
        else:
            print('Fold')
    elif Option == 'Call20':
        if Bank / (3 * Bet) >= 20:
            print('Call')
        else:
            print('Fold')
    """