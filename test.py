import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 711, 711

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Background Colour
BACKGROUND = (11, 61, 145)

# Colour for Triangles
TRIANGLE_COLOUR = (255, 20, 147)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sierpiński Triangle Construction")
screen.fill(BACKGROUND)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Recursive function to draw the Sierpiński triangle
def draw_sierpinski(vertices, depth, screen):
    if depth == 0:
        pygame.draw.polygon(screen, TRIANGLE_COLOUR, vertices)
    else:
        # Calculate midpoints of the triangle's edges
        midpoints = [
            [(vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2],
            [(vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2],
            [(vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2],
        ]

        # Draw smaller triangles
        draw_sierpinski([vertices[0], midpoints[0], midpoints[2]], depth - 1, screen)
        draw_sierpinski([midpoints[0], vertices[1], midpoints[1]], depth - 1, screen)
        draw_sierpinski([midpoints[2], midpoints[1], vertices[2]], depth - 1, screen)

# Animation function
def animate_sierpinski(max_depth):
    running = True
    clock = pygame.time.Clock()
    depth = 0  # Start with depth 0

    # Define the initial large triangle vertices
    vertices = [
        (WIDTH / 2, 50),                 # Top vertex
        (50, HEIGHT - 50),              # Bottom-left vertex
        (WIDTH - 50, HEIGHT - 50),      # Bottom-right vertex
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND)  # Clear the screen
        draw_sierpinski(vertices, depth, screen)  # Draw the triangle up to the current depth
        pygame.display.flip()  # Update the display

        depth += 1  # Increment depth for the next frame
        if depth > max_depth:
            depth = max_depth  # Stop at the maximum depth

        clock.tick(1)  # Limit updates to 1 frame per second

    pygame.quit()

# Run the animation with a maximum depth of 8
animate_sierpinski(8)
