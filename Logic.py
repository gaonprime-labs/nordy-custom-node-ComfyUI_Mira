import math
cat = "Mira/Logic"

class AlwaysEqualProxy(str):
#ComfyUI-Logic 
#refer: https://github.com/theUpsider/ComfyUI-Logic
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False

def CheckEvenOrOdd(num):       
    if num & 1:
        return (True, 'True',)
    else:
        return (False, 'False',)

def BooleanListInterpreter(bool_list, Start_At_Index, times = 1):
    new_list = []
    index = Start_At_Index
    list_len = len(bool_list)
    
    for _ in range(times):
        # not recommend, but this would be fun
        while index >= list_len:
            index = index - list_len
            
        new_bool = bool_list[index]
        new_list.append(new_bool)      
        index = index + 1
        
    return (new_list)              

class SingleBooleanTrigger:
    '''
    A Boolean Trigger
    
    Inputs:
    bool    - Boolean trigger
    
    Outputs:
    bool    - Boolean value same as input
    '''
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool": ("BOOLEAN", {
                    "default": False,
                }),                
            },
        }
                
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool",)
    FUNCTION = "SingleBooleanTriggerEx"
    CATEGORY = cat
    
    def SingleBooleanTriggerEx(self, bool):
        return (bool,)
    
class TwoBooleanTrigger:
    '''
    2 Boolean Triggers
    
    Inputs:
    bool        - Boolean trigger
    
    Outputs:
    bool_list   - Boolean list for `BooleanListInterpreter`
    '''
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_1": ("BOOLEAN", {"default": False,}),
                "bool_2": ("BOOLEAN", {"default": False,}),
            },
        }
                
    RETURN_TYPES = ("BOOLEAN_LIST",)
    RETURN_NAMES = ("bool_list",)
    FUNCTION = "TwoBooleanTriggerEx"
    CATEGORY = cat
    
    def TwoBooleanTriggerEx(self, bool_1, bool_2,):
        bool_list = [bool_1, bool_2]
        return (bool_list,)
    
class FourBooleanTrigger:
    '''
    4 Boolean Triggers
    
    Refer to TwoBooleanTrigger
    '''
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_1": ("BOOLEAN", {"default": False,}),
                "bool_2": ("BOOLEAN", {"default": False,}),
                "bool_3": ("BOOLEAN", {"default": False,}),
                "bool_4": ("BOOLEAN", {"default": False,}),
            },
        }
                
    RETURN_TYPES = ("BOOLEAN_LIST",)
    RETURN_NAMES = ("bool_list",)
    FUNCTION = "FourBooleanTriggerEx"
    CATEGORY = cat
    
    def FourBooleanTriggerEx(self, bool_1, bool_2, bool_3, bool_4):
        bool_list = [bool_1, bool_2, bool_3, bool_4]
        return (bool_list,)

class SixBooleanTrigger:
    '''
    6 Boolean Triggers
    
    OH... come on, It's all the same. Wanna know where I need those triggers? A LoRA train.
    Refer to TwoBooleanTrigger
    '''
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_1": ("BOOLEAN", {"default": False,}),
                "bool_2": ("BOOLEAN", {"default": False,}),
                "bool_3": ("BOOLEAN", {"default": False,}),
                "bool_4": ("BOOLEAN", {"default": False,}),
                "bool_5": ("BOOLEAN", {"default": False,}),
                "bool_6": ("BOOLEAN", {"default": False,}),
            },
        }
                
    RETURN_TYPES = ("BOOLEAN_LIST",)
    RETURN_NAMES = ("bool_list",)
    FUNCTION = "SixBooleanTriggerEx"
    CATEGORY = cat
    
    def SixBooleanTriggerEx(self, bool_1, bool_2, bool_3, bool_4, bool_5, bool_6):
        bool_list = [bool_1, bool_2, bool_3, bool_4, bool_5, bool_6]
        return (bool_list,)
    
