from CrossBoard import CrossBoard

class OmokBoard (CrossBoard):
  def __init__ (self, master):
    super().__init__(master)
  
  def draw_white_stone (self, xy):
    self.create_oval(
      xy[0] * self.ONE_SPACE_SIZE, xy[1] * self.ONE_SPACE_SIZE,
      (xy[0] + 1) * self.ONE_SPACE_SIZE, (xy[1] + 1) * self.ONE_SPACE_SIZE,
      fill='white'
    )
  
  def draw_black_stone (self, xy):
    self.create_oval(
      xy[0] * self.ONE_SPACE_SIZE, xy[1] * self.ONE_SPACE_SIZE,
      (xy[0] + 1) * self.ONE_SPACE_SIZE, (xy[1] + 1) * self.ONE_SPACE_SIZE,
      fill='black'
    )