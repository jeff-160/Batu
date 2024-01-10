from utils import *

class Parser:
    @staticmethod
    def Parse(expr):
        try:
            return eval(Parser.ReplaceVar(expr))
        except TypeError:
            Utils.Error("type", "incompatible types in expression")
        except:
            Utils.Error("syntax", f'invalid expression "{expr}"')

    @staticmethod
    def ReplaceVar(expr):
        from system import System
        for i in reversed(range(len(expr))):
            if expr[i]=="$":
                symbol = Utils.FindChar(expr[i:], f"[{Utils.Symbols}]")
                index = symbol+i if symbol!=None else len(expr)

                name = expr[i:index]
                if name not in System.Variables:
                    Utils.Errors.NoVar("variable", name)

                value = System.Variables[name.strip()].Value 
                value = f'"{value}"' if System.Variables[name.strip()].Type==System.Types["str"] else value
                
                expr = f"{expr[:i]}{value}{expr[index:]}"
        return expr