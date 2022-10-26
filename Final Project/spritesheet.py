import pygame
import json

#spritesheet and json code to cut up sprite sheet into smaller images

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png','json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
        
    def get_sprite(self, x, y, w, h): #function to get sprites cordinates from json
        sprite = pygame.Surface((w, h)) #make a blank canvas the size of the sprite being used
        sprite.set_colorkey((163,239,165)) #remove backround
        sprite.blit(self.sprite_sheet,(0,0),(x , y, w, h)) #find can cut out the sprite
        return sprite #delete the sprite from canvas
    
    def parse_sprite(self, name): #function the lets the user cut up sprite sheet
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image