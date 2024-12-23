import pygame

################################# SETTINGS #####################################

# Screen dimensions
WIDTH, HEIGHT = 711, 711

# Background Colour
BACKGROUND = (135, 206, 235)

# Colour for Triangles
TRIANGLE_COLOUR = (25, 25, 112)

# The number of iterations to perform
ITERATIONS = 8

################################################################################

# Setup for pygame
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sierpiński Triangle Construction")
window.fill(BACKGROUND)


# Recursive function to draw the Sierpiński triangle
def sierpinski(vertices: list[tuple[int, int]], depth: int, frame: pygame.Surface) -> None:
    if depth == 0:
        pygame.draw.polygon(frame, TRIANGLE_COLOUR, vertices)
    else:
        # Calculate midpoints of the triangle's edges
        midpoints = [
            [(vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2],
            [(vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2],
            [(vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2],
        ]

        # Draw smaller triangles
        sierpinski([vertices[0], midpoints[0], midpoints[2]], depth - 1, frame)
        sierpinski([midpoints[0], vertices[1], midpoints[1]], depth - 1, frame)
        sierpinski([midpoints[2], midpoints[1], vertices[2]], depth - 1, frame)


# Function to animate the process
def sierpinski_animation(iterations: int) -> None:
    running = True
    clock = pygame.time.Clock()
    depth = 0  # Start with depth 0

    # Define the initial large triangle vertices
    vertices = [
        (WIDTH / 2, 50),                # Top vertex
        (50, HEIGHT - 50),              # Bottom-left vertex
        (WIDTH - 50, HEIGHT - 50),      # Bottom-right vertex
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(BACKGROUND)  # Clear the screen
        sierpinski(vertices, depth, window)  # Draw the triangle up to the current depth
        pygame.display.flip()  # Update the display

        depth += 1  # Increment depth for the next frame
        if depth > iterations:
            depth = iterations  # Stop at the maximum depth

        clock.tick(1)  # Limit updates to 1 frame per second

    pygame.quit()

################################################################################


# Run the animation with a maximum depth of ITERATIONS
sierpinski_animation(ITERATIONS)
