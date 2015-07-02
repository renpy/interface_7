# This file is in the public domain. Feel free to modify it as a basis
# for your own interface.

################################################################################
# Sizes
#
# These will need to be changed if you change the size of the game. Remember
# to click "Window" in preferences to ensure the window itself is resized.

# The width and height of the screen.
init python:
    config.screen_width = 1280
    config.screen_height = 720

# The size of text in text buttons.
define BUTTON_SIZE = 25

# The width of the panes.
define PANE_WIDTH = 280


################################################################################
# Colors
#
# The colors of various aspects of the interface.

# An accent color used throughout the interface.
define ACCENT_COLOR = "#00b8c3"

# The color used for a text button while it is focused.
define HOVER_COLOR = ACCENT_COLOR

# The color used for a text button when it is selected but not focused.
# A button is selected if it is the current screen or preference value
define SELECTED_COLOR = "#ffffff"

# The color used for a text button when it is neither selected nor hovered.
define IDLE_COLOR = "#555555"

# The color used for a text button when it cannot be selected.
define INSENSITIVE_COLOR = "#55555580"


################################################################################
# Window, Frame, Pane, and Menu backgrounds

# The background of the main menu.
define MAIN_MENU_BACKGROUND = "images/main menu.jpg"

# The background of the game menu.
define GAME_MENU_BACKGROUND = "image/game menu.jpg"

# The background of the window containing dialogue from characters.
define WINDOW_BACKGROUND = "#000000cc"

# The background of user interface frames.
define FRAME_BACKGROUND = "#000000cc"

# A right-aligned vertical line of the ACCENT_COLOR that may bee used by PANE_BACKGROUND.
define ACCENT_LINE = Solid(ACCENT_COLOR, xmaximum=4, xalign=1.0)

# The background of an interface pane. Interface panes are frames that are used
# for the main menu, game menu navigation, and file pane selection.
define PANE_BACKGROUND = Fixed(FRAME_BACKGROUND, ACCENT_LINE)


################################################################################
# Style common user interface components.

style button_text:
    size BUTTON_SIZE
    color IDLE_COLOR
    insensitive_color INSENSITIVE_COLOR
    selected_color SELECTED_COLOR
    hover_color HOVER_COLOR


################################################################################
# Menu Background
#
# This screen is used to supply the background to the main and game menus.

screen menu_background():

    if main_menu:
        add MAIN_MENU_BACKGROUND
    else:
        add GAME_MENU_BACKGROUND


################################################################################
# Navigation Pane
#
# This is the pane that makes up the left side of the screen in main and game
# menus, providing a text buttons that are used to navigate through those menus.

screen navigation_pane():

    frame:
        style_group "nav"
        background PANE_BACKGROUND
        xsize PANE_WIDTH
        yfill True

        has vbox:
            spacing BUTTON_SIZE // 2
            yalign 0.5

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Main Menu") action MainMenu()

        if main_menu:
            textbutton _("Extras") action ShowMenu("extras")

        textbutton _("Help") action Help()

        textbutton _("About") action ShowMenu("about")

        textbutton _("Quit") action Quit(confirm=not main_menu)


style nav_button is button:
    xfill True
    xpadding 40


##############################################################################
# Main Menu
#
# Used to display the main menu when Ren'Py starts.
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu. This can be changed to be an image by
    # commenting out the next line and uncommenting the following line.
    # add "#000"
    add "main menu"
    # add Transform("main_menu.png", size=(1280, 720))

    use menu_background

    hbox:
        use navigation_pane
