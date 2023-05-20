from turtleimg import ImageNFT
import series

sizeh = 512
sizew = 512
cells = 10
margin = 5
#margin = sizew / (cells + 2)

rs = "#fdcae1"
b = "#84b6f4"
y = "#fdfd96"
tc = "#ff5830"


image = ImageNFT(sizew, sizeh, margin, 'black', 'white')
#image.set_grid(cells, cells)

# prime_numbers = series.get_primes_lower_than_x(cells * cells)
# image.paint_serie(prime_numbers, 'white')
# image.add_text("primes series", margin, margin*1/4, tc, int(margin * 2/3))

# image.add_text(f"[b/w {cells * cells}]", margin, sizeh - margin, tc, int(margin * 2/3))

# image.add_text("[ak]", sizew - margin *2.3, sizeh - margin, tc, int(margin * 2/3))

# image.add_image("right.png", (sizew - margin*2, 0))
#image.draw_grid('white')

# image.savejpg('primes')

# image.show()

