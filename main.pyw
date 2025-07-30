#import loadscreen
import pygame, sys, pickle

#import level
from pygame.math import Vector2
from os import path
from loadimage import *
from time import sleep
from math import sqrt


#pygame
pygame.init()
pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 4096)

#tile
tile_size = 32
tile_num = 16



#screen
screen_width = tile_size * tile_num
screen_height = tile_size * tile_num + 150
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pyescape")
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()

#fonts 
game_font = pygame.font.Font('fonts/PoetsenOne-Regular.ttf', 15)
dots_font = pygame.font.Font('fonts/4x4kanafont.ttf', 16)

#color 
WHITE = (255,255,255)

#game
load_level = 1
bg_img = 0
level_list = []

#variables for debug
debug = False

#souds 
key_open_sound = pygame.mixer.Sound('sounds/key_open.wav')
die_sound = pygame.mixer.Sound('sounds/die.wav')
break_sound = pygame.mixer.Sound('sounds/break.wav')





#level




def load_level(level, x, y):
    current_bgm = main_game.current_level.bgm
    main_game.current_level = level_list[level - 1]
    main_game.player.pos = Vector2(x*tile_size + main_game.player.width/2 , y*tile_size + main_game.player.height/2)
    main_game.play_bgm(main_game.current_level.bgm, current_bgm)
    
def play_sound(sound, volume):
    sound_channel = sound.play()
    sound_channel.set_volume(volume)

class Messege_box():
    def __init__(self):
        self.bg = pygame.image.load('images/message.png').convert()
        pass
    
    def message(self, massage):
        massage_surface = game_font.render(massage, True, WHITE)
        
        screen.blit(self.bg , (0, screen_height - 150))
        screen.blit(massage_surface, (tile_size, tile_size * 3))
        main_game.player.active = False
        
        
        

    def option(self, option1, option2=None, option3=None, option4=None):
        option_list = [option1, option2, option3, option4]
        i = 0
        for option in option_list:
            if not option == None:
                pass
                option_surface = game_font.render(option, True, WHITE)
                screen.blit(option_surface, (50, 32 * (16 + i)))
        i += 1
    
    def draw(self):
        screen.blit(self.bg , (0, screen_height - 150))


