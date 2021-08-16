from CrossCanvas import CrossCanvas

class CrossBoard (CrossCanvas):
  def __init__ (self, master):
    super().__init__(master)
    self.bind('<Button-1>', lambda event: self.handle_cross_click(self.convert_canvas_pos_to_cross_pos((event.x, event.y))))
