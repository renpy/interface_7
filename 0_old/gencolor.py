#@PydevCodeAnalysisIgnore
from __future__ import print_function

import colorsys
import argparse

class Color(object):

    @staticmethod
    def from_hexcode(hexcode):

        hexcode = hexcode.lstrip('#')

        r = int(hexcode[0:2], 16) / 255.0
        g = int(hexcode[2:4], 16) / 255.0
        b = int(hexcode[4:6], 16) / 255.0

        rv = Color()
        rv.h, rv.l, rv.s = colorsys.rgb_to_hls(r, g, b)

        return rv

    def multiply(self, l=1.0, s=1.0):

        rv = Color()
        rv.h = self.h
        rv.l = self.l * l
        rv.s = self.s * s

        return rv

    def __str__(self):
        r, g, b = colorsys.hls_to_rgb(
            self.h,
            self.l,
            self.s)

        return "#{:02x}{:02x}{:02x}".format(
            int(255 * r),
            int(255 * g),
            int(255 * b),
            )


c = Color.from_hexcode("#00b8c3")
print(c.h, c.l, c.s)
print("Original", c)
print("Hover", c.multiply(l=1.1))
print("Muted", c.multiply(l=0.3))
print("Hover Muted", c.multiply(l=0.4))


