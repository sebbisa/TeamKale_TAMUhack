import pygame
import random
import sys

# Initialize pygame
pygame.init()

# # Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brain Blast")

color_light = (170, 170,170)

color_dark = (100,100,100)

color = (255, 255, 255)
smallfont = pygame.font.SysFont('Corbel', 35, bold=False, italic=False)

text = smallfont.render('quit', True, color)

#create game window

bg_image = pygame.image.load('assets/photo_of_bomb.jpeg').convert_alpha()

# game loop
run = True
while run:

    # draw background
    screen.blit(bg_image, (0,0))
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
    # update display window
    pygame.display.update()

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
