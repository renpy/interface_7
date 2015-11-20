#!/usr/bin/env python

import math
import random

from renpy.store import Color

# The target widths used in templates.
WIDTH = 1280
HEIGHT = 720

class ImageGenerator(object):

    def __init__(self, prefix, width, height):
        import pygame_sdl2
        pygame_sdl2.image.init()

        self.prefix = prefix

        self.width = width
        self.height = height

        self.scale = 1.0 * height / HEIGHT

        self.accent_color = Color("#00b8c3")
        self.boring_color = Color("#000000")

    def rescale_template(self, t):

        rv = [ ]

        for pos, opacity in t:
            rv.append((pos * self.scale, opacity))

        return rv

    def generate_line(self, template):

        size = int(max(i[0] for i in template))

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

    def crop_line(self, line, size):
        """
        Crops the center `size` pixels out of `line`.
        """

        if len(line) <= size:
            return line

        start = (len(line) - size) // 2

        return line[start:start + size ]

    def generate_image(self, filename, xtmpl, ytmpl, color=(0, 0, 0, 255)):

        r, g, b, a = color

        xtmpl = self.rescale_template(xtmpl)
        ytmpl = self.rescale_template(ytmpl)

        xline = self.generate_line(xtmpl)
        yline = self.generate_line(ytmpl)

        xline = self.crop_line(xline, self.width)
        yline = self.crop_line(yline, self.height)

        import pygame_sdl2
        s = pygame_sdl2.Surface((len(xline), len(yline)), pygame_sdl2.SRCALPHA)

        for x, xv in enumerate(xline):
            for y, yv in enumerate(yline):
                v = xv * yv
                s.set_at((x, y), (r, g, b, int(a * v)))

        pygame_sdl2.image.save(s, self.prefix + filename + ".png")

    def generate_textbox(self):

        XSIZE = WIDTH
        XINSIDE = (XSIZE - 744) // 2

        YSIZE = 185
        YBORDER = 5

        X = [
            (0, 0.0),
            (XINSIDE, 1.0),
            (XSIZE - XINSIDE, 1.0),
            (XSIZE, 0.0),
            ]

        Y = [
            (0, 0.0),
            (YBORDER, 1.0),
            (YSIZE, 1.0),
            ]

        self.generate_image("textbox", X, Y, self.boring_color.opacity(.8))

    def generate_choice_button(self):
        XSIZE = 790
        XINSIDE = 100

        YSIZE = 30
        YBORDER = 3

        X = [
            (0, 0.0),
            (XINSIDE, 1.0),
            (XSIZE - XINSIDE, 1.0),
            (XSIZE, 0.0),
            ]

        Y = [
            (0, 0.0),
            (YBORDER, 1.0),
            (YSIZE - YBORDER, 1.0),
            (YSIZE, 0.0),
            ]

        self.generate_image("choice_button", X, Y, self.boring_color.opacity(.8))
        self.generate_image("hover_choice_button", X, Y, self.accent_color.opacity(.95))


    def generate_all(self):
        self.generate_textbox()
        self.generate_choice_button()


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()

    ap.add_argument("prefix")
    ap.add_argument("width", type=int)
    ap.add_argument("height", type=int)

    args = ap.parse_args()

    ImageGenerator(args.prefix, args.width, args.height).generate_all()


