import math

cat = "Mira/Util"

def SafeCheck(Width = 16, Height = 16, Batch = 1, HiResMultiplier = 1.0):
        if 16 > Width:
            Width = 16
            
        if 16 > Height:
            Height = 16
            
        if 1 > Batch:
            Batch = 1
            
        if 1.0 > HiResMultiplier:
            HiResMultiplier = 1.0
        
        return Width, Height, Batch, HiResMultiplier

class CanvasCreatorSimple:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Width": ("INT", {
                    "default": 576,
                    "min": 16,
                    "step": 8,
                    "display": "number" 
                }),
                "Height": ("INT", {
                    "default": 1024,
                    "min": 16,
                    "step": 8,
                    "display": "number" 
                }),
                "Landscape": ("BOOLEAN", {
                    "default": False
                }),
            },
        }
                
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("Width","Height",)
    FUNCTION = "CanvasCreatorSimpleEx"
    CATEGORY = cat
    
    def CanvasCreatorSimpleEx(self, Width, Height, Landscape):                         
        Width, Height, = SafeCheck(Width, Height)
        
        if(False == Landscape):
            return(Width, Height,)
        else:
            return(Height, Width,)

        
class CanvasCreatorAdvanced:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Width": ("INT", {
                    "default": 576,
                    "min": 16,
                    "step": 8,
                    "display": "number" 
                }),
                "Height": ("INT", {
                    "default": 1024,
                    "min": 16,
                    "step": 8,
                    "display": "number" 
                }),
                "Batch": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 16,
                    "step": 1,
                    "display": "number" 
                }),
                "Landscape": ("BOOLEAN", {
                    "default": False
                }),
                "HiResMultiplier": ("FLOAT", {
                    "default": 1.5,
                    "min": 1,
                    "step": 0.1,
                    "display": "number" 
                }),
            },
        }

    RETURN_TYPES = ("INT","INT","INT","INT","INT","STRING",)
    RETURN_NAMES = ("Width","Height","Batch","HiRes Width","HiRes Height","Debug",)
    FUNCTION = "CanvasCreatorEx"
    CATEGORY = cat
    
    def CanvasCreatorEx(self, Width, Height, Batch, Landscape, HiResMultiplier):       
        DebugMessage = 'Mira:'       
        
        Width, Height, Batch, HiResMultiplier = SafeCheck(Width, Height, Batch, HiResMultiplier)
            
        HiResWidth = Width * HiResMultiplier
        HiResHeight = Height * HiResMultiplier        
        
        if 0 != math.floor(HiResWidth)%8:
            DebugMessage += '\n(Before)HiResWidth = ' + str(math.floor(HiResWidth))
            residue = math.floor(HiResWidth)%8
            if 3 >= math.floor(HiResWidth)%8:
                HiResWidth = math.floor(HiResWidth) - residue
            else:
                HiResWidth = math.floor(HiResWidth) + 8 - residue
            DebugMessage += '\n(After)HiResWidth = ' + str(math.floor(HiResWidth))            
            
        if 0 != math.floor(HiResHeight)%8:
            DebugMessage += '\n(Before)HiResHeight = ' + str(math.floor(HiResHeight))
            residue = math.floor(HiResHeight)%8
            if 3 >= math.floor(HiResHeight)%8:
                HiResHeight = math.floor(HiResHeight) - residue
            else:
                HiResHeight = math.floor(HiResHeight) + 8 - residue
            DebugMessage += '\n(After)HiResHeight = ' + str(math.floor(HiResHeight))
        
        if(False == Landscape):
            DebugMessage += '\nWidth = ' + str(Width)
            DebugMessage += '\nHeight = ' + str(Height)
            DebugMessage += '\nHiResWidth = ' + str(math.floor(HiResWidth))
            DebugMessage += '\nHiResHeight = ' + str(math.floor(HiResHeight))
            
            intHiResHeight = math.floor(HiResHeight)
            intHiResWidth = math.floor(HiResWidth)
            return(Width, Height, Batch, intHiResWidth, intHiResHeight, DebugMessage,)
        else:
            DebugMessage += '\nLandscape actived, swap Height and Width'
            DebugMessage += '\nWidth = ' + str(Height)
            DebugMessage += '\nHeight = ' + str(Width)
            DebugMessage += '\nHiResWidth = ' + str(math.floor(HiResWidth))
            DebugMessage += '\nHiResHeight = ' + str(math.floor(HiResHeight))
            
            intHiResHeight = math.floor(HiResHeight)
            intHiResWidth = math.floor(HiResWidth)
            return(Height, Width, Batch, intHiResHeight, intHiResWidth, DebugMessage,)
        
        