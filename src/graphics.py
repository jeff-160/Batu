import tkinter as tk
from utils import *

class Graphics:
    Colors = {
        **{
            k: f"#{v[0]:02X}{v[1]:02X}{v[2]:02X}"
            for k,v in{
                "red": (255,0,0),
                "orange": (252,102,14),
                "yellow": (255,255,0),
                "green": (0,255,0),
                "blue": (0,0,255),
                "purple": (128,0,128),
                "pink": (255,192,203),
                "black": (0,0,0),
                "white": (255,255,255),
            }.items()
        }
    }
    
    @staticmethod
    def InitCheck(func):
        def wrapper(*args):
            from system import System
            if not System.Graphics.Root:
                Utils.Error("graphics", "canvas not initialised")
            func(*args)
        return wrapper
    
    @staticmethod
    def ColorCheck(func):
        def wrapper(*args):
            if not args[0].lower() in Graphics.Colors:
                Utils.Error("graphics", f'color "{args[0]}" not recognised')
            func(*args)
        return wrapper

    @staticmethod
    def Init(title, width, height):
        from system import System
        if System.Graphics.Root:
            Utils.Error("graphics", "canvas already intialised")

        Root = tk.Tk()
        Root.wm_title(title)
        Root.resizable(0,0)
        Root.protocol("WM_DELETE_WINDOW", Graphics.Destroy)

        Canvas = tk.Canvas(Root, width=width, height=height, bg=Graphics.Colors["black"], borderwidth=0, highlightthickness=0)
        Canvas.pack()

        System.Graphics.Root, System.Graphics.Canvas = Root, Canvas

    @staticmethod
    @InitCheck
    def Destroy():
        from system import System
        System.Graphics.Root.destroy()
        System.Graphics.Root = System.Graphics.Canvas = None

    @staticmethod
    @InitCheck
    @ColorCheck
    def Rect(c, x, y, w, h):
        from system import System
        System.Graphics.Canvas.create_rectangle(x, y, x+w, y+h, fill=Graphics.Colors[c], outline="")

    @staticmethod
    @InitCheck
    @ColorCheck
    def Circle(c, x, y, r):
        from system import System
        System.Graphics.Canvas.create_oval(x, y, x+r*2, y+r*2, fill=Graphics.Colors[c], outline="")

    @staticmethod
    @InitCheck
    def Sprite():
        pass