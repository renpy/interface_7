init -100 python in gui:

    def scale(n):
        return int(n)

init 100 python in gui:

    if not renpy.mobile:
        from store import config

        import sys
        import os
        sys.path.insert(0, os.path.join(config.renpy_base, "launcher", "game"))

        from gui7.parameters import GuiParameters
        from gui7.images import ImageGenerator
        from gui7 import generate_gui

        p = GuiParameters(
            config.gamedir, config.gamedir,
            config.screen_width, config.screen_height,
            ACCENT_COLOR, "#000000", False, None,
            True, False, False)
        generate_gui(p)
