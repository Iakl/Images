from PIL import Image, ImageDraw
import series

class ImageNFT:
  def __init__(self, w, h, margin, bgcolor="blue"):
      # Create a new image with RGB mode 
    self.margin = margin
    self.image = Image.new("RGB", (w, h), "#fdfd96")
    self.num_rows = 0
    self.num_cols = 0
    self.cell_w = 0
    self.cell_h = 0
    draw = ImageDraw.Draw(self.image)
    draw.rectangle((margin, margin, w - margin, h - margin), fill=bgcolor)
  
  
  def draw_grid(self, lcolor="white"):
    draw = ImageDraw.Draw(self.image)
    width, height =self.image.size

    for x in range(self.margin, width - self.margin + 1, self.cell_w):
        draw.line([(x, self.margin), (x, height - self.margin)], fill=lcolor)

    for y in range(self.margin, height - self.margin + 1, self.cell_h):
        draw.line([(self.margin, y), (width - self.margin, y)], fill=lcolor)

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
    self.cell_w = int((width -2*self.margin) / num_rows)
    self.cell_h = int((height -2*self.margin) / num_cols)


sizeh = 300
sizew = 300
margin = 10
cells = 10

image = ImageNFT(sizew, sizeh, margin, "#fdcae1")
image.set_grid(cells, cells)

prime_numbers = series.get_primes_lower_than_x(cells * cells)
image.paint_serie(prime_numbers, "#84b6f4")

image.draw_grid("#fdfd96")

image.savejpg('primes.png')

# Prime series:
# 
