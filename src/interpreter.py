from lexer import *

class Interpreter:
    @staticmethod
    def Interprete(line):
        function, args = Lexer.Lex(line.strip())
        from syntax import Syntax

        if function not in Syntax.Keywords:
            Utils.Error("name", f'"{function}" is not defined') 
        
        rArgs, eArgs = args, Syntax.Keywords[function].ArgTypes
        if len(rArgs)!=len(eArgs):
            Utils.Error("argument", f"Expected {len(eArgs)} arguments, received {len(rArgs)}")

        fArgs = []
        for i in range(len(eArgs)):
            if eArgs[i] is Syntax.NameType:
                fArgs.append(rArgs[i])
            else:
                cast = [eArgs[i], lambda x:x][eArgs[i] is Syntax.ValueType]
                try:
                    fArgs.append(cast(Parser.Parse(rArgs[i])))
                except:
                    Utils.Errors.NoConvert(rArgs[i], Syntax.Types[cast.__name__] if cast.__name__ in Syntax.Types else "")

        Syntax.Keywords[function].Function(*fArgs)