class Level:
    def __init__(self, bg, data, warp_points, bgm, level_num):
        self.level_num = level_num
        self.bg_tile = bg
        self.tile_list = []
        self.bgm = bgm
        #spite group
        self.door_group = pygame.sprite.Group()
        self.key_group = pygame.sprite.Group()
        self.bat_group = pygame.sprite.Group()
        self.treasurebox_group = pygame.sprite.Group()
        self.teddybear_group = pygame.sprite.Group()
        self.barrel_group = pygame.sprite.Group()
        
        

        self.warp_point_list = warp_points

        
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 2:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 3:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 4:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 5:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 6:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 7:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 8:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 9:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 10:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 11:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 12:  self.create_tile(col_count, row_count, images[tile -1])            
                
                if tile == 13:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 14:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 15:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 16:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 17:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 18:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 19:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 20:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 21:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 22:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 23:  self.create_tile(col_count, row_count, images[tile -1])
                if tile == 24: 
                    door = Door(col_count * tile_size, row_count * tile_size, door1_right_img, 1)
                    self.door_group.add(door)

                    #img = pygame.transform.scale(door_right_img, (tile_size, tile_size * 2))
                    #img_rect = img.get_rect()
                    #img_rect.x = col_count * tile_size
                    #img_rect.y = row_count * tile_size
                    #tile = (img, img_rect, True)
                    #self.tile_list.append(tile)
                if tile == 25: 
                    door = Door(col_count * tile_size, row_count * tile_size, door1_left_img, 1)
                    self.door_group.add(door)

                    #img = pygame.transform.scale(door_left_img, (tile_size, tile_size * 2))
                    #img_rect = img.get_rect()
                    #img_rect.x = col_count * tile_size
                    #img_rect.y = row_count * tile_size
                    #tile = (img, img_rect, True)
                    #self.tile_list.append(tile)	
                if tile == 26: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 27: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 28: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 29: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 30: self.create_tile(col_count, row_count, images[tile -1])	
                if tile == 31: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 32: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 33: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 34: self.create_tile(col_count, row_count, images[tile -1])	
                if tile == 35: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 36: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 37: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 38: self.create_tile(col_count, row_count, images[tile -1])	
                if tile == 39: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 40: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 41: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 42: self.create_tile(col_count, row_count, images[tile -1])	
                if tile == 43: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 44: self.create_tile(col_count, row_count, images[tile -1], False)

                if tile == 45: self.key_group.add(Key(col_count * tile_size, row_count * tile_size, 1))

                if tile == 46: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 47: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 48: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 49: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 50: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 51: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 52: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 53: self.create_tile(col_count, row_count, images[tile -1])

                if tile == 54: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 55: self.create_tile(col_count, row_count, images[tile -1], False)
                if tile == 56: self.create_tile(col_count, row_count, images[tile -1], False)       
                
                if tile == 57: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 58: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 59: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 60: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 61: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 62: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 63: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 64: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 65: self.bat_group.add(Bat(col_count * tile_size, row_count * tile_size))     
                if tile == 66: self.treasurebox_group.add(Treasurebox(col_count * tile_size, row_count * tile_size, 'brown', 'axe'))  
                if tile == 67: self.treasurebox_group.add(Treasurebox(col_count * tile_size, row_count * tile_size, 'brown', 'key2'))         
                if tile == 68: self.treasurebox_group.add(Treasurebox(col_count * tile_size, row_count * tile_size, 'brown', 'key3'))         
       
                if tile == 69: self.teddybear_group.add(Teddy_bear(col_count * tile_size, row_count * tile_size))
                
                if tile == 70: self.door_group.add(Door(col_count * tile_size, row_count * tile_size, images[tile -1], 2))                 
                if tile == 71: self.door_group.add(Door(col_count * tile_size, row_count * tile_size, images[tile -1], 2))      
                if tile == 72: self.door_group.add(Door(col_count * tile_size, row_count * tile_size, images[tile -1], 3))                 
                if tile == 73: self.door_group.add(Door(col_count * tile_size, row_count * tile_size, images[tile -1], 3))
                
                if tile == 74: self.key_group.add( Key(col_count * tile_size, row_count * tile_size, 2) )
                if tile == 75: self.key_group.add( Key(col_count * tile_size, row_count * tile_size, 3) )                
                if tile == 76: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 77: self.barrel_group.add(Barrel(col_count * tile_size, row_count * tile_size))
                
                if tile == 78: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 79: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 80: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 81: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 82: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 83: self.create_tile(col_count, row_count, images[tile -1])
                if tile == 84: self.create_tile(col_count, row_count, images[tile -1], False)                                
                
                     
                col_count += 1
            row_count += 1
        
    def create_tile(self, col, row, image, collision = True):
        img = pygame.transform.scale(image, (tile_size, tile_size))
        img_rect = img.get_rect()
        img_rect.x = col * tile_size
        img_rect.y = row * tile_size
        tile = [img, img_rect, collision]
        self.tile_list.append(tile)
                        
    def draw_bg(self):
        #draw backgound
        for image_x in range(tile_num):
            for image_y in range(tile_num):
                screen.blit(self.bg_tile, (image_x*32, image_y*32))       

    def draw_elements(self):
        #draw elements on the level
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
                
    def draw_grid(self):
        for line in range(0, tile_num):
            pygame.draw.line(screen, WHITE, (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(screen, WHITE, (line * tile_size, 0), (line * tile_size, screen_height))
            

    def draw(self):
        self.draw_bg()
        self.draw_elements()

# the key class 
class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, keynum):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'images/key{keynum}.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.keynum = keynum
    
    def update(self):
        if pygame.sprite.pygame.sprite.collide_rect(main_game.player, self): # check for collision with key and remove key from the group when collison occur
            print (f"key{self.keynum} collected")
            main_game.player.items.append(f'key{self.keynum}')
            main_game.current_level.key_group.remove(self)
            
class Treasurebox(pygame.sprite.Sprite):
    def __init__(self, x, y, color, item_name):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.images = []
        for i in range(1, 4):
            image = pygame.image.load(f'images/treasurebox_{color}{i}.png').convert_alpha()
            self.images.append(image)
        self.image = self.images[0]
        self.rect = self.image.get_rect( topleft=(self.x, self.y) )
        self.item = item_name
        self.open = False
        self.index = 0
        self.counter = 0
        
        
    def update(self):
        if pygame.sprite.collide_rect(self, main_game.player) and not self.open: # open action
            main_game.player.items.append(self.item)
            self.open = True
            play_sound(key_open_sound, 30)     
            print (self.item + ' collected')
        if self.open and self.index < 2:# open animation if opened
            self.counter += 1
            if self.counter == 5:
                self.counter = 0
                self.index += 1
                0
                self.image = self.images[self.index]
            
            

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, image, keynum):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.keynum = keynum
        
    def update(self):
        #check for collision with sprits in the door sprite list and open the door if player have a key  
        if main_game.player.items.count(f'key{self.keynum}') > 0: #if player have a key 
            if pygame.sprite.collide_rect(self, main_game.player): #door open 
                for side_door in main_game.current_level.door_group: 
                    if side_door.rect.x == self.rect.x + tile_size or side_door.rect.x == self.rect.x - tile_size: #if any other door is sitting besite the door, open that doo togather. this side dores are detected by theire position base
                        main_game.player.items.pop(main_game.player.items.index(f'key{self.keynum}')) #delete used key from player's item
                        main_game.current_level.door_group.remove(side_door)
                main_game.current_level.door_group.remove(self)
                play_sound(key_open_sound, 30)
        else: # if player don't have a key
            if self.rect.colliderect(int(main_game.player.rect.x), int(main_game.player.nextpos.y), main_game.player.width, main_game.player.height):
                main_game.player.dpos.y = self.rect.bottom - main_game.player.rect.top
                
                
