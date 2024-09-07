from setting import *
from os import join
from os import walk

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('shooting game')
        self.clock = pygame.time.Clock()
        self.running = True
        
        #group
        self.sprite = pygame.sprite.Group()
        self.collision_sprite = pygame.sprite.Group()
    
    def setup(self):
        map = load_pygame(join('data','map','map.tmx'))
    
    def run(self):
        while self.running:
            datatime = self.clock.tick(FRAME) / 1000
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # update the sprite
            self.sprite.update(datatime)
            
            # draw the interface
            self.display.fill(Background_COLOR)
            self.sprite.draw(self)
            
        pygame.quit()