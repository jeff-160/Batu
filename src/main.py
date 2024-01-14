import sys
sys.dont_write_bytecode = True

from system import *

def main():
    System.Directory.Interpreter = path.dirname(path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__))
    System.Directory.Code = path.dirname(path.abspath(sys.argv[1]))

    System.Run(open(sys.argv[1]).read().split("\n"))

if __name__=="__main__":
    main()