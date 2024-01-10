from interpreter import *
from syntax import Syntax

class System:
    LineNumber, CurrentLine = 0, None
    Keywords, Types, Comment = Syntax.Keywords, Syntax.Types, Syntax.Comment
    Variables = {}
    Labels = {}

    @staticmethod
    def Run(code):
        while System.LineNumber<len(code):
            System.CurrentLine = code[System.LineNumber]
            System.LineNumber+=1
            if not len(System.CurrentLine.strip()) or System.CurrentLine.strip()[0]==System.Comment: 
                continue
            Interpreter.Interprete(System.CurrentLine)