#!/usr/bin/env python
import pygame as py

from images import BACKGROUND_IMAGE
from alpha import Ninja, Zombie
from constants import DISPLAY_SIZE, GAME_TITLE, CLOCK_TICK

py.init()

win = py.display.set_mode(DISPLAY_SIZE, py.FULLSCREEN)
py.display.set_caption(GAME_TITLE)

player = Ninja()
enemy = Zombie()

clock = py.time.Clock()

# Add Sounds


def redraw_window():

    win.blit(BACKGROUND_IMAGE, (0, 0))

    player.draw(win)
    enemy.draw(win, player_pos=player.x)

    py.display.update()


def main():
    font = py.font.SysFont('comicsans', 30, True)
    run = True

    while run:
        clock.tick(CLOCK_TICK)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()

        if keys[py.K_ESCAPE]:
            run = False

        if keys[py.K_1]:
            enemy.current_state = 'WALK'

        if keys[py.K_2]:
            enemy.current_state = 'DEAD'

        if keys[py.K_3]:
            enemy.current_state = 'ATTACK'

        if keys[py.K_4]:
            enemy.current_state = 'IDLE'

        if keys[py.K_5]:
            player.current_state = 'CLIMB'

        if keys[py.K_6]:
            player.current_state = 'DEAD'

        if keys[py.K_7]:
            player.current_state = 'GLIDE'

        if keys[py.K_8]:
            player.current_state = 'JUMPATTACK'

        if keys[py.K_9]:
            player.current_state = 'JUMPTHROW'

        if keys[py.K_0]:
            player.current_state = 'SLIDE'

        if keys[py.K_TAB]:
            if player.is_jumping:
                player.current_state = 'JUMPTHROW'

            else:
                player.current_state = 'THROW'

        if keys[py.K_UP] or player.is_jumping:
            player.jump()

        if (keys[py.K_RIGHT] or keys[py.K_LEFT]) and not player.is_attacking:
            if keys[py.K_RIGHT]:
                player.direction = 'RIGHT'

            if keys[py.K_LEFT]:
                player.direction = 'LEFT'

            if not player.is_jumping:
                player.current_state = 'RUN'

            player.move()

        if not any(keys) and not player.is_jumping and not player.is_attacking:
            player.current_state = 'IDLE'

        if keys[py.K_SPACE] and not player.is_jumping:
            player.is_attacking = True
            player.current_state = 'ATTACK'

        redraw_window()


if __name__ == '__main__':
    main()
