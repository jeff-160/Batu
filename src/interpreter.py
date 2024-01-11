from lexer import *

class Interpreter:
    @staticmethod
    def Interprete(line):
        function, args = Lexer.Lex(line.strip())
        from system import System
        from syntax import Syntax

        if function not in Syntax.Keywords:
            Utils.Error("name", f'"{function}" is not defined') 
        
        rArgs, eArgs = args, Syntax.Keywords[function].ArgTypes
        if len(rArgs)!=len(eArgs):
            Utils.Error("argument", f"Expected {len(eArgs)} arguments, received {len(rArgs)}")

        Syntax.Keywords[function].Function(
            *[rArgs[i]
               if eArgs[i] is Syntax.NameType else 
               [eArgs[i], lambda x:x][eArgs[i] is Syntax.ValueType](Parser.Parse(rArgs[i]))
               for i in range(len(eArgs))]
        )