import json
import Tkinter as tk
import tkMessageBox

GAMES = {
    "SNAKE": "./snakearbol.ast",
    "TETRIS": "./tetrisarbol.ast",
}
#import pygame

class Juego():
    def __init__(self, data):
        self.data = data
        self.game = self.data["name"]
        self.width = self.data.get("board_size", [10, 20])[0]       
        self.height = self.data.get("board_size", [10, 20])[1]
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height) ]
        self.points = 0
        self.game_over = False

        # GUI config
        self.root = tk.Tk()
        self.root.geometry("320x150")
        self.root.title("BrickScript")
        
        # 25 pixels per cell
        self.cell_size = 25
        self.canvas_width
        self.canvas_height

        ''' Events '''
        
    def run(self):
        self.root.mainloop()

    def testrun(self):
        print self.data




# def widthdraw_root(game):
#     if root.state() == 'normal':
#         root.state('withdrawn')
#         print "Root has been withdrawn"
#         gameFile = GAMES[game]
#         print "Gamefile is: " + gameFile
#     else:
#         root.state('normal')
#         print "Root is back to normal"


if __name__ == "__main__":
    # Game data
    with open("./tetrisarbol.ast") as f:
        game_data = json.load(f)

    game = Juego(game_data)
    game.testrun()

    print "Hello, world!"


'''
class movable_object(): 
    def __init__(self, xpos, ypos, width, height, color):
        # Initial xy coordinate position
        self.x = xpos
        self.y = ypos

        # Width and height
        self.width = width 
        self.height = height
        # Color
        self.color = color
    
# Initialize pygame
pygame.init()

# Creates a screen to display on
screen = pygame.display.set_mode((640, 480))
s_width = screen.get_width()
s_height = screen.get_height()

# Movable brick
brick = movable_object(s_width/2, s_height/2, 20, 10, color="red")
speed = 3.5
#print "Initial position x: {} ".format(brick.x)
#print "Initial position y: {} ".format(brick.y)

# Main game clock
clock = pygame.time.Clock()
running = True

# Delta time
dt = 0

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, brick.color, (brick.x, brick.y, brick.width, brick.height))

    # Controls movement of object
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: 
        brick.y -= speed 
    if keys[pygame.K_DOWN]: 
        brick.y += speed
    if keys[pygame.K_LEFT]: 
        brick.x -= speed
    if keys[pygame.K_RIGHT]: 
        brick.x += speed
    
    if brick.x <= 0:
        brick.x = 0
    if brick.x >= s_width - brick.width:
        brick.x = s_width - brick.width
    if brick.y <= 0:
        brick.y = 0
    if brick.y >= s_height - brick.height:
        brick.y = s_height - brick.height

    #print "Changing position x: {}".format(brick.x)
    #print "Changing position y: {}".format(brick.y)
    
    
    # Puts work on screen
    pygame.display.flip()

    # Limit to 60fps
    dt = clock.tick(60) / 1000

pygame.quit()
'''