class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(x, y)
        self.image = barrel_img
        self.rect = self.image.get_rect( topleft=(self.pos.x, self.pos.y) )
        self.width = self.rect.width
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y - 2, tile_size, tile_size * 4)
        self.broke = False

    def update(self):
        #collision detect - hitbox
        if self.rect.colliderect(int(main_game.player.nextpos.x), int(main_game.player.rect.y), main_game.player.width, main_game.player.height): 
            if main_game.player.items.count('axe') > 0 and not self.broke: # break barrel if player have axe 
                # open aciton
                #main_game.current_level.barrel_group.remove(self)
                self.image = pygame.image.load('images/barrel2.png').convert_alpha()
                play_sound(break_sound, 25)
                self.broke = True
                
            elif not self.broke:
                main_game.player.dpos.x = self.hitbox.left - main_game.player.rect.right   
            else:
                pass
            
     
        
        pass
                

class Bat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(x, y)
        self.direction = Vector2(0, 1)
        self.iamge_list = []
        self.speed = 6
        self.images_right = []
        self.images_left = []
        self.images_up = []
        self.images_down = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):#append images to the image list
            #horizontal img
            img_right = pygame.image.load(f'images/bat_right{num}.png').convert_alpha()
            img_left = pygame.transform.flip(img_right, True, False) #flip image for left direction 
            self.images_right.append(img_right)
            self.images_left.append(img_left)
            #vertical img
            img_up = pygame.image.load(f'images/bat_up{num}.png').convert_alpha()
            img_down = pygame.image.load(f'images/bat_down{num}.png').convert_alpha()
            self.images_up.append(img_up)
            self.images_down.append(img_down)
        self.image = self.images_down[1]
        self.rect = self.image.get_rect( topleft=(int(self.pos.x), int(self.pos.y)) )

    def update(self):
        #position update
        self.pos += self.direction*self.speed #move bat to the self direciton
        nextpos = self.pos + self.direction*self.speed
     
        for tile in main_game.current_level.tile_list:
            #check for collision in y 
            if tile[1].colliderect(self.rect.x, nextpos.y, self.rect.width, self.rect.height) and tile[2]:
                #check if player moving up
                self.direction = self.direction * -1

        #animation
        self.counter += 1
        if self.counter == 3: # if the counter is 3 change the image respose to the direciton and update rectangle.
            if self.index == 2:
                self.index = 0
            else:
                self.index += 1
            self.counter = 0
            if self.direction.y > 0:
                self.image = self.images_down[self.index]
            if self.direction.y < 0:
                self.image = self.images_up[self.index]
            #update rect size and position 
            self.rect = self.image.get_rect( topleft=(self.pos.x, self.pos.y) ) # update self.rect

