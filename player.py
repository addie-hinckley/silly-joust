import pygame

class Player(pygame.sprite.Sprite):

    move_right = False
    move_left = False
    movement_speed = 3


    def __init__(self, player_number, surface: pygame.Surface, location: tuple, lives: int):
        super().__init__()
        self.player_number = player_number
        self.image = surface
        self.rect = surface.get_rect(topleft = location)
        self.lives = 3
        speed = 3
        self.jump_speed = 3
        self.location = location

        self.gravity = .25
        self.y_velocity = -5
        self.terminal_velocity = 5


        self.is_moving_right = False
        self.is_moving_left = False


    def __str__(self):
        return f"player lives: {self.lives} XY: {self.rect.x, self.rect.y} SPEED: {self.get_movement_speed}"
    
    def apply_gravity(self):
        self.y_velocity += self.gravity
        self.rect.y += int(self.y_velocity)
        if self.y_velocity >= self.terminal_velocity:
            self.y_velocity = self.terminal_velocity
        
        # finish this the jumping doesnt work well
    



    def lose_life(self):
        self_lives -= 1
        return f"player lives: {self.lives}"
    
    def get_movement_speed(self):  
        return self.movement_speed


    def move_right(self):
        self.rect.x += self.get_movement_speed()

    def move_left(self):
        self.rect.x -= self.get_movement_speed()
    
    def player_jump(self):
        self.y_velocity = -6

        



    

