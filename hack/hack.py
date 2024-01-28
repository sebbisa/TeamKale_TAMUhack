import pygame
import random
import sys

# Initialize pygame
pygame.init()

# # Set up display
width, height = 700, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Guess the Number")

#create game window

bg_image = pygame.image.load('assets/photo_of_bomb.jpeg').convert_alpha()

# game loop
run = True
while run:

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# font_color = (0, 0, 0)

# # Fonts
# font = pygame.font.Font(None, 36)

# def draw_text(text, x, y):
#     text_surface = font.render(text, True, font_color)
#     screen.blit(text_surface, (x, y))

# def guess_the_number():
#     secret_number = random.randint(1, 10)
#     attempts = 3

#     while attempts > 0:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         screen.fill(white)
#         draw_text("Guess the number between 1 and 10:", 30, 50)
#         draw_text(f"Attempts left: {attempts}", 30, 100)

#         pygame.display.flip()

#         guess = input("Enter your guess: ")

#         try:
#             guess = int(guess)
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if guess == secret_number:
#             screen.fill(white)
#             draw_text("Congratulations! You guessed the correct number.", 30, 150)
#             pygame.display.flip()
#             pygame.time.wait(2000)  # Display the message for 2 seconds
#             pygame.quit()
#             sys.exit()
#         else:
#             screen.fill(white)
#             draw_text("Try again!", 30, 150)
#             pygame.display.flip()
#             pygame.time.wait(1000)  # Display the message for 1 second
#             attempts -= 1

#     screen.fill(white)
#     draw_text(f"Sorry, you ran out of attempts. The correct number was {secret_number}.", 30, 150)
#     pygame.display.flip()
#     pygame.time.wait(3000)  # Display the message for 3 seconds

# # Call the function to start the game
# guess_the_number()
