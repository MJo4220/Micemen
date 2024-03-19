import pygame.sprite


class Mice:
    def __init__(self, id, ycord, xcord, status, team):
        self.id = id
        self.xcord = xcord
        self.ycord = ycord
        self.status = status
        self.team = team
        

class Button:
    def __init__(self,  up_down, column, active, pressed):
        self.up_down = up_down
        self.column = column
        self.active = active
        self.pressed = pressed


class Micesprite(pygame.sprite.Sprite):
    def __init__(self, png, x, y):
        super().__init__()
        self.png = png
        self.x = x
        self.y = y
        self.rect = self.png.get_rect()
        self.rect.center = (x, y)

    def move(self, direction):
        if direction == "down":
                self.rect.move_ip(0, 25)
                self.y = self.y + 25
        elif direction == "left":
                self.rect.move_ip(10, 0)
                self.x = self.x +10
        elif direction == "right":
                self.rect.move_ip(-10, 0)
                self.x = self.x -10

    def draw(self, surface):
        surface.blit(self.png, self.rect)