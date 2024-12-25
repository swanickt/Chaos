import pygame

################################# SETTINGS #####################################

# Height and Width of the numpy screen
WIDTH, HEIGHT = 750, 750

# The number of iterations to check whether |z_i|>2
MAX_ITERATIONS = 150

################################################################################

# function to compute whether a points sequence escapes to infinity

def mandelbrot_inclusion(c: complex) -> int:
    """
    Calculate the escape time for a complex number c in the Mandelbrot set.
    Returns the number of iterations before escape (or -1 if it doesn't escape).
    """
    z = 0 + 0j      # setting z to the complex number 0+0i
    i = 0           # index to track number of iterations

    while (abs(z) <= 2 and i <= MAX_ITERATIONS):
        z = z*z + c
        i += 1

    if i > MAX_ITERATIONS:
        return -1
    return i + 1 - (abs(z) - 2) / 2  # Smooth iteration count

def escape_time_colour(iterations: int) -> tuple[int, int, int]:
    if iterations == -1:
        return 0, 0, 0        # points inside the mandelbrot set are coloured black

        # Calculate color based on escape time
    # Transition from orange to yellow to blue
    hue = (iterations / MAX_ITERATIONS) * 811
    saturation = 1.0
    value = 1.0

    return hsv_to_rgb(hue, saturation, value)

# Converts HSV (hue, saturation, value) to RGB
def hsv_to_rgb(hue, saturation, value):
    # Ensure hue is between 0 and 360
    hue = hue % 360
    c = value * saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = value - c

    if 0 <= hue < 60:
        r, g, b = c, x, 0
    elif 60 <= hue < 120:
        r, g, b = x, c, 0
    elif 120 <= hue < 180:
        r, g, b = 0, c, x
    elif 180 <= hue < 240:
        r, g, b = 0, x, c
    elif 240 <= hue < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    # Add m to shift the color
    r, g, b = (r + m) * 255, (g + m) * 255, (b + m) * 255

    return int(r), int(g), int(b)

def main():
    """
    Draw the Mandelbrot set on the Pygame screen.
    """

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mandelbrot Set Fractal")

    # Loop through each pixel in the image
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Map pixel coordinates to complex plane
            real = (x / WIDTH) * 3.5 - 2.5      # real axis will range in [-2.5, 0.5]
            imaginary = (y / WIDTH) * 3.2 - 1.7         # imaginary axis will range in [-1.7, 1.5]
            c = complex(real, imaginary)

            iterations = mandelbrot_inclusion(c)
            colour = escape_time_colour(iterations)
            screen.set_at((x,y), colour)

    pygame.display.flip()


    # Game loop to keep the screen open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
################################################################################

# painting the fractal:
if __name__ == '__main__':
    main()