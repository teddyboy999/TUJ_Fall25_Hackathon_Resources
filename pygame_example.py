import pygame

# Initialize Game
pygame.init()
## Game Window Title
pygame.display.set_caption("Test Game")

# Global Variables
run: bool = True

## Game Window Dimensions
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

## Create Player
player = pygame.Rect((300, 250, 50, 50))

if __name__ == "__main__":
    # 1. Create Game Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # 2. Create Game Loop -- So that the game/window keeps running
    while (run):
        # Refresh the Screen - Color it black
        ## We need to do this so previous objects don't keep showing up.
        screen.fill((0, 0, 0))

        # 2.1. Draw Elements
        ## Draw Player
        pygame.draw.rect(screen, (250, 0, 0), player)

        # Define Controls
        key = pygame.key.get_pressed()
        if (key[pygame.K_a] == True):
            player.move_ip(-1, 0) 
            # move_ip(x, y) == move in place 
            # (-x, 0) == Move left, don't affect y coordinate
        elif (key[pygame.K_d] == True):
            player.move_ip(1,0)
        elif (key[pygame.K_w] == True):
            player.move_ip(0,-1)
        elif (key[pygame.K_s] == True):
            player.move_ip(0,1)
        else:
            pass

        # 3. EventHandler
        ## Event Handler listens for events - keypresses, mouseclicks, etc.
        ## Iterate through the EventHandler
        for event in pygame.event.get():
            # Check for "quit" event ("Escape Button pressed" == Quit the Game)
            if event.type == pygame.QUIT:
                run = False

        # Update Screen to draw elements/update game state -- ideally should happen every frame
        pygame.display.update()
    
    # Quit Window
    pygame.quit()

