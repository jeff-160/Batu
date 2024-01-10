from lexer import *

class Interpreter:
    @staticmethod
    def Interprete(line):
        function, args = Lexer.Lex(line.strip())
        from system import System
        from keywords import Keyword

        if function not in System.Keywords:
            Utils.Error("name", f'"{function}" is not defined') 
        
        rArgs, eArgs = args, System.Keywords[function].ArgTypes
        if len(rArgs)!=len(eArgs):
            Utils.Error("argument", f"Expected {len(eArgs)} arguments, received {len(rArgs)}")

        System.Keywords[function].Function(
            *[rArgs[i]
               if eArgs[i] is Keyword.NameType else 
               [eArgs[i], lambda x:x][eArgs[i] is Keyword.ValueType](Parser.Parse(rArgs[i]))
               for i in range(len(eArgs))]
        )