class Teddy_bear(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(x, y)
        self.direciton = Vector2(0, 0)
        self.speed = 2.5
        self.active = False
        self.images = []
        for i in range(1, 3): #load images
            image = pygame.image.load(f'images/teddy_bear{i}.png').convert_alpha()
            self.images.append(image)
        self.image = self.images[0]
        self.rect = self.image.get_rect( topleft=(int(self.pos.x), int(self.pos.y)) )
        self.width = self.rect.width
        self.height = self.rect.height
        
    def collision_check(self):
        if pygame.sprite.collide_rect(self, main_game.player):
            main_game.player.die()
        
    def update(self):
        #If player get close to within 3 tiles, activate self
        if sqrt((self.pos.x - main_game.player.pos.x)**2) // tile_size < 3 and sqrt((self.pos.y - main_game.player.pos.y)**2) // tile_size < 3 and not self.active:
            self.active = True
            self.image = self.images[1]
            #change tile if level is 8
            if main_game.current_level.level_num == 8:
                main_game.current_level.tile_list[6][0] = wall_right_bottom_img
                main_game.current_level.tile_list[9][0] = wall_left_bottom_img
                main_game.current_level.tile_list.pop(8)
                main_game.current_level.tile_list.pop(7)
            
        self.collision_check()
            
        #chase player 
        #deside self direction       
        if self.active:
            #for y
            if self.pos.y - self.speed > main_game.player.rect.y:
                self.direciton.y = -1
            elif self.pos.y + self.speed < main_game.player.rect.y:
                self.direciton.y = 1
            else:
                self.direciton.y = 0            
            
                #for x
                if self.pos.x - self.speed> main_game.player.rect.x:
                    self.direciton.x = -1
                elif self.pos.x + self.speed < main_game.player.rect.x:
                    self.direciton.x = 1
                else:
                    self.direciton.x = 0

        #update position
        self.pos += self.direciton * self.speed
        self.rect.x, self.rect.y = int(self.pos.x), int(self.pos.y) 
        self.direciton = Vector2(0, 0)


class Player:
    def __init__(self):
        self.pos = Vector2(200, 200)
        self.direction = Vector2(0, 0)
        self.direction_old = Vector2(0, 0)
        self.speed = 5 
        self.items = []
        self.images_right = []
        self.images_left = []
        self.images_up = []
        self.images_down = []
        self.index = 2
        self.counter = 0     
        self.action = False   
        for num in range(1, 4):#append images to the image list
            #horizontal img
            img_right = pygame.image.load(f'images/player_right{num}.png').convert_alpha()
            img_left = pygame.transform.flip(img_right, True, False) #flip image for left direction 
            self.images_right.append(img_right)
            self.images_left.append(img_left)
            #vertical img
            img_up = pygame.image.load(f'images/player_up{num}.png').convert_alpha()
            img_down = pygame.image.load(f'images/player_down{num}.png').convert_alpha()
            self.images_up.append(img_up)
            self.images_down.append(img_down)
        self.image = self.images_down[1]
        #self.rect = self.image.get_rect( center = (self.pos.x, self.pos.y) )
        self.width = self.image.get_width() - 10
        self.height = self.image.get_height() - 23
        self.rect = pygame.Rect(int(self.pos.x - self.width/2), int(self.pos.y - self.height/2), self.width, self.height)
        self.active = True
        self.deth_cout = 0
        
        # self.player.rect.x, self.player.rect.y, self.player.width, self.player.height
        
    def warp(self):# when player wark into a warp point
        for warp_point in main_game.current_level.warp_point_list:
            if warp_point[0] == self.pos.x // tile_size and warp_point[1] == self.pos.y // tile_size:
                load_level(warp_point[2], warp_point[3], warp_point[4])

    def update(self):
        walk_cooldown = 5
        self.active = True

        #check key inputs
        pygame.event.pump()   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = Vector2(0, -1)
        if keys[pygame.K_DOWN]:
            self.direction = Vector2(0, 1)
        if keys[pygame.K_RIGHT]:
            self.direction = Vector2(1, 0)
        if keys[pygame.K_LEFT]:
            self.direction = Vector2(-1, 0)   

        #animation
        self.counter += 1
        if self.counter > walk_cooldown or not self.direction_old == self.direction:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0            
            
            if self.direction.x > 0: #right
                self.image = self.images_right[self.index]
            elif self.direction.x < 0: #left
                self.image = self.images_left[self.index]                
            elif self.direction.y > 0: #down
                self.image = self.images_down[self.index]
            elif self.direction.y < 0: #up
                self.image = self.images_up[self.index]                                
            else:
                pass
            #    self.index = 0
            #    self.counter = 7
            #    self.image = self.images_down[1]
        
        self.dpos = self.direction * self.speed   
        self.nextpos = Vector2(self.rect.x, self.rect.y) + self.dpos            
         
        #CHECK COLLISION
        for tile in main_game.current_level.tile_list:
            #check for collision in x
            if tile[1].colliderect(int(self.nextpos.x), self.rect.y, self.width, self.height) and tile[2]:
                #check if player moving left
                if self.direction.x < 0:
                    self.dpos.x = tile[1].right - self.rect.left
                #check if player moving right 
                if self.direction.x > 0:
                    self.dpos.x = tile[1].left - self.rect.right    

            #check for collision in y 
            if tile[1].colliderect(self.rect.x, int(self.nextpos.y), self.width, self.height) and tile[2]:
                #check if player moving up
                if self.direction.y < 0:
                    self.dpos.y = tile[1].bottom - self.rect.top
                #check if player moving down 
                if self.direction.y > 0:
                    self.dpos.y = tile[1].top - self.rect.bottom


        #collision with sprite
        #door
        main_game.current_level.door_group.update()

        main_game.current_level.barrel_group.update()

        
        #bat
        if pygame.sprite.spritecollide(self, main_game.current_level.bat_group, False):
            self.die()
            

        


        #update player position while keep player in the level
        if ( 0 < int(self.nextpos.x) < screen_width and 0 < self.nextpos.y < screen_height - 150 and self.active):
            self.pos += self.dpos
        
        #if not 0 <= self.pos.x + self.direction.x * self.speed >= screen_width and not 0 <= self.pos.y + self.direction.y * self.speed >= screen_height - 150 and self.active:
        #    self.pos += self.dpos

        self.direction_old = self.direction
        self.direction = Vector2(0, 0) #reset direction 
        #if pygame.sprite.spritecollide(self, door_group, False) and self.item.count('key') > 0:
        #    pygame.sprite.spritecollide(self, door_group, True)
        #    self.item.pop(self.item.index('key'))

            
        #check for warp points
        self.warp()

    def die(self):
        self.deth_cout += 1
        pygame.mixer.music.pause()
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, screen_width, screen_height)) 
        die_img = self.images_left[1]
        for i in range(90):
            i *= -1
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, screen_width, screen_height))         
            screen.blit(pygame.transform.rotate(die_img, i), (screen_width/2, screen_height/2))
            pygame.display.update()

            sleep(0.005)
            
            
        play_sound(die_sound, 25)        
        sleep(2)
        load_level(1, 6, 6)
        pygame.mixer.music.unpause()
        #main_game.current_level = level_list[0]
        #self.pos = Vector2(200, 200)
            
    def draw_player_item(self):
        #draw player's items on screen
        item_count = 1
        for item in self.items: #draw item on screen for each items in the list 
            if item == 'key1':
                item_img = key1_img
                screen.blit(item_img, (32 * item_count,tile_size * 16))   
            elif item == 'key2':
                item_img = key2_img
                screen.blit(item_img, (32 * item_count,tile_size * 16)) 
            elif item == 'key3':
                item_img = key3_img
                screen.blit(item_img, (32 * item_count,tile_size * 16))   
            elif item == 'axe':
                screen.blit(axe_img, (32 * item_count,tile_size * 16))                          
            item_count += 1     
        
    def draw(self):
       
        #self.rect = self.image.get_rect( center = (self.pos.x, self.pos.y) )
        
        self.rect = pygame.Rect(int(self.pos.x - self.width/2), int(self.pos.y - self.height/2), self.width, self.height)
        screen.blit(self.image, (self.rect.x -5, self.rect.y - 23))


