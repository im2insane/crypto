try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import cryptoGUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    cryptoGUI_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    cryptoGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+437+149")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")



        self.textBox_search = Text(top)
        self.textBox_search.place(relx=0.02, rely=0.02, relheight=0.05
                , relwidth=0.37)
        self.textBox_search.configure(background="white")
        self.textBox_search.configure(font="TkTextFont")
        self.textBox_search.configure(foreground="black")
        self.textBox_search.configure(highlightbackground="#d9d9d9")
        self.textBox_search.configure(highlightcolor="black")
        self.textBox_search.configure(insertbackground="black")
        self.textBox_search.configure(selectbackground="#c4c4c4")
        self.textBox_search.configure(selectforeground="black")
        self.textBox_search.configure(width=224)
        self.textBox_search.configure(wrap=WORD)

        self.button_Confirm = ttk.Button(top)
        self.button_Confirm.place(relx=0.42, rely=0.02, height=25, width=316)
        self.button_Confirm.configure(takefocus="")
        self.button_Confirm.configure(text='''Look Up''')
        self.button_Confirm.configure(width=316)






if __name__ == '__main__':
    vp_start_gui()