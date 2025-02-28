# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# define sprite
class sprite:
    speed = 300
    
    def __init__(self, location, size, colour):
        self.location = location
        self.size = size
        self.colour = colour

    def draw_sprite(self):
        pygame.draw.rect(screen, "blue", pygame.Rect(self.location.x, self.location.y, self.size, self.size))

    def move_sprite(self, direction, dt):
        if direction == "up":
            self.location.y -= self.speed * dt
        if direction == "down":
            self.location.y += self.speed * dt
        if direction == "left":
            self.location.x -= self.speed * dt
        if direction == "right":
            self.location.x += self.speed * dt

# make a sprite
sprite1 = sprite(pygame.Vector2(screen.get_width() * 0.5, screen.get_height() * 0.5), 40, "blue")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        sprite1.move_sprite("up", dt)
    if keys[pygame.K_s]:
        sprite1.move_sprite("down", dt)
    if keys[pygame.K_a]:
        sprite1.move_sprite("left", dt)
    if keys[pygame.K_d]:
        sprite1.move_sprite("right", dt)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    sprite1.draw_sprite()
    
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()