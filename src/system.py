from interpreter import *
from keywords import _Keywords, _Types

class System:
    LineNumber, CurrentLine = 0, None
    Keywords, Types = _Keywords, _Types
    Variables = {}
    Labels = {}

    @staticmethod
    def Run(code):
        while System.LineNumber<len(code):
            System.CurrentLine = code[System.LineNumber]
            System.LineNumber+=1
            if not len(System.CurrentLine.strip()): 
                continue
            Interpreter.Interprete(System.CurrentLine)