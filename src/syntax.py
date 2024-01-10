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
            Utils.CheckName(name)
            from system import System
            try:
                System.Variables[f"${{name}}"] = Variable({datatype}(value), "{name}")
            except:
                Utils.Error("type", f'unable to convert "{{value}}" to type "{name}"')
            """)
        return eval(f"_{name}")


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
    Utils.CheckName(name)

    from system import System
    if name in System.Labels:
        Utils.Error("name", f'label "{name}" already exists')
    System.Labels[name] = System.LineNumber

def _goto(name):
    from system import System
    if not name in System.Labels:
        Utils.Errors.NoVar("label", name)
    System.LineNumber = System.Labels[name]


class Syntax:
    NameType = []
    ValueType = []

    Comment = "#"
    Types = {
        "int": "ambatukam",
        "float": "ambatunut",
        "str": "ambadeblou",
        "bool": "ambasing"
    }
    Keywords = {}

Syntax.Keywords = {
    "yuwandisnut": Keyword(_output, [str]),
    "iwanit": Keyword(_input, [Syntax.NameType, str]),

    **{
        i[0]: Keyword(Variable.Declare(i[0], i[1]), [Syntax.NameType, Syntax.ValueType])
            for i in [(Syntax.Types[k], k) for k in Syntax.Types]
    },

    "bus": Keyword(_label, [Syntax.NameType]),
    "yomemibus": Keyword(_goto, [Syntax.NameType]),

    "aauuhh": Keyword(lambda i: sleep(i/1000), [int]),
    "yuboutodestroydisass": Keyword(exit, [])
}