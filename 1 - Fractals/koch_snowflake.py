import pygame
import math

################################# SETTINGS #####################################

# Screen dimensions
WIDTH, HEIGHT = 800, 800

# Background Colour
BACKGROUND = (135, 206, 235)

# Line Colour
LINE_COLOUR = (25, 25, 112)

# The number of iterations to perform
ITERATIONS = 7

################################################################################

# Setup for pygame
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Koch Snowflake Construction")
window.fill(BACKGROUND)

def distance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    """Calculate the distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def koch_snowflake(order: int, points: list[tuple[int, int]], surface: pygame.Surface) -> None:
    """
    Recursively draw the Koch snowflake.

    order: The current depth of recursion.
    points: A list of points representing the current curve.
    surface: The pygame surface to draw on.
    """
    if order == 0:
        # Draw a line between consecutive points
        # The last argument represents the thickness of the lines
        for i in range(len(points) - 1):
            pygame.draw.line(surface, LINE_COLOUR, points[i], points[i + 1], 2)
    else:
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]

            # Calculate the three new points
            dx = (p2[0] - p1[0]) / 3
            dy = (p2[1] - p1[1]) / 3

            # First point (1/3 along the segment)
            p3 = (p1[0] + dx, p1[1] + dy)

            # Second point (apex of the triangle)
            px = (p1[0] + p2[0]) / 2 - math.sqrt(3) * (p2[1] - p1[1]) / 6
            py = (p1[1] + p2[1]) / 2 + math.sqrt(3) * (p2[0] - p1[0]) / 6
            p4 = (px, py)

            # Third point (2/3 along the segment)
            p5 = (p1[0] + 2 * dx, p1[1] + 2 * dy)

            # Append points in the correct order
            new_points.extend([p1, p3, p4, p5])

        # Add the last point of the original segment
        new_points.append(points[-1])

        # Recur for the next order
        koch_snowflake(order - 1, new_points, surface)


def animate_koch_snowflake(iterations):
    """Animate the construction of the Koch snowflake."""
    running = True
    clock = pygame.time.Clock()
    depth = 0  # Start at 0 iterations

    # Define the initial triangle
    size = 550
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    p1 = (center_x - size // 2, center_y + size // 3)
    p2 = (center_x + size // 2, center_y + size // 3)
    p3 = (center_x, center_y - size * 2 // 3)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        window.fill(BACKGROUND)

        # Draw the Koch snowflake
        koch_snowflake(depth, [p1, p2, p3, p1], window)

        # Update the display
        pygame.display.flip()

        depth += 1  # Increment depth for the next frame
        if depth > iterations:
            depth = iterations  # Stop at the maximum depth

        clock.tick(1)  # Limit updates to 1 frame per second

    pygame.quit()

################################################################################

if __name__ == '__main__':
    # Run the animation
    animate_koch_snowflake(ITERATIONS)
