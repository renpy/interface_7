#!/usr/bin/env python

import math
import random

WIDTH = 1280
XINSIDE = (WIDTH - 744) // 2
XOUTSIDE = 0 # XINSIDE - 20

HEIGHT = 185
YBORDER = 5

XMA = .0

X = [
    (0, XMA),
    (XOUTSIDE, XMA),
    (XINSIDE, .8),
    (WIDTH - XINSIDE, .8),
    (WIDTH - XOUTSIDE, XMA),
    (WIDTH, XMA),
    ]

Y = [
    (0, 0.0),
    (YBORDER, 1.0),
    (HEIGHT, 1.0),
    ]

def generate_line(template, size):
    rv = [ ]

    right_pos, right_value = template[0]

    for i in range(size):

        if i == right_pos:
            rv.append(right_value)
            continue

        while i >= right_pos:
            left_pos = right_pos
            left_value = right_value

            right_pos, right_value = template.pop(0)

        done = 1.0 * (i - left_pos) / (right_pos - left_pos)
        rv.append(left_value + done * (right_value - left_value))


    return rv

xdata = generate_line(X, WIDTH)
ydata = generate_line(Y, HEIGHT)

import pygame_sdl2

pygame_sdl2.init()
s = pygame_sdl2.Surface((WIDTH, HEIGHT), pygame_sdl2.SRCALPHA)

for x, xv in enumerate(xdata):
    for y, yv in enumerate(ydata):
        # r = random.uniform(.95, 1.0)
        v = xv * yv
        s.set_at((x, y), (0, 0, 0, int(255 * v)))

pygame_sdl2.image.save(s, "game/images/tb2.png")

