import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("task")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Positions of the "yes" and "no" options
yes_rect = pygame.Rect(200, 400, 100, 50)
no_rect = pygame.Rect(500, 400, 100, 50)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    cursor_pos = pygame.mouse.get_pos()

    # Check if cursor is over "no" option
    if no_rect.collidepoint(cursor_pos):
        # Move the cursor to a random position
        pygame.mouse.set_pos(random.randint(0, width), random.randint(0, height))

    # Draw background
    screen.fill(white)

    

    # Draw "yes" and "no" options
    pygame.draw.rect(screen, red, yes_rect)
    pygame.draw.rect(screen, red, no_rect)

    # Draw text
    yes_text = font.render("Yes", True, white)
    no_text = font.render("No", True, white)
    screen.blit(yes_text, (yes_rect.centerx - yes_text.get_width() // 2, yes_rect.centery - yes_text.get_height() // 2))
    screen.blit(no_text, (no_rect.centerx - no_text.get_width() // 2, no_rect.centery - no_text.get_height() // 2))

    # Draw "Choose No" text
    choose_no_text = font.render("CHOOSE NO", True, black)
    screen.blit(choose_no_text, (width // 2 - choose_no_text.get_width() // 2, 150))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)


