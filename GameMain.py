import pygame
pygame.init()
# width and height
surf = pygame.display.get_surface

# setting display, caption, icon, and bg_img
window = pygame.display.set_mode()
Width = window.get_width()
Height = window.get_height()
pygame.display.set_caption("Aqua Snap")
screenIcon = pygame.image.load('AquaSnapIcon.png')
bg_img = pygame.image.load('BeachPixel.jpg')
#scale of background
scale = pygame.transform.scale(bg_img, (Width, Height))
pygame.display.set_icon(screenIcon)
color_red = (100,20,0)
color_white = (0,0,0)
window.blit(scale,(0,0))
pygame.draw.rect(window, color_red, [Width - 80 , 0, 80 , 30])
smallfont = pygame.font.SysFont('Corbel',30) 
text = smallfont.render('X' , True , color_white)
window.blit(text , (Width - 45 , 0))

def main():
  
    run = True
    while run:
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if Width - 80 <= mouse[0] <= Width and 0 <= mouse[1] <= 30:
                    pygame.quit()
        
            mouse = pygame.mouse.get_pos()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



