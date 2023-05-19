import pygame
Window = pygame.display.set_mode((1100, 500), pygame.RESIZABLE)
screenIcon = pygame.image.load('AquaSnapIcon.png')
pygame.display.set_icon(screenIcon)
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()



