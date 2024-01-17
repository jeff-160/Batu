from parser import *

class Lexer:
    @staticmethod
    def Lex(line):
        index, comment = Utils.FindChar(line, " "), Utils.FindChar(line, "#")
        function = line[:index]
        return (function, Lexer.GetArgs(line[index+1:comment] if comment!=None else line[index+1:], []) if function!=line.strip() else [])
            
    @staticmethod
    def GetArgs(line, args):
        index = Utils.FindChar(line, ",")
        args.append((line if index==None else line[:index]).strip())
        
        if not len(args[-1]):
            Utils.Error("syntax", "expected argument")
        if index==None:
            return args
        return Lexer.GetArgs(line[index+1:], args)