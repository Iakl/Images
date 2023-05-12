from PIL import Image, ImageDraw
import series


def draw_serie(image, serie, name):
    # Save the image as a JPG
    image.save(f"{name}.jpg", "JPEG")


def new_base_image(w, h, margin):
    # Create a new image with RGB mode
    image = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((margin, margin, w - margin, h - margin), fill="blue")
    return image


def draw_grid(image, num_rows, num_cols):
    # get the width and height in pixels of the image img
    width, height = image.size
    cell_w = int(width / num_rows)
    cell_h = int(height / num_cols)

    draw = ImageDraw.Draw(image)

    for x in range(0, width, cell_w):
        draw.line([(x, 0), (x, height)], fill='black')

    for y in range(0, height, cell_h):
        draw.line([(0, y), (width, y)], fill='black')

    # return image

size = 300
margin = 10
cells = 10

image = new_base_image(size, size, margin)
draw_grid(image, cells, cells)

image.save('grid.png')

# Prime series:
# x = 10
# prime_numbers = series.get_first_x_primes(x)
# draw_serie(img, prime_numbers, "primes")
