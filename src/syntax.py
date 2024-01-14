from time import sleep
from sys import stdout
from random import randint, uniform
from math import cos, sin, tan

from gui import *
from utils import *

class Keyword:
    def __init__(self, function, args=[]):
        self.Function, self.ArgTypes = function, args

    @staticmethod
    def StoreFunc(func):
        def wrapper(*args):
            from system import System
            if args[0] not in System.Variables:
                Utils.Errors.NoVar("variable", args[0])

            exec(f"_{System.Variables[args[0]].Type}('{args[0]}', '{func(*args)}')")
        return wrapper

class Variable:
    def __init__(self, value, datatype):
        self.Value, self.Type = value, datatype

    @staticmethod
    def Declare(name, datatype):
        exec(f"""global _{name};\ndef _{name}(name, value): 
            Utils.CheckName(name, "variable")
            from system import System
            try:
                System.Variables[name] = Variable({datatype}(value), "{name}")
            except:
                Utils.Errors.NoConvert(value, "{name}")
            """)
        return eval(f"_{name}")

class Label:
    def __init__(self, line, isglobal=True):
        self.LineNumber = line
        self.Global = isglobal
    

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
        Utils.Error("value", "condtional block span must be a positive integer")

    from system import System
    if System.LineNumber+span>len(System.CurrentCode):
        Utils.Error("syntax", "condtional block extends past end of file")
    if not condition:
        System.LineNumber+=span
    System.IfEnd = System.LineNumber+span+1

@Keyword.StoreFunc
def _randint(var, min, max):
    try:
        return randint(min, max)
    except ValueError:
        Utils.Error("value", f'invalid range "{min}-{max}"')
        

class Syntax:
    NameType = []
    ValueType = []

    Comment = "#"
    Variable = "$"
    BuiltIn = "%"
    GUI = "&"
    Symbol = None

    Types = {
        "bool": "ambasing",
        "int": "ambatukam",
        "float": "ambatublou",
        "str": "ambatuexplode",
    }
    Keywords = {}

Syntax.Symbols = ''.join([i for i in string.punctuation if i not in [Syntax.Comment, Syntax.Variable, Syntax.BuiltIn, Syntax.GUI]])

Syntax.Keywords = {
    "yuwandisnut": Keyword(lambda text: print(text, end='') or stdout.flush(), [str]),
    "iwanit": Keyword(Keyword.StoreFunc(lambda var, text: input(text)), [Syntax.NameType, str]),

    **{
        i[0]: Keyword(Variable.Declare(i[0], i[1]), [Syntax.NameType, Syntax.ValueType])
            for i in [(Syntax.Types[k], k) for k in Syntax.Types]
    },

    "ambatubus": Keyword(_label, [Syntax.NameType]),
    "yomemibus": Keyword(_goto, [Syntax.NameType]),

    "kazdasdanutanee": Keyword(_if, [bool, int]),

    "aauuhh": Keyword(lambda i: sleep(i/1000), [int]),
    "ewww": Keyword(sys.exit),

    "ambatunat": Keyword(Keyword.StoreFunc(lambda var: uniform(0,1)), [Syntax.NameType]),
    "ambatufakinat": Keyword(_randint, [Syntax.NameType, int, int]),
    "yesthankyousomuch": Keyword(Keyword.StoreFunc(lambda var, val: sin(val)), [Syntax.NameType, float]),
    "thankyou": Keyword(Keyword.StoreFunc(lambda var, val: cos(val)), [Syntax.NameType, float]),
    "thatmaybejustwhatineedtobus": Keyword(Keyword.StoreFunc(lambda var, val: tan(val)), [Syntax.NameType, float]),

    "omaygot": Keyword(GUI.Init, [str, int, int]),
    "dontkam": Keyword(GUI.InitCheck(lambda: exec("from system import System; System.GUI.Root.update()"))),
    "washthatass": Keyword(GUI.InitCheck(lambda: exec('from system import System; System.GUI.Canvas.delete("all")'))),
    "stretchdisass": Keyword(GUI.InitCheck(lambda width, height: exec(f"from system import System; System.GUI.Root.geometry('{width}x{height}')")), [int, int]),
    "yuboutodestroydisass": Keyword(GUI.Destroy),
    "haurder": Keyword(GUI.Rect, [str, float, float, float, float]),
    "bus": Keyword(GUI.Circle, [str, float, float, float]),
    "steven": Keyword(GUI.Sprite, [str, float, float, int, int]),
    "vukvukvukvukvukvuk": Keyword(GUI.Text, [str, str, int, int, int])
}