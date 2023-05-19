import pygame
# width and height
Width = 1100
Height = 500
# setting display, caption, icon, and bg_img
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Aqua Snap")
screenIcon = pygame.image.load('AquaSnapIcon.png')
bg_img = pygame.image.load('BeachPixel.jpg')
#scale of background
scale = pygame.transform.scale(bg_img, (Width, Height))
pygame.display.set_icon(screenIcon)


def main():
  
    run = True
    while run:
        
        window.blit(scale,(0,0))
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
        

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



