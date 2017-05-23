'''
Created on 21 maj 2017

@author: Oskar/Kazan
'''

from model.GameField import GameField
from model.GameField import Color

class BoardState:
    '''
    class which represents state of board at the moment.
    '''


    def __init__(self, fields = None):
        self.__fields_states = None
        self.__fields_states = []
        if fields == None:
            self.__fields_states = BoardState.startingBoardState()
        else:
            self.__fields_states = fields
            
    
    @staticmethod
    def startingBoardState():
        'static method which returns list of 24 fields containing starting state'
        default_fields = []
        
                                                                                
        default_fields.append(GameField(False, 2, Color.RED))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 1, Color.BLACK)) #5
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 1, Color.BLACK)) #3
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(is_empty=True))
        default_fields.append(GameField(False, 5, Color.RED))
        default_fields.append(GameField(False, 1, Color.BLACK)) #5
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
        default_fields.append(GameField(False, 1, Color.BLACK)) #2
        default_fields.reverse() 

        #default_fields.append(GameField(False, 1, Color.BLACK)) #2
        
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(False, 1, Color.BLACK)) #5
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(False, 1, Color.BLACK)) #3
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        
        #default_fields.append(GameField(False, 1, Color.BLACK)) #5
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        
        #default_fields.append(GameField(is_empty=True))
        
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(is_empty=True))
        #default_fields.append(GameField(False, 2, Color.RED))
        #default_fields.append(GameField(False, 3, Color.RED))
        #default_fields.append(GameField(False, 5, Color.RED))
        #default_fields.append(GameField(False, 5, Color.RED))
        
        #default_fields.reverse() 
        
        return default_fields
                              
        
        
        def update_field_at_index(self, index, game_field):
            fields_states.insert(index, game_field) 

        @property
        def fields_states(self):
            return self.__fields_states
                              
                              
                              
                              
                              
                                 