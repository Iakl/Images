from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

  def add_image(self, path, pos):
    img_n = Image.open(path).convert("RGBA")
    img_n = img_n.resize((64, 64))
    mask = img_n.split()[3]  # Canal alfa
    self.image.paste(img_n, pos, mask=mask)

  def add_text(self, text, xp, yp, color='black', fsize=16):
    draw = ImageDraw.Draw(self.image)
    font_path = "iakl.ttf"
    font = ImageFont.truetype(font_path, fsize)
    draw.text((xp, yp), text, fill=color, font=font)
  
  def draw_grid(self, lcolor="white"):
    draw = ImageDraw.Draw(self.image)
    width, height =self.image.size

    for c in range(self.num_cols + 1):
        draw.line([(self.margin + c * self.cell_w, self.margin), (self.margin + c * self.cell_w, height - self.margin)], fill=lcolor, width=3)

    for r in range(self.num_rows + 1):
        draw.line([(self.margin, self.margin + r * self.cell_h, ), (width - self.margin, self.margin + r * self.cell_h)], fill=lcolor, width=3)

  def paint_serie(self, serie, scolor):
    for num in serie:
      x = num % self.num_cols
      y = int(num / self.num_rows)
      self.paint_cell(x, y, scolor)

  def paint_cell(self, x, y, ccolor):
    draw = ImageDraw.Draw(self.image)
    draw.rectangle((self.margin + x*self.cell_w, self.margin + y*self.cell_h, self.margin + (x+1)*self.cell_w, self.margin + (y+1)*self.cell_h), fill=ccolor)

  def savejpg(self, name):
    self.image.save(f"fibonacci series/{name}.jpg", "JPEG")

  def set_grid(self, num_rows, num_cols):
    width, height = self.image.size
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_w = (width -2*self.margin) / num_rows
    self.cell_h = (height -2*self.margin) / num_cols

  def show(self):
    # Display the image
    plt.imshow(self.image)
    plt.axis('off')  # Optional: Turn off axis labels and ticks

    # Show the plot
    plt.show()