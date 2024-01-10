import sys
sys.dont_write_bytecode = True

from system import *

def main():
    System.Run(open(sys.argv[1]).read().split("\n"))

if __name__=="__main__":
    main()