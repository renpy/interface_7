#!/usr/bin/env python

import pygame_sdl2

from renpy.store import Color

# The target widths used in templates.
WIDTH = 1280
HEIGHT = 720

class ImageGenerator(object):

    def __init__(self, prefix, width, height, color):
        pygame_sdl2.image.init()

        self.prefix = prefix

        self.width = width
        self.height = height

        self.scale = 1.0 * height / HEIGHT

        self.accent_color = Color(color)
        self.boring_color = Color("#000000")

        self.hover_color = self.accent_color.tint(.6)
        self.muted_color = self.accent_color.shade(.4)
        self.hover_muted_color = self.accent_color.shade(.6)

    def scale_int(self, n):
        rv = int(n * self.scale)

        if rv < 1:
            rv = 1

        return rv

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

    def save(self, s, filename):
        pygame_sdl2.image.save(s, self.prefix + filename + ".png")

    def make_surface(self, width, height):
        return pygame_sdl2.Surface((width, height), pygame_sdl2.SRCALPHA)

    def generate_image(self, filename, xtmpl, ytmpl, color=(0, 0, 0, 255)):

        r, g, b, a = color

        xtmpl = self.rescale_template(xtmpl)
        ytmpl = self.rescale_template(ytmpl)

        xline = self.generate_line(xtmpl)
        yline = self.generate_line(ytmpl)

        xline = self.crop_line(xline, self.width)
        yline = self.crop_line(yline, self.height)

        s = self.make_surface(len(xline), len(yline))

        for x, xv in enumerate(xline):
            for y, yv in enumerate(yline):
                v = xv * yv
                s.set_at((x, y), (r, g, b, int(a * v)))

        self.save(s, filename)

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

    def generate_nvl(self):
        XSIZE = WIDTH
        XINSIDE = (XSIZE - 800) // 2

        YSIZE = HEIGHT

        X = [
            (0, 0.0),
            (XINSIDE, 1.0),
            (XSIZE - XINSIDE, 1.0),
            (XSIZE, 0.0),
            ]

        Y = [
            (0, 1.0),
            (YSIZE, 1.0),
            ]


        self.generate_image("nvl", X, Y, self.boring_color.opacity(.8))
        self.generate_image("history", X, Y, self.boring_color.opacity(.8))



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

    def generate_darken(self):

        width = self.scale_int(280)
        line_width = self.scale_int(3)

        # Main menu.
        mm = self.make_surface(width, self.height)
        mm.fill(self.boring_color.opacity(.8))
        mm.subsurface((width - line_width, 0, line_width, self.height)).fill(self.accent_color)
        self.save(mm, "main_menu_darken")


        gm = self.make_surface(self.width, self.height)
        gm.fill(self.boring_color.opacity(.8))
        self.save(gm, "game_menu_darken")

        gm = self.make_surface(self.width, self.height)
        gm.fill(self.boring_color.opacity(.6))
        self.save(gm, "confirm_darken")

    def generate_separator(self):

        vwidth = self.scale_int(3)
        vheight = self.scale_int(570)

        v = self.make_surface(vwidth, vheight)
        v.fill(self.accent_color)
        self.save(v, "vertical_separator")

    def generate_file_slot(self):

        width = self.scale_int(276)
        height = self.scale_int(216)

        bar_width = self.scale_int(6)
        shot_width = self.scale_int(256)
        shot_offset = self.scale_int(10)

        top_y = self.scale_int(10)
        top_height = self.scale_int(144)

        s = self.make_surface(width, height)
        # s.subsurface((0, top_y, bar_width, top_height)).fill(self.accent_color)
        s.subsurface((shot_offset, top_y, shot_width, top_height)).fill(self.accent_color.shade(.33))
        self.save(s, "idle_file_slot")

        s = self.make_surface(width, height)
        s.subsurface((0, top_y, bar_width, top_height)).fill(self.accent_color)
        s.subsurface((shot_offset, top_y, shot_width, top_height)).fill(self.accent_color.shade(.5))
        self.save(s, "hover_file_slot")


    def generate_confirm_background(self):
        width = self.scale_int(600)
        height = self.scale_int(250)

        border = self.scale_int(3)

        s = self.make_surface(width, height)
        s.fill(self.accent_color)
        s.subsurface((border, border, width - 2 * border, height - 2 * border)).fill(self.boring_color)
        self.save(s, "confirm_background")

    def generate_bars(self):

        def fill(name, color, width, height, vname=None):
            width = self.scale_int(width)
            height = self.scale_int(height)

            s = self.make_surface(width, height)
            s.fill(color)
            self.save(s, name)

            if vname is None:
                vname = "v" + name

            s = self.make_surface(height, width)
            s.fill(color)
            self.save(s, vname)

        fill("bar_left", self.accent_color, 350, 30, "bar_bottom")
        fill("bar_right", self.muted_color, 350, 30, "bar_top")

        fill("slider", self.muted_color, 350, 30)
        fill("slider_hover", self.hover_muted_color, 350, 30)
        fill("slider_thumb", self.accent_color, 10, 30)
        fill("slider_hover_thumb", self.hover_color, 10, 30)

        fill("scrollbar", self.muted_color, 350, 10)
        fill("scrollbar_hover", self.hover_muted_color, 350, 10)
        fill("scrollbar_thumb", self.accent_color, 350, 10)
        fill("scrollbar_hover_thumb", self.hover_color, 350, 10)

    def generate_buttons(self):

        padding = self.scale_int(2)

        def fill(name, width, height, color=None, fill_width=None):
            width = self.scale_int(width) + padding * 2
            height = self.scale_int(height) + padding * 2

            s = self.make_surface(width, height)

            if fill_width:
                fill_width = self.scale_int(fill_width)
                ss = s.subsurface((padding, padding, fill_width, height - padding * 2))
            else:
                ss = s

            if color is not None:
                ss.fill(color)

            self.save(s, name)

        fill("button", 250, 40)
        fill("button_hover", 250, 40)

        fill("button_checked", 250, 40, self.accent_color, fill_width=5)
        fill("button_unchecked", 250, 40)

        fill("medium_button", 30, 40)
        fill("medium_button_hover", 30, 40)

        fill("small_button", 30, 40)
        fill("small_button_hover", 30, 40)


    def generate_skip(self):
        XSIZE = 240
        XRIGHT = 50

        YSIZE = 43

        X = [
            (0, 1.0),
            (XSIZE - XRIGHT, 1.0),
            (XSIZE, 0.0),
            ]

        Y = [
            (0, 1.0),
            (YSIZE, 1.0),
            ]

        self.generate_image("skip_indicator", X, Y, self.boring_color.opacity(.8))

    def generate_notify(self):
        XSIZE = 922
        XRIGHT = 50

        YSIZE = 43

        X = [
            (0, 1.0),
            (XSIZE - XRIGHT, 1.0),
            (XSIZE, 0.0),
            ]

        Y = [
            (0, 1.0),
            (YSIZE, 1.0),
            ]

        self.generate_image("notify", X, Y, self.boring_color.opacity(.8))

    def generate_all(self):
        self.generate_textbox()
        self.generate_choice_button()
        self.generate_darken()
        self.generate_separator()
        self.generate_file_slot()
        self.generate_confirm_background()
        self.generate_nvl()
        self.generate_bars()
        self.generate_buttons()
        self.generate_skip()
        self.generate_notify()

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()

    ap.add_argument("prefix")
    ap.add_argument("width", type=int)
    ap.add_argument("height", type=int)

    args = ap.parse_args()

    ImageGenerator(args.prefix, args.width, args.height).generate_all()


