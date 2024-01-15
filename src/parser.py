from utils import *

class Parser:
    @staticmethod
    def Parse(expr):
        try:
            return eval(Parser.ReplaceVar(expr))
        except TypeError:
            Utils.Error("type", "incompatible types in expression")
        except Exception:
            Utils.Error("syntax", f'invalid expression "{expr}"')

    @staticmethod
    def ReplaceVar(expr):
        from syntax import Syntax
        inString = False

        i = len(expr)-1
        while i>=0:
            if expr[i] in Syntax.Quotes:
                inString = not inString

            if expr[i] in [Syntax.Variable, Syntax.BuiltIn, Syntax.GUI] and not inString:
                symbol = Utils.FindChar(expr[i:], f"[{Syntax.Symbols}, ' ']")
                index = symbol+i if symbol!=None else len(expr)

                name = expr[i+1:index].strip()

                if expr[i]==Syntax.GUI:
                    from gui import GUI
                    if name not in GUI.Events:
                        Utils.Errors.NoGUI(name, "key")
                    value = GUI.Events[name]
                else:        
                    from system import System
                    col = [System.BuiltIn, System.Variables][expr[i]==Syntax.Variable]
                    if name not in col:
                        Utils.Errors.NoVar(["built-in constant", "variable"][expr[i]==Syntax.Variable], name)
                    value = col[name].Value
                    value = f'"""{value}"""' if col[name].Type==Syntax.Types["str"] else value
                
                expr = f"{expr[:i]}{value}{expr[index:]}"
            i-=1
        return expr