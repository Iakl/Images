from PIL import Image, ImageDraw, ImageFont
import series

class ImageNFT:
  def __init__(self, w, h, margin, bgcolor="blue", bdcolor="blue"):
      # Create a new image with RGB mode 
    self.margin = margin
    self.image = Image.new("RGB", (w, h), bdcolor)
    self.num_rows = 0
    self.num_cols = 0
    self.cell_w = 0
    self.cell_h = 0
    draw = ImageDraw.Draw(self.image)
    draw.rectangle((margin, margin, w - margin, h - margin), fill=bgcolor)

  def add_text(self, text, xp, yp, color='black'):
    draw = ImageDraw.Draw(self.image)
    font_path = "iakl.ttf"
    font_size = 16
    font = ImageFont.truetype(font_path, font_size)
    draw.text((xp, yp), text, fill=color, font=font)
  
  def draw_grid(self, lcolor="white"):
    draw = ImageDraw.Draw(self.image)
    width, height =self.image.size

    for c in range(self.num_cols + 1):
        draw.line([(self.margin + c * self.cell_w, self.margin), (self.margin + c * self.cell_w, height - self.margin)], fill=lcolor)

    for r in range(self.num_rows + 1):
        draw.line([(self.margin, self.margin + r * self.cell_h, ), (width - self.margin, self.margin + r * self.cell_h)], fill=lcolor)

  def paint_serie(self, serie, scolor):
    for num in serie:
      x = num % self.num_cols
      y = int(num / self.num_rows)
      self.paint_cell(x, y, scolor)

  def paint_cell(self, x, y, ccolor):
    draw = ImageDraw.Draw(self.image)
    draw.rectangle((margin + x*self.cell_w, margin + y*self.cell_h, margin + (x+1)*self.cell_w, margin + (y+1)*self.cell_h), fill=ccolor)

  def savejpg(self, name):
    self.image.save(f"{name}.jpg", "JPEG")

  def set_grid(self, num_rows, num_cols):
    width, height = self.image.size
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_w = (width -2*self.margin) / num_rows
    self.cell_h = (height -2*self.margin) / num_cols


sizeh = 1020
sizew = 1020
margin = 10
cells = 100

rs = "#fdcae1"
b = "#84b6f4"
y = "#fdfd96"


image = ImageNFT(sizew, sizeh, margin, b, rs)
image.set_grid(cells, cells)

prime_numbers = series.get_primes_lower_than_x(cells * cells)
image.paint_serie(prime_numbers, y)
image.add_text("hola", 2, 2, "#ffca99")

#image.draw_grid(rs)

image.savejpg('primes')

# Prime series:
# 
