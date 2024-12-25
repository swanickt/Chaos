from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
################################# SETTINGS #####################################

# Height and Width of the complex plane grid
WIDTH, HEIGHT = 2500, 2500

# Note that matplotlib colours must be normalized to have all values be between 0 and 1 (inclusive)
# Colour for points outside the mandelbrot set
OUTSIDE_M = (1, 1, 1)

# Colour for points inside the mandelbrot set
INSIDE_M = (0, 0, 0)

# The number of iterations to check whether |z_i|>2
MAX_ITERATIONS = 150

################################################################################

def binary_mandelbrot(height: int, width: int, max_it: int,
                      inside_colour: tuple[int, int, int], outside_colour: tuple[int, int, int]) -> None:

    # 1) Create a 2D grid of complex numbers (np.ogrid stands for "open grid")
        # np.ogrid returns two 1D arrays (vertical axis (imaginary part) and horizontal axis (real part))
        # -1.4:1.4:height*1j delivers height evenly spaced points along the imaginary axis from -1.4i to 1.4i
        # -2:0.8:width*1j delivers width evenly spaced points along the real axis from -2 to 0.8
        # in numpy, j = i = sqrt(-1)

    y, x = np.ogrid[-1.0:1.0:height*1j, -1.5:0.5:width*1j]  # Grid for complex plane
    c = x + y * 1j                                        # Complex numbers as c = x + yi (creates a numpy array of complex values)

    # 2) initialize a zero array to prepare for iterations
        # binary mask is a numpy array filled with zeros or ones
        # we will use mask to track whether each point in c belongs to the mandelbrot set

    z = np.zeros_like(c)  # creates a numpy array the same size as c, each value being 0 + 0j
    mask = np.zeros(z.shape, dtype=int) # Binary mask to indicate divergence (0 = inside, 1 = outside)
    # z.shape ensures that the new array mask has the same dimensions as z

    # 3) Iterate over each point to check for divergence
    for _ in range(max_it):
        z = z**2 + c
        diverge = np.abs(z) > 2                  # Check divergence condition |z| > 2
        mask[diverge] = 1                        # Mark diverging points as outside the set
        z[diverge] = 0                           # Stop further computation for diverged points

    # 4) Create the binary colour map
    colours = [inside_colour, outside_colour]
    colour_map = ListedColormap(colours)
    # 5) Plot the Mandelbrot set with the custom colormap
    plt.figure(figsize=(WIDTH / 100, HEIGHT / 100))
    plt.imshow(mask, cmap=colour_map)
    plt.title("Binary Mandelbrot Set")
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.show()

################################################################################

if __name__ == "__main__":
    binary_mandelbrot(HEIGHT, WIDTH, MAX_ITERATIONS, INSIDE_M, OUTSIDE_M)
