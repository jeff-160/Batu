import tkinter as tk
from utils import *

class Graphics:
    @staticmethod
    def GetHex(r, g, b):
        return f"#{r:02X}{g:02X}{b:02X}"
    
    @staticmethod
    def Check(func):
        def wrapper(*args, **kwargs):
            from system import System
            if not System.Graphics.Root:
                Utils.Error("graphics", "canvas not initialised")
            func(*args, **kwargs)
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

        Canvas = tk.Canvas(Root, width=width, height=height, bg=Graphics.GetHex(0,0,0), borderwidth=0, highlightthickness=0)
        Canvas.pack()

        System.Graphics.Root, System.Graphics.Canvas = Root, Canvas

    @staticmethod
    @Check
    def Destroy():
        from system import System
        System.Graphics.Root.destroy()
        System.Graphics.Root = System.Graphics.Canvas = None

    @staticmethod
    @Check
    def Rect(x, y, w, h):
        from system import System
        System.Graphics.Canvas.create_rectangle(x, y, x+w, y+h, fill=Graphics.GetHex(255,0,0),outline="")

    @staticmethod
    @Check
    def Circle(x, y, r):
        pass

    @staticmethod
    @Check
    def Sprite():
        pass