import pygame_sdl2
import os
import math

pygame_sdl2.import_as_pygame()

import pygame

SIZE = 40


def process(fn):
    s = pygame.image.load(fn)

    w, h = s.get_size()
    for y in range(h):
        for x in range(w):
            a = s.get_at((x, y))[3]
            s.set_at((x, y), (255, 255, 255, a))


    s2 = pygame.Surface((SIZE, SIZE), pygame.SRCALPHA)

    xo = (SIZE - w) / 2
    yo = math.ceil((SIZE - h) / 2.0)

    s2.blit(s, (xo, yo))

    pygame.image.save(s2, "out/" + fn)



def main():
    for i in os.listdir("."):
        if not i.endswith(".png"):
            continue

        print i

        process(i)

if __name__ == "__main__":
    main()
