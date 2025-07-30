import pygame
pygame.display.set_mode((10,10))

#load images


save_img = pygame.image.load('images/save_btn.png')
load_img = pygame.image.load('images/load_btn.png')

plank_tile = pygame.image.load('images/floor.png').convert()

#tile images
wall_top_img = pygame.image.load('images/wall_top.png').convert()
wall_right_top_img = pygame.image.load('images/wall_right-top.png').convert()
wall_right_img = pygame.image.load('images/wall_right.png').convert()
wall_right_bottom_img = pygame.image.load('images/wall_right-bottom.png').convert()
wall_bottom_img = pygame.image.load('images/wall_bottom.png').convert()
wall_left_bottom_img = pygame.image.load('images/wall_left-bottom.png').convert()
wall_left_img = pygame.image.load('images/wall_left.png').convert()
wall_left_top_img = pygame.image.load('images/wall_left-top.png').convert()
wall_right_top2_img = pygame.image.load('images/wall_right-top2.png').convert()
wall_right_bottom2_img = pygame.image.load('images/wall_right-bottom2.png').convert()
wall_left_bottom2_img = pygame.image.load('images/wall_left-bottom2.png').convert()
wall_left_top2_img = pygame.image.load('images/wall_left-top2.png').convert()

#wall_top_corner_right_img = pygame.image.load('images/wall_top_corner_right.png').convert()
#wall_top_corner_left_img = pygame.image.load('image/wall_top_corner_left.png').convert()
#wall_right_corner_top_img = pygame.image.load('images/wall_right_corner_top.png').convert()
#wall_right_corner_bottom_img = pygame.image.load('images/wall_right_corner_bottom.png').convert()
#wall_left_corner_top_img = pygame.image.load('images/wall_left_corner_top.png').convert()



wall_corner_righttop_img = pygame.image.load('images/wall_corner_righttop.png').convert()
wall_corner_rightbottom_img = pygame.image.load('images/wall_corner_rightbottom.png').convert()
wall_corner_leftbottom_img = pygame.image.load('images/wall_corner_leftbottom.png').convert()
wall_corner_lefttop_img = pygame.image.load('images/wall_corner_lefttop.png').convert()

wall_end_top_img = pygame.image.load('images/wall_end_top.png').convert()
wall_end_right_img = pygame.image.load('images/wall_end_right.png').convert()
wall_end_bottom_img = pygame.image.load('images/wall_end_bottom.png').convert()
wall_end_left_img = pygame.image.load('images/wall_end_left.png').convert()

wall_horizontal_img = pygame.image.load('images/wall_horizontal.png').convert()
wall_vertical_img = pygame.image.load('images/wall_vertical.png').convert()

wall_black_img = pygame.image.load('images/wall_black.png').convert()

door1_right_img = pygame.image.load('images/door1_right.png').convert()
door1_left_img = pygame.image.load('images/door1_left.png').convert()

stairs1_img = pygame.image.load('images/stairs1.png').convert()
stairs2_img = pygame.image.load('images/stairs2.png').convert()
stairs3_img = pygame.image.load('images/stairs3.png').convert()
stairs4_img = pygame.image.load('images/stairs4.png').convert()

#stone tiles 
stone_tile_img = pygame.image.load('images/stone_floor.png').convert()

stone_wall_top_img = pygame.image.load('images/stone_wall_top.png').convert()
stone_wall_right_top_img = pygame.image.load('images/stone_wall_right-top.png').convert_alpha()
stone_wall_right_img = pygame.image.load('images/stone_wall_right.png').convert()
stone_wall_right_bottom_img = pygame.image.load('images/stone_wall_right-bottom.png').convert_alpha()
stone_wall_bottom_img = pygame.image.load('images/stone_wall_bottom.png').convert()
stone_wall_left_bottom_img = pygame.image.load('images/stone_wall_left-bottom.png').convert_alpha()
stone_wall_left_img = pygame.image.load('images/stone_wall_left.png').convert()
stone_wall_left_top_img = pygame.image.load('images/stone_wall_left-top.png').convert_alpha()

stone_corner_leftbottom_img = pygame.image.load('images/stone_corner_leftbottom.png').convert()
stone_wall_corner_lefttop_img = pygame.image.load('images/stone_wall_corner_lefttop.png').convert()
stone_wall_corner_righttop_img = pygame.image.load('images/stone_wall_corner_righttop.png').convert()
stone_wall_corner_rightbottom_img = pygame.image.load('images/stone_wall_corner_rightbottom.png').convert()

stone_stairs1_img = pygame.image.load('images/stone_stairs1.png').convert()
stone_stairs2_img = pygame.image.load('images/stone_stairs2.png').convert_alpha()

spider_wave1_img = pygame.image.load('images/spider_wave1.png').convert_alpha()
spider_wave2_img = pygame.image.load('images/spider_wave2.png').convert_alpha()
spider_wave3_img = pygame.image.load('images/spider_wave3.png').convert_alpha()


wall_bottom_corner_left_img = pygame.image.load('images/wall_bottom_corner_left.png').convert()
wall_bottom_corner_right_img = pygame.image.load('images/wall_bottom_corner_right.png').convert()
wall_left_corner_bottom_img = pygame.image.load('images/wall_left_corner_bottom.png').convert()
wall_left_corner_top_img = pygame.image.load('images/wall_left_corner_top.png').convert()
wall_right_corner_bottom_img = pygame.image.load('images/wall_right_corner_bottom.png').convert()
wall_right_corner_top_img = pygame.image.load('images/wall_right_corner_top.png').convert()
wall_top_corner_left_img = pygame.image.load('images/wall_top_corner_left.png').convert()
wall_top_corner_right_img = pygame.image.load('images/wall_top_corner_right.png').convert()


