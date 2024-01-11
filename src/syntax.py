from time import sleep
from sys import stdout

from utils import *

class Keyword:
    def __init__(self, function, args):
        self.Function, self.ArgTypes = function, args

class Variable:
    def __init__(self, value, datatype):
        self.Value, self.Type = value, datatype

    @staticmethod
    def Declare(name, datatype):
        exec(f"""global _{name};\ndef _{name}(name, value): 
            Utils.CheckName(name, "variable")
            from system import System
            try:
                System.Variables[f"${{name}}"] = Variable({datatype}(value), "{name}")
            except:
                Utils.Errors.NoConvert(value, "{name}")
            """)
        return eval(f"_{name}")

class Label:
    def __init__(self, line, isglobal=True):
        self.LineNumber = line
        self.Global = isglobal


def _output(text):
    print(text, end='')
    stdout.flush()

def _input(var, text):
    name = f"${var}"

    from system import System
    if name not in System.Variables:
        Utils.Errors.NoVar("variable", name)
    
    value = input(text)
    exec(f"_{System.Variables[name].Type}('{var}', '{value}')")

def _label(name):
    Utils.CheckName(name, "label")

    from system import System
    if name in System.Labels:
        Utils.Error("name", f'label "{name}" already exists')
    System.Labels[name] = Label(System.LineNumber, System.IfEnd==None)

def _goto(name):
    from system import System
    if not name in System.Labels:
        Utils.Errors.NoVar("label", name)
    System.LineNumber = System.Labels[name].LineNumber

def _if(condition, span):
    if span<=0:
        Utils.Error("syntax", "if block span must be a positive integer")

    from system import System
    if System.LineNumber+span>len(System.CurrentCode):
        Utils.Error("syntax", "if block extends past end of file")
    if not condition:
        System.LineNumber+=span
    System.IfEnd = System.LineNumber+span+1


class Syntax:
    NameType = []
    ValueType = []

    Comment = "#"
    Variable = "$"
    BuiltIn = "%"
    Symbol = None

    Types = {
        "int": "ambatukam",
        "float": "ambatunut",
        "str": "ambadeblou",
        "bool": "ambasing"
    }
    Keywords = {}

Syntax.Symbols = ''.join([i for i in string.punctuation if i not in [Syntax.Comment, Syntax.Variable, Syntax.BuiltIn]])

Syntax.Keywords = {
    "yuwandisnut": Keyword(_output, [str]),
    "iwanit": Keyword(_input, [Syntax.NameType, str]),

    **{
        i[0]: Keyword(Variable.Declare(i[0], i[1]), [Syntax.NameType, Syntax.ValueType])
            for i in [(Syntax.Types[k], k) for k in Syntax.Types]
    },

    "bus": Keyword(_label, [Syntax.NameType]),
    "yomemibus": Keyword(_goto, [Syntax.NameType]),

    "kazdasdanutanee": Keyword(_if, [bool, int]),

    "aauuhh": Keyword(lambda i: sleep(i/1000), [int]),
    "yuboutodestroydisass": Keyword(exit, [])
}