from PIL import Image, ImageDraw
import series

class ImageNFT:

  def __init__(self, w, h, margin, bgcolor="blue"):
      # Create a new image with RGB mode 
    self.margin = margin
    self.image = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(self.image)
    draw.rectangle((margin, margin, w - margin, h - margin), fill=bgcolor)
  
  
  def draw_grid(self, num_rows, num_cols, lcolor="black"):
      # get the width and height in pixels of the image img
    width, height = self.image.size
    cell_w = int((width -2*self.margin) / num_rows)
    cell_h = int((height -2*self.margin) / num_cols)

    draw = ImageDraw.Draw(self.image)

    for x in range(self.margin, width - self.margin, cell_w):
        draw.line([(x, self.margin), (x, height - self.margin)], fill=lcolor)

    for y in range(self.margin, height - self.margin, cell_h):
        draw.line([(self.margin, y), (width - self.margin, y)], fill='black')

  def draw_serie(self, serie, name):
    # Save the image as a JPG
    image.save(f"{name}.jpg", "JPEG")

  def savejpg(self, name):
    self.image.save(f"{name}.jpg", "JPEG")

size = 300
margin = 10
cells = 10

image = ImageNFT(size, size, margin)
image.draw_grid(cells, cells)

image.savejpg('grid.png')

# Prime series:
# x = 10
# prime_numbers = series.get_first_x_primes(x)
# draw_serie(img, prime_numbers, "primes")