wall_bottom_corner_img = pygame.image.load('images/wall_bottom_corner.png').convert()
wall_top_corner_img = pygame.image.load('images/wall_top_corner.png').convert()
wall_right_corner_img = pygame.image.load('images/wall_right_corner.png').convert()
wall_left_corner_img = pygame.image.load('images/wall_left_corner.png').convert()

right_corner_img = pygame.image.load('images/right_corner.png').convert()
top_corner_img = pygame.image.load('images/right_corner.png').convert()
bottom_corner_img = pygame.image.load('images/bottom_corner.png').convert()
left_corner_img = pygame.image.load('images/left_corner.png').convert()

treasurebox_brown1_img = pygame.image.load('images/treasurebox_brown1.png').convert_alpha()
treasurebox_blue1_img = pygame.image.load('images/treasurebox_blue1.png').convert_alpha()
treasurebox_green1_img = pygame.image.load('images/treasurebox_green1.png').convert_alpha()



door2_right_img = pygame.image.load('images/door2_right.png').convert()
door2_left_img = pygame.image.load('images/door2_left.png').convert()
door3_right_img = pygame.image.load('images/door3_right.png').convert()
door3_left_img = pygame.image.load('images/door3_left.png').convert()

floor_hole_img = pygame.image.load('images/floor_hole.png').convert()

grass_img = pygame.image.load('images/grass.png').convert()


#fence
fance_vertical_img = pygame.image.load('images/fance_vertical.png').convert_alpha()
fence_horizontal_img = pygame.image.load('images/fence_horizontal.png').convert_alpha()
fence_right_top_img = pygame.image.load('images/fence_right_top.png').convert_alpha()
fence_right_bottom_img = pygame.image.load('images/fence_right_bottom.png').convert_alpha()
fence_left_bottom_png = pygame.image.load('images/fence_left_bottom.png').convert_alpha()
fence_left_top_png = pygame.image.load('images/fence_left_top.png').convert_alpha()



cobblestone_img = pygame.image.load('images/cobblestone.png').convert()

#items 
key1_img = pygame.image.load('images/key1.png').convert_alpha()
key2_img = pygame.image.load('images/key2.png').convert_alpha()
key3_img = pygame.image.load('images/key3.png').convert_alpha()


#Character

bat_img = pygame.image.load('images/bat_down3.png').convert_alpha()
teddy_bear_img = pygame.image.load('images/teddy_bear1.png').convert_alpha()
butler_left1_img = pygame.image.load('images/butler_left1.png').convert_alpha()


barrel_img = pygame.image.load('images/barrel.png').convert_alpha()

axe_img = pygame.image.load('images/axe.png').convert_alpha()


#image list 
images = [
	wall_top_img,
	wall_right_top_img,
	wall_right_img,
	wall_right_bottom_img,
	wall_bottom_img,
	wall_left_bottom_img,
	wall_left_img,
	wall_left_top_img,
	wall_right_top2_img,
	wall_right_bottom2_img,
	wall_left_bottom2_img,
	wall_left_top2_img,
	wall_corner_righttop_img,
	wall_corner_rightbottom_img,
	wall_corner_leftbottom_img,
	wall_corner_lefttop_img,
	wall_end_top_img,
	wall_end_right_img,
	wall_end_bottom_img,
	wall_end_left_img,
	wall_horizontal_img,
	wall_vertical_img,
	wall_black_img,
	door1_right_img,
	door1_left_img,
	stairs1_img,
	stairs2_img,
	stairs3_img,
	stairs4_img,
 
	stone_tile_img,
	stone_wall_top_img,
	stone_wall_right_top_img,
	stone_wall_right_img,
	stone_wall_right_bottom_img,
	stone_wall_bottom_img,
	stone_wall_left_bottom_img,
	stone_wall_left_img,
	stone_wall_left_top_img,
	stone_corner_leftbottom_img,
	stone_wall_corner_lefttop_img,
	stone_wall_corner_righttop_img,
	stone_wall_corner_rightbottom_img,
	stone_stairs1_img,
	stone_stairs2_img,

	key1_img,

	wall_bottom_corner_left_img,
	wall_bottom_corner_right_img,
	wall_left_corner_bottom_img,
	wall_left_corner_top_img,
	wall_right_corner_bottom_img,
	wall_right_corner_top_img,
	wall_top_corner_left_img,
	wall_top_corner_right_img,

	spider_wave1_img,
	spider_wave2_img,
	spider_wave3_img,

	wall_bottom_corner_img,
	wall_top_corner_img,
	wall_right_corner_img,
	wall_left_corner_img,

	right_corner_img,
	top_corner_img,
	bottom_corner_img,
	left_corner_img,

	bat_img,

	treasurebox_brown1_img,
	treasurebox_blue1_img,
	treasurebox_green1_img,
 
 	teddy_bear_img,

	door2_right_img,
	door2_left_img,
	door3_right_img,
	door3_left_img,
	
	key2_img,
	key3_img,
 
	floor_hole_img,
 
 	#butler_left1_img,
  
 	barrel_img,
  
	fance_vertical_img,
	fence_horizontal_img,
	fence_right_top_img,
	fence_right_bottom_img,
	fence_left_bottom_png,
	fence_left_top_png,
 
	
 
	cobblestone_img
	

]

bg_list = [
	plank_tile,
	stone_tile_img,
 	grass_img
]
