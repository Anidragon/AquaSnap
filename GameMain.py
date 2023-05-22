import sys
import pygame


#Creating a player class
#Cause you can create classes inside of classes in this shitty language
#Actually I think you can do it in java too but its stupid
class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, posX, posY):
        super().__init__()
        
        self.sprites = []
        self.sprites.append(pygame.image.load('RobotRightOne.png'))
        self.sprites.append(pygame.image.load('RobotRightTwo.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]
        self.is_animating = False

    def animate(self):
        self.is_animating = True

    def stopAnimate(self):
        self.is_animating = False
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]
pygame.init()
# width and height
surf = pygame.display.get_surface

# setting display, caption, icon, and bg_img and clock
window = pygame.display.set_mode((1280, 720))
Width = window.get_width()
Height = window.get_height()
pygame.display.set_caption("Aqua Snap")
screenIcon = pygame.image.load('AquaSnapIcon.png')
bg_img = pygame.image.load('BeachPixel.jpg')
clock = pygame.time.Clock()

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
#Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)
def main():
  
    run = True
    while run:
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if Width - 80 <= mouse[0] <= Width and 0 <= mouse[1] <= 30:
                    pygame.quit()
            if(event.type == pygame.KEYDOWN):
                player.animate()
            if(event.type == pygame.KEYUP):
                player.stopAnimate()

            mouse = pygame.mouse.get_pos()
        pygame.display.update()
        pygame.display.set_icon(screenIcon)
        moving_sprites.draw(window)
        moving_sprites.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()



