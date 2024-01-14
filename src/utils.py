import re, sys

class Utils:
    @staticmethod
    def CheckName(name, vartype):
        if not name[0].isalpha():
            Utils.Error("syntax", f"{vartype} name must start with alphabetic character")
        if " " in name:
            Utils.Error("syntax", f"{vartype} name cannot contain whitespace")
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
            sys.exit()

        fn = lambda t: t[0].upper()+t[1:]

        print(f"\n{fn(errtype)}Error: {fn(msg)}\n\tat line {System.LineNumber}: {System.CurrentLine.strip()}")
        System.LineNumber = float("inf")
        sys.exit()
            
    class Errors:
        NoVar = lambda vartype, name: Utils.Error("reference", f'{vartype} "{name}" is not defined')
        NoConvert = lambda value, type: Utils.Error("type", f'unable to convert "{value}" to type "{type}"')
        NoGUI = lambda name, type: Utils.Error("GUI", f'invalid {type} "{name}"')