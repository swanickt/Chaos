import pygame
import colorsys

# Screen dimensions
WIDTH, HEIGHT = 800, 800

# Mandelbrot parameters
MAX_ITER = 100
ZOOM = 200  # Pixels per unit in the complex plane
CENTER_X, CENTER_Y = -0.5, 0  # Center of the complex plane


def mandelbrot(c):
    """
    Calculate the escape time for a complex number c in the Mandelbrot set.
    Returns the number of iterations before escape (or MAX_ITER if it doesn't escape).
    """
    z = 0
    for n in range(MAX_ITER):
        z = z**2 + c
        if abs(z) > 2:
            return n + 1 - (abs(z) - 2) / 2  # Smooth iteration count
    return MAX_ITER


def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB.
    """
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def draw_mandelbrot(screen):
    """
    Draw the Mandelbrot set on the Pygame screen.
    """
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Map pixel to the complex plane
            a = (x - WIDTH / 2) / ZOOM + CENTER_X
            b = (y - HEIGHT / 2) / ZOOM + CENTER_Y
            c = complex(a, b)

            # Calculate escape time
            m = mandelbrot(c)

            # Map escape time to hue
            hue = m / MAX_ITER
            color = hsv_to_rgb(hue, 1, 1) if m < MAX_ITER else (0, 0, 0)

            # Draw the pixel
            screen.set_at((x, y), color)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mandelbrot Set with Hue Coloring")

    # Draw the Mandelbrot set
    draw_mandelbrot(screen)
    pygame.display.flip()

    # Event loop to keep the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
