'''
Created on 21 maj 2017

@author: Oskar
'''

from backgammon.model.GameField import GameField
from backgammon.model.GameField import Color

class BoardState(object):
    '''
    class which represents state of board at the moment.
    '''


    def __init__(self, fields_states = None):
        __fields_states = []
        if fields_states == None:
            self.__fields_states = BoardState.startingBoardState()
        else:
            self.__fields_states = fields_states
            
    
    @staticmethod
    def startingBoardState():
        'static method which returns list of 24 fields containing starting state'
        default_fields = []
        '''we append so we add elements starting from the end (first is 24th field
        default_field[i] means (i+1) field'''
                                                                                
        default_fields.append(GameField(False, 2, Color.RED))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 5, Color.BLACK))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 3, Color.BLACK))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 5, Color.RED))
        default_fields.append(GameField(False, 5, Color.BLACK))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 3, Color.RED))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 5, Color.RED))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 2, Color.BLACK))
        default_fields.reverse() 
        
        return default_fields
                              
        @property
        def fields_states(self):
            return self.__fields_states
        
        def update_field_at_index(self, index, game_field):
            fields_states.insert(index, game_field) 
                              
                              
                              
                              
                              
                                 