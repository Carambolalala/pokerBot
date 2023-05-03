from data.comboStartHand import comboStartHand
from data.outRate import outRate

from getParameters import getData
import analyse

#доПрефлоп
#Blind = getData.blind() # float
#Bank = getData.bank() # float

#ОСНОВНОЙ ЦИКЛ ИГРЫ
while True:
    # Префлоп - ПЕРЕПИСАТЬ НА СЛУЧАЙ РЕРЕЙЗА ИЛИ РЕЙЗА ПОСЛЕ НАС
    #Players = getData.players() # int
    Position = getData.position() #int
    Hand = getData.startHand() # str
    OpponentOptions = getData.opponentOptions() # str 'R' - raise, 'F' - all fold, 'C' - some call

    CardCategory = analyse.cardCategory(Hand)
    PositionCategory = analyse.positionCategory(Position)
    HandCombination = analyse.isItDouble(CardCategory)
    print('Required option:  ' + comboStartHand[CardCategory][OpponentOptions][PositionCategory])
    print('#######################################################')
    
    # Флоп
    BoardCards = getData.flopCards() # str
    FlopBoardCombination = analyse.flopBoardCombination(BoardCards)
    HandCombination = analyse.flopHandCombination(Hand, BoardCards, HandCombination)
    if HandCombination == 'double':
        HandCombination += FlopBoardCombination
    if HandCombination != 'flash':
        FlashDro, FlashSuit = analyse.handFlashDro(Hand, BoardCards)
    if HandCombination != 'street':
        StreetDro, StreetCards = analyse.handStreetDro(Hand, BoardCards)
    if HandCombination == 'street':
        Scare = analyse.boardFlashDro(BoardCards)
    Dro = FlashDro + StreetDro
    Outs = analyse.outsCount(HandCombination, Dro)
    
    OpponentOptions = getData.opponentOptions() # str 'R' - raise, 'F' - all fold, 'C' - some call, 'Ch' - check


    break
####################################
