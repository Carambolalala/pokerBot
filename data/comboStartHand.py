#КОМБА -> ДЕЙСТВИЯ ОППОНЕНТОВ -> ПОЗИЦИЯ
#EP - ранняя позиция, МР - средняя позиция, LP - поздняя позиция
comboStartHand = {
    'highDouble': { #Старшие пары
        'Fold': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        },
        'Raise': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        }
    },
    'middleDouble': { #Средние пары
        'Fold': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        },
        'Raise': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'juniorDouble': { #Младшие пары
        'Fold': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Call' 
        },
        'Call': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'highAces': { #Сильные тузы
        'Fold': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        },
        'Raise': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        }
    },
    'middleAces': { #Средние тузы
        'Fold': {
            'EP': 'Call',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'juniorAcesSuited': { #Малые одномастные тузы
        'Fold': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    },
    'picturesSuited': { #Одномастные картинки
        'Fold': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'picturesOfsuited': { #Разномастные картинки
        'Fold': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'connectorSuited': { #Одномастные коннекторы
        'Fold': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'Call': {
            'EP': 'Call',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'foldHand': {
        'Fold': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Call' 
        },
        'Call': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Call'
        },
        'Raise': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    }
}