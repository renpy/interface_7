init -1 python in gui:

    def scale(n):
        return int(n)

init 100 python in gui:

    if not renpy.mobile:
        from store import config
        from generate_images import ImageGenerator

        ImageGenerator(config.gamedir + "/gui/", config.screen_width, config.screen_height, ACCENT_COLOR, overwrite=True).generate_all()
