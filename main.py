from PIL import Image, ImageDraw 
import series 

def draw_serie(image, serie, name):
  # Save the image as a JPG
  image.save(f"{name}.jpg", "JPEG")

def new_base_image(w, h, margin):
  # Create a new image with RGB mode
  image = Image.new("RGB", (w, h),  "white")
  draw = ImageDraw.Draw(image)
  draw.rectangle((margin, margin, w - margin, h - margin), fill="blue")
  return image

def draw_grid(img, num_rows, num_cols):
  width = img.width
  height = img.height
  cell_w = width / num_rows
    
    for x in range(0, width, cell_size):
        draw.line([(x, 0), (x, height)], fill='black')

    for y in range(0, height, cell_size):
        draw.line([(0, y), (width, y)], fill='black')

    return image

image = draw_grid(400, 400, 10, 10, 40)
image.save('grid.png')


size = 300
margin = 10
cells = 10
cell_size = size / cells

img = new_base_image(size, size, margin)

# Prime series:
x = 10
prime_numbers = series.get_first_x_primes(x)
draw_serie(img, prime_numbers, "primes")



