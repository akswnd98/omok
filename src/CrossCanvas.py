import tkinter as tk

class CrossCanvas (tk.Canvas):
  CROSS_DIV = [7, 7]
  ONE_SPACE_SIZE = 30

  def __init__ (self, master):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_crosses()

  def create_crosses (self):
    for y in range(self.CROSS_DIV[0]):
      for x in range(self.CROSS_DIV[1]):
        self.create_cross(x, y)

  def create_cross (self, x, y):
    self.create_line(
      x * self.ONE_SPACE_SIZE, self.ONE_SPACE_SIZE / 2 + y * self.ONE_SPACE_SIZE,
      (x + 1) * self.ONE_SPACE_SIZE, self.ONE_SPACE_SIZE / 2 + y * self.ONE_SPACE_SIZE
    )
    self.create_line(
      self.ONE_SPACE_SIZE / 2 + x * self.ONE_SPACE_SIZE, y * self.ONE_SPACE_SIZE,
      self.ONE_SPACE_SIZE / 2 + x * self.ONE_SPACE_SIZE, (y + 1) * self.ONE_SPACE_SIZE
    )

  def handle_cross_click (self, xy):
    pass

  def convert_cross_pos_to_canvas_start_pos (self, xy):
    return (
      xy[0] * self.ONE_SPACE_SIZE,
      xy[1] * self.ONE_SPACE_SIZE
    )
  
  def convert_cross_pos_to_canvas_end_pos (self, xy):
    return (
      (xy[0] + 1) * self.ONE_SPACE_SIZE,
      (xy[1] + 1) * self.ONE_SPACE_SIZE
    )
  
  def convert_canvas_pos_to_cross_pos (self, xy):
    return (
      xy[0] // self.ONE_SPACE_SIZE,
      xy[1] // self.ONE_SPACE_SIZE
    )