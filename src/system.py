from syntax import Syntax, Variable
from math import pi, e
from os import path

from interpreter import *

class System:
    class Directory:
        Interpreter = Code = None

    LineNumber, CurrentLine, CurrentCode = 0, None, []
    IfEnd = None

    Variables = {}
    Labels = {}
    
    class GUI:
        Root = None
        Canvas = None

    BuiltIn = {
        "ambatugogetmesomesupper": Variable(pi, "float"),
        "itssofuckinghuge": Variable((1+5**0.5)/2, "float"),
        "ugheeeee": Variable(e, "float")
    }

    @staticmethod
    def Run(code):
        System.CurrentCode = code
        while System.LineNumber<len(System.CurrentCode):
            System.CurrentLine = System.CurrentCode[System.LineNumber]
            System.LineNumber+=1
            if System.IfEnd!=None and System.LineNumber==System.IfEnd:
                System.Labels = {k:System.Labels[k] for k in System.Labels if System.Labels[k].Global}
                System.IfEnd = None
            if not len(System.CurrentLine.strip()) or System.CurrentLine.strip()[0]==Syntax.Comment: 
                continue
            Interpreter.Interprete(System.CurrentLine)