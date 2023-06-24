from ..data.picturePower import picturePower

cardPresets = [
    [], #2
    [], #3
    [], #4
    [], #5
    [], #6
    [], #7
    [], #8
    [], #9
    [], #T
    [], #J
    [], #Q
    [], #K
    [], #A
]

def getCard(card):
    i = 1
    for el in cardPresets:
        i += 1
        if card == cardPresets:
            if i >= 10:
                return picturePower[i]
            return str(i)