class EightBooleanTrigger:
    '''
    8 Boolean Triggers
    
    Refer to TwoBooleanTrigger
    '''
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_1": ("BOOLEAN", {"default": False,}),
                "bool_2": ("BOOLEAN", {"default": False,}),
                "bool_3": ("BOOLEAN", {"default": False,}),
                "bool_4": ("BOOLEAN", {"default": False,}),
                "bool_5": ("BOOLEAN", {"default": False,}),
                "bool_6": ("BOOLEAN", {"default": False,}),
                "bool_7": ("BOOLEAN", {"default": False,}),
                "bool_8": ("BOOLEAN", {"default": False,}),
            },
        }
                
    RETURN_TYPES = ("BOOLEAN_LIST",)
    RETURN_NAMES = ("bool_list",)                
    FUNCTION = "EightBooleanTriggerEx"
    CATEGORY = cat
    
    def EightBooleanTriggerEx(self, bool_1, bool_2, bool_3, bool_4, bool_5, bool_6, bool_7, bool_8):
        bool_list = [bool_1, bool_2, bool_3, bool_4, bool_5, bool_6, bool_7, bool_8]
        return (bool_list,)    
    
class LogicNot:
    '''   
    Always return Boolean Not
    
    Input | Output
    True    False
    False   True    
    '''
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool": ("BOOLEAN", {"default": True,}),
            },
        }
                
    RETURN_TYPES = ("BOOLEAN","STRING")
    RETURN_NAMES = ("not_bool", "result")
    FUNCTION = "LogicNotEx"
    CATEGORY = cat
    
    def LogicNotEx(self, bool,):
        return (not bool, str(not bool),)
    
class EvenOrOdd:
    '''   
    Check if a `Integer` is odd or even.   
    
    Input | Output
    Odd     True    
    Even    False
    '''
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num": ("INT", {"default": 1,}),
            },
        }
                
    RETURN_TYPES = ("BOOLEAN", "STRING")
    RETURN_NAMES = ("bool_Odd_True", "result")
    FUNCTION = "EvenOrOddEx"
    CATEGORY = cat
    
    def EvenOrOddEx(self, num,):       
        return (CheckEvenOrOdd(num),)
    
class EvenOrOddList:
    '''   
    Checks whether each `digit` (decimal) of the input `integer` is odd or even, 
    and returns `true` for even numbers and `false` for odd numbers. 
    The final output is a `Boolean List` which is connected to the `Boolean List Interpreter`. 
    If the input `Number of digits` is less than the `Requirement`, 
    it will go back to the lowest digit to re-recognize and complete the list, 
    and the way the list is completed can be chosen as `as is` or `not`. 
    The output node `String` displays the actual results.

    Inputs:
    integer     - Recommend connect to `Seed Generator`
    quantity    - Length of the `Boolean list`, (I think) 16 for now is enough...
    NOT_filling - Filling Algorithm, `Enable` for switch `NOT` and "AS IS" in future loop, `Disable` for `AS IS` in every loop
    
    Outputs:
    bool_list   - Boolean list
    result      - String result
    
    Odd     True    
    Even    False
    '''
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "integer": ("INT", {
                    "default": 1234567890, 
                    "min": 0, 
                    "max": 0xffffffffffffffff,
                    "display": "input"
                }),
                "quantity": ("INT", {
                    "default": 1, 
                    "min": 1, 
                    "max": 16
                }),
                "NOT_filling": ("BOOLEAN", {
                    "default": False, 
                }),
            },            
        }
        
    RETURN_TYPES = ("BOOLEAN_LIST", "STRING")
    RETURN_NAMES = ("bool_list_Odd_True", "result")
    FUNCTION = "EvenOrOddListEx"
    CATEGORY = cat
    
    def EvenOrOddListEx(self, integer, quantity, NOT_filling):        
        bool_list = []
        string_list = 'Input = ' + str(integer) + ' Times = ' + str(len(str(integer))) + '\nResults\n'
        new_seed = integer       
        swap = False
        
        for _ in range(quantity):
            new_bool = CheckEvenOrOdd(new_seed)
            if False is swap:
                bool_list.append(new_bool[0])
                string_list = string_list + str(new_bool[0]) + '(' + str(new_seed) + ')\n'
            else:
                bool_list.append(not new_bool[0])
                string_list = string_list + str(not new_bool[0]) + '(' + str(new_seed) + ')\n'
                
            new_seed = math.floor(new_seed * 0.1)            
            if 0 >= new_seed:
                new_seed = integer
                if True is NOT_filling and swap is not True:
                    swap = True
                else:
                    swap = False   
                         
        return(bool_list, string_list, )
    