class Main:
    def __init__(self):
        self.player = Player()
        self.current_level = level_list[0] #0 ~ 9
        self.play_bgm(self.current_level.bgm)

    def debug(self): #debug
        if debug:
            pygame.display.set_caption("Test game - debug | fps" + str(int(clock.get_fps())))



            player_pos = str(self.player.pos)
            player_dpos = str(self.player.direction_old)

            pos_surface = game_font.render('position' + player_pos, True, WHITE)
            direction_surface = game_font.render('direction' + player_dpos, True, WHITE)
            overlap = game_font.render('overlap', True, (255,5,5))

            #dubug texts
            
            screen.blit(pos_surface, (10, 5)) #position 
            screen.blit(direction_surface, (10, 25)) #direction

            for tile in self.current_level.tile_list: #overlap and tile hit box
                if tile[2]:
                    pygame.draw.rect(screen, WHITE, tile[1], 1) 
                if tile[1].colliderect(self.player.rect):
                    screen.blit(overlap, (10,45))
             #player hitbox
            pygame.draw.rect(screen, WHITE, (self.player.rect), 1)
            
            
            # sprotes hit box 
            for barrel in self.current_level.barrel_group:
                pygame.draw.rect(screen, WHITE, barrel.rect, 1)
            
            for bat in self.current_level.bat_group:
                pygame.draw.rect(screen, WHITE, bat.rect, 1)
                
            for teddy_bear in self.current_level.teddybear_group:
                pygame.draw.rect(screen, WHITE, teddy_bear.rect, 1)
            
            
            
            #trigger by key input
            pygame.event.pump()   
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]: #reset player position 
                self.player.pos = Vector2(200, 200)
            
        else:
            pygame.display.set_caption("Test game")
            
    def play_bgm(self, bgm_name, current_bgm=''):
        if not bgm_name == current_bgm:
            pygame.mixer.music.load(f'music/{bgm_name}.wav')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)        
            
    def win_state(self):
        win_text = 'Congratulations you are escaped!'
        win_text_surface = dots_font.render(win_text, True, WHITE)
        pygame.transform.rotozoom(win_text_surface, 0, 5) 
        screen.blit(win_text_surface, (screen_width/2 - win_text_surface.get_width()/2, (screen_height - 150)/4 - win_text_surface.get_height()/2))
        
            


    def update(self):
        
        self.player.update()
        self.current_level.key_group.update()
        self.current_level.bat_group.update()
        self.current_level.treasurebox_group.update()
        self.current_level.teddybear_group.update()
        
       # self.current_level.butler_group.update()


    def draw(self):

        self.current_level.draw()

        self.current_level.door_group.draw(screen)
        self.current_level.key_group.draw(screen)
        self.current_level.bat_group.draw(screen)
        self.current_level.treasurebox_group.draw(screen)
        self.current_level.teddybear_group.draw(screen)
        self.current_level.barrel_group.draw(screen)
        
        self.player.draw()
        
        if self.current_level.level_num == 10:
            self.win_state()
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 512, 512, 150))
        self.player.draw_player_item()

        


