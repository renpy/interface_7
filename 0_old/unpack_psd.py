from __future__ import unicode_literals, division, absolute_import, print_function

from psd_tools import PSDImage, Group, Layer
import argparse
import os

def walk_layers(prefix, l):

    # print(type(l))

    if isinstance(l, (Group, PSDImage)):

        for i, ll in enumerate(l.layers):

            if len(l.layers) == 1:
                ll_prefix = prefix + "_"
            else:
                n = ll.name
                n = n.replace("copy ", "")
                n = n.replace(" ", "")
                n = n.replace("Shape", "")
                n = n[:18]

                ll_prefix = prefix + n + "_"

            walk_layers(ll_prefix, ll)

    elif isinstance(l, Layer):
        prefix += "{},{}".format(l.bbox.x1, l.bbox.y1)

    print(prefix, l)

    if prefix[-1] == "/":
        prefix += "_"

    img = l.as_PIL()
    img.save(prefix + ".png")



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("filename")
    args = ap.parse_args()

    psd = PSDImage.load(args.filename)

    print(type(psd.layers))

    walk_layers(os.path.splitext(args.filename)[0] + "/", psd)


if __name__ == "__main__":
    main()
