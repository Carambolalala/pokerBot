#КОМБА -> ДЕЙСТВИЯ ОППОНЕНТОВ -> ПОЗИЦИЯ
#EP - ранняя позиция, МР - средняя позиция, LP - поздняя позиция
comboStartHand = {
    'highDouble': { #Старшие пары
        'F': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        },
        'R': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        }
    },
    'middleDouble': { #Средние пары
        'F': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        },
        'R': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'juniorDouble': { #Младшие пары
        'F': {
            'EP': 'Fold',
            'MP': 'Call',
            'LP': 'Raise',
            'Blind': 'Call' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'R': {
            'EP': 'Call20',
            'MP': 'Call20',
            'LP': 'Call20',
            'Blind': 'Call20'
        }
    },
    'highAces': { #Сильные тузы
        'F': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        },
        'R': {
            'EP': 'Raise',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise'
        }
    },
    'middleAces': { #Средние тузы
        'F': {
            'EP': 'Fold',
            'MP': 'Raise',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Raise',
            'Blind': 'Call'
        },
        'R': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    },
    'juniorAcesSuited': { #Малые одномастные тузы
        'F': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'R': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    },
    'picturesSuited': { #Одномастные картинки
        'F': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'R': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    },
    'picturesOfsuited': { #Разномастные картинки
        'F': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Call'
        },
        'R': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    },
    'connectorSuited': { #Одномастные коннекторы
        'F': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Raise',
            'Blind': 'Raise' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Call',
            'LP': 'Call',
            'Blind': 'Call'
        },
        'R': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    },
    'foldHand': { #Одномастные коннекторы
        'F': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold' 
        },
        'C': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        },
        'R': {
            'EP': 'Fold',
            'MP': 'Fold',
            'LP': 'Fold',
            'Blind': 'Fold'
        }
    }
}