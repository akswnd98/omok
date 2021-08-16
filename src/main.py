import tkinter as tk
from OmokBoard import OmokBoard

class Application (tk.Frame):
  def __init__ (self, master=None):
    super().__init__(master)
    self.master = master
    self.create_widgets()
    self.pack()
  
  def create_widgets (self):
    self.omok_board = OmokBoard(self)
    self.omok_board.handle_cross_click = self.handle_click
    self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
    self.quit.pack(side='bottom')

  def handle_click (self, xy):
    print(xy)
    self.omok_board.draw_white_stone(xy)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
