import pygame
import pymunk
import pymunk.pygame_util
import math

# Constants
WIDTH, HEIGHT = 1000, 800
COLOR_RED = (255, 0, 0, 100)

# Setup
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
draw_options = pymunk.pygame_util.DrawOptions(window)


def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()


def create_boundaries(space, width, height):
    rects = [
        [(width/2, height-10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width-10, height/2), (20, height)]
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)


def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (WIDTH/2, HEIGHT/2)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = COLOR_RED
    shape.elasticity = 0.9
    shape.friction = 0.4
    space.add(body, shape)

    return shape


def main(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    # Delta Time, 1/60 of a second, the time period we want the 'space' to update
    dt = 1 / fps

    space = pymunk.Space()
    space.gravity = (0, 981)

    ball = create_ball(space, 30, 10)
    create_boundaries(space, width, height)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.body.apply_impulse_at_local_point((10000, 0), (0, 0))

        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps )
    
    pygame.quit()


if __name__ == "__main__":
    main(window, WIDTH, HEIGHT)
