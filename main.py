# from turtleimg import ImageNFT
from pillowimg import ImageNFT
import series

sizeh = 4096
sizew = 4096
cells = 10
margin = 50
font_size = 39
# serie = "primes"
serie = "fibonacci"

rs = "#fdcae1"
b = "#84b6f4"
y = "#fdfd96"
tc = "#ff5830"




for i in range(10, 101):
    cells = i
    image = ImageNFT(sizew, sizeh, margin, 'black', 'white')
    image.set_grid(cells, cells)

    numbers = series.get_numbers_lower_than_x(serie, cells * cells)
    print(numbers)
    image.paint_serie(numbers, 'white')
    image.add_text(f"{serie} series", margin, margin*1/5, tc, font_size)

    image.add_text(f"[b/w {cells * cells}]", margin, sizeh - margin, tc, font_size)

    image.add_text("[ak]", sizew - margin *2.3, sizeh - margin, tc, font_size)

    image.add_image("right.png", (sizew - margin*2, 0))
    image.draw_grid('white')

    image.savejpg(f'{serie} b-w {cells * cells}')

# image.show()

