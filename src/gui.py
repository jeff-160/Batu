import tkinter as tk
from os import path
from PIL import Image, ImageTk
import string

from utils import *

class GUI:
    Sprites = []

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

    Events = {
        **{f"Key{i}": False for i in [c for c in string.ascii_uppercase]+["SPACE", "ENTER"]},
        "POINTER": False,
        "POINTERX": -1,
        "POINTERY": -1
    }

    @staticmethod
    def InitCheck(func):
        def wrapper(*args):
            from system import System
            if not System.GUI.Root:
                Utils.Error("GUI", "canvas not initialised")
            func(*args)
        return wrapper
    
    @staticmethod
    def ColorCheck(func):
        def wrapper(*args):
            if not args[0].lower() in GUI.Colors:
                Utils.Errors.NoGUI(args[0], "color")
            func(*args)
        return wrapper
    
    @staticmethod
    def UpdateKey(event, up):
        key = "Key"+[event.keysym, "enter"][event.keysym.lower()=="return"].upper()
        key not in GUI.Events or exec("GUI.Events[key] = up")

    @staticmethod
    def Init(title, width, height):
        from system import System
        if System.GUI.Root:
            Utils.Error("GUI", "canvas already intialised")

        Root = tk.Tk()
        Root.wm_title(title)
        Root.resizable(0,0)
        Root.protocol("WM_DELETE_WINDOW", GUI.Destroy)

        path = f"{System.Directory.Interpreter}\\resources\\batu.ico"
        Root.wm_iconbitmap(path)
        Root.iconbitmap(path)

        Root.bind("<KeyPress>", lambda e: GUI.UpdateKey(e, 1))
        Root.bind("<KeyRelease>", lambda e: GUI.UpdateKey(e, 0))
        Root.bind("<ButtonPress-1>", lambda _: exec("GUI.Events['POINTER']=True"))
        Root.bind("<ButtonRelease-1>", lambda _: exec("GUI.Events['POINTER']=False"))
        Root.bind("<Motion>", lambda e: exec("GUI.Events['POINTERX'], GUI.Events['POINTERY'] = e.x, e.y"))

        Canvas = tk.Canvas(Root, width=width, height=height, bg=GUI.Colors["black"], borderwidth=0, highlightthickness=0)
        Canvas.pack()

        System.GUI.Root, System.GUI.Canvas = Root, Canvas

    @staticmethod
    @InitCheck
    def Destroy():
        from system import System
        System.GUI.Root.destroy()
        System.GUI.Root = System.GUI.Canvas = None
        GUI.Sprites = []

    @staticmethod
    @InitCheck
    @ColorCheck
    def Rect(c, x, y, w, h):
        from system import System
        System.GUI.Canvas.create_rectangle(x, y, x+w, y+h, fill=GUI.Colors[c], outline="")

    @staticmethod
    @InitCheck
    @ColorCheck
    def Circle(c, x, y, r):
        from system import System
        System.GUI.Canvas.create_oval(x-r, y-r, x+r*2, y+r*2, fill=GUI.Colors[c], outline="")

    @staticmethod
    @InitCheck
    def Sprite(src, x, y, w, h):
        from system import System

        full = f"{System.Directory.Code}\\{src}"
        if not path.exists(full):
            Utils.Errors.NoGUI(src, "filepath")

        image = ImageTk.PhotoImage(Image.open(full).resize((w, h)))
        GUI.Sprites.append(image)
        System.GUI.Canvas.create_image(x, y, image=image, anchor=tk.NW)

    @staticmethod
    @InitCheck
    @ColorCheck
    def Text(c, t, x, y, s):
        from system import System
        System.GUI.Canvas.create_text(x, y, text=t, fill=c, font=(f'Helvetica {s} bold'), anchor=tk.NW)