class BooleanListInterpreter1:  
    '''   
    Decode `Boolean` value(s) from `Boolean list`.
    
    Inputs:
    bool_list       - Boolean list
    Start_At_Index  - If `Start_At_Index` is greater than length of `Boolean list`, it will restart from `0`
    
    Outputs:
    bool(0~N)   - Boolean list    
    '''
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_list": ("BOOLEAN_LIST", {
                    "display": "input", 
                }),
                "Start_At_Index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "step": 1,
                    "display": "number" 
                }),                
            },            
        }
        
    RETURN_TYPES = ("BOOLEAN", )
    RETURN_NAMES = ("bool", )
    FUNCTION = "BooleanListInterpreter1Ex"
    CATEGORY = cat
    
    def BooleanListInterpreter1Ex(self, bool_list, Start_At_Index):
        new_list = BooleanListInterpreter(bool_list, Start_At_Index)
            
        return (new_list[0],)
    
class BooleanListInterpreter4:  
    '''   
    Same as BooleanListInterpreter1
    '''
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_list": ("BOOLEAN_LIST", {
                    "display": "input", 
                }),
                "Start_At_Index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "step": 1,
                    "display": "number" 
                }),                
            },            
        }
        
    RETURN_TYPES = ("BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN",)
    RETURN_NAMES = ("bool_0", "bool_1", "bool_2", "bool_3", )
    FUNCTION = "BooleanListInterpreter4Ex"
    CATEGORY = cat
    
    def BooleanListInterpreter4Ex(self, bool_list, Start_At_Index):
        new_list = BooleanListInterpreter(bool_list, Start_At_Index, 4)
            
        return (new_list[0],new_list[1],new_list[2],new_list[3],)
    
class BooleanListInterpreter8:  
    '''   
    Same as BooleanListInterpreter1
    '''
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bool_list": ("BOOLEAN_LIST", {
                    "display": "input", 
                }),
                "Start_At_Index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "step": 1,
                    "display": "number" 
                }),                
            },            
        }
        
    RETURN_TYPES = ("BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN","BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN",)
    RETURN_NAMES = ("bool_0", "bool_1", "bool_2", "bool_3", "bool_4", "bool_5", "bool_6", "bool_7",)
    FUNCTION = "BooleanListInterpreter8Ex"
    CATEGORY = cat
    
    def BooleanListInterpreter8Ex(self, bool_list, Start_At_Index):
        new_list = BooleanListInterpreter(bool_list, Start_At_Index, 8)
            
        return (new_list[0],new_list[1],new_list[2],new_list[3],new_list[4],new_list[5],new_list[6],new_list[7],)
    
class FunctionSwap:
    """
    Swap `func1` and `func2` outputs depends on `trigger`.
    
    Inputs:
    swap    - True or False
    func1   - Any function. E.g. `Mask_1`.
    func1   - Any function. E.g. `Mask_2`.
    
    Outputs:
    | swap  |   A   |   B   |
    | True  | func2 | func1 |
    | False | func1 | func2 |
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "trigger": ("BOOLEAN", {"default": False, "display":"input",}),
                "func1": (AlwaysEqualProxy("*"),),
                "func2": (AlwaysEqualProxy("*"),),
            },
        }

    RETURN_TYPES = (AlwaysEqualProxy("*"), AlwaysEqualProxy("*"),)
    RETURN_NAMES = ("A", "B", )
    FUNCTION = "FunctionSwapEx"
    CATEGORY = cat

    def FunctionSwapEx(self, trigger, func1, func2):
        if True is trigger:
            return (func2, func1,)
        else:
            return (func1, func2,)    
    
