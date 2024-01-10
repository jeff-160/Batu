import re, string

class Utils:
    Symbols = ''.join([i for i in string.punctuation if i not in "$_"])

    @staticmethod
    def CheckName(name):
        if not name[0].isalpha():
            Utils.Error("syntax", "variable name must start with alpha")
        if " " in name:
            Utils.Error("syntax", "variable name cannot contain whitespace")
        if len([*filter(lambda x: (not x.isalnum()) and x!="_", name)]):
            Utils.Error("syntax", "invalid symbol in variable name")

    @staticmethod
    def FindChar(line, char):
        inString = False
        for i in range(len(line)):
            if line[i] in "\"'": 
                inString = not inString
            if re.findall(char, line[i]) and not inString:
                return i
    
    @staticmethod
    def Error(errtype, msg):
        from system import System
        if System.LineNumber==float("inf"):
            exit()

        fn = lambda t: t[0].upper()+t[1:]

        print(f"\n{fn(errtype)}Error: {fn(msg)}\n\tat line {System.LineNumber}: {System.CurrentLine}")
        System.LineNumber = float("inf")
        exit()
            
    class Errors:
        NoVar = lambda vartype, name: Utils.Error("reference", f'{vartype} "{name}" is not defined')