#load level data
def load_levels():
    for i in range(1, 11):
        if path.exists(f'level{i}_data'):
            
            print(f'lvel{i} loaded')
            pickle_in = open(f'level{i}_data', 'rb')
            level = pickle.load(pickle_in)
            warp_points = pickle.load(pickle_in)
            bg_img = bg_list[pickle.load(pickle_in)]
            bgm = pickle.load(pickle_in)
            #bgm = pickle.load(pickle_in)
            
            level_list.append(Level(bg_img, level, warp_points, bgm, i))
            #main_game.current_level = Level(bg_img, level, warp_points)
            #main_game.player.pos = Vector2(x*tile_size + main_game.player.width/2 , y*tile_size + main_game.player.height/2)
        else:
            print("failed to load level")



load_levels()
#create main game instance 
main_game = Main()



#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit game 
            #close progam
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #key input
            #print(keys)
            if event.key == pygame.K_F10:
                debug = not debug
            if event.key == pygame.K_p:
                print(main_game.current_level.tile_list)
            if event.key == pygame.K_SPACE and not main_game.player.action:
                main_game.player.action = True
            if event.key == pygame.K_F5: # reload all game map
                playerlevel = level_list.index(main_game.current_level)
                level_list = []
                load_levels()
                main_game.current_level = level_list[playerlevel]
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and main_game.player.action:
                main_game.player.action = False
            
                

    clock.tick(30)
    #draw, update
    main_game.update()
    main_game.draw()
    main_game.debug()
    pygame.display.update()