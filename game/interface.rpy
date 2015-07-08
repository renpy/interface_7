﻿# This file is in the public domain. Feel free to modify it as a basis
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

# The size of text in text buttons and labels.
define HUGE_SIZE = 50
define LARGE_SIZE = 24
define NORMAL_SIZE = 22

# Scale factor for various sizes.
define SCALE = 10

################################################################################
# Colors
#
# The colors of various aspects of the interface.

# An accent color used throughout the interface.
define ACCENT_COLOR = "#00b8c3"
define HOVER_COLOR = "#00cad6"
define MUTED_COLOR = "#00373a"
define HOVER_MUTED_COLOR = "#00494e"

# The color used for a text button when it is selected but not focused.
# A button is selected if it is the current screen or preference value
define SELECTED_COLOR = "#ffffff"

# The color used for a text button when it is neither selected nor hovered.
define IDLE_COLOR = "#555555"

# The color used for a text button when it cannot be selected.
define INSENSITIVE_COLOR = "#55555580"


################################################################################
# Window, Frame, Pane, and Menu backgrounds

# The background of the main menu and game menu.
define MAIN_MENU_BACKGROUND = "images/main menu.jpg"
define GAME_MENU_BACKGROUND = "images/game menu.jpg"

# Solid colors that are overlaid on those backgrounds to darken or lighten
# them.
define MAIN_MENU_DARKEN = "#000000cc"
define GAME_MENU_DARKEN = "#000000cc"

# The background of the window containing dialogue from characters.
define WINDOW_BACKGROUND = "#000000cc"

# Vertical lines made up of the accent color.
define NARROW_LINE = Solid(ACCENT_COLOR, xsize=SCALE // 3)
define WIDE_LINE = Solid(ACCENT_COLOR, xsize=SCALE // 2)

################################################################################
# Style common user interface components.

style button_text:
    size NORMAL_SIZE
    color IDLE_COLOR
    insensitive_color INSENSITIVE_COLOR
    selected_color SELECTED_COLOR
    hover_color HOVER_COLOR
    selected_hover_color HOVER_COLOR

style label:
    ysize 3 * SCALE

style label_text:
    size LARGE_SIZE
    color ACCENT_COLOR
    yalign 1.0

style interface_frame is default

style bar:
    ysize 3 * SCALE
    left_bar Solid(ACCENT_COLOR)
    right_bar Solid(MUTED_COLOR)
    hover_left_bar Solid(HOVER_COLOR)
    hover_right_bar Solid(HOVER_MUTED_COLOR)

style slider is bar

################################################################################
# Derived constants.
define PANE_WIDTH = 28 * SCALE

################################################################################
# Navigation
#
# This screen is not called directly, but included via the use statement. It
# provides the buttons on the left side of the screen, which make up the main
# menu and game menu navigation.

screen navigation():

    vbox:
        style_group "nav"

        xpos 5 * SCALE
        xmaximum PANE_WIDTH - 5 * SCALE

        yalign 0.5
        spacing LARGE_SIZE // 2


        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Extras") action ShowMenu("extras")
        else:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        textbutton _("Help") action Help()

        textbutton _("Quit") action Quit(confirm=not main_menu)


style nav_button_text:
    size LARGE_SIZE


##############################################################################
# Main Menu
#
# Used to display the main menu when Ren'Py starts.
# http://www.renpy.org/doc/html/screen_special.html#main-menu
#
# This lays out the main menu and its backgrounds, but uses the navigation
# screen to actually supply the main menu buttons.

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    add MAIN_MENU_BACKGROUND

    hbox:
        style_group "interface"

        frame:
            background MAIN_MENU_DARKEN
            xsize PANE_WIDTH
            yfill True

        add NARROW_LINE

    use navigation


##############################################################################
# Game Menu
#
# This lays out the basic common structure of a game menu screen. It's called
# with the screen title, and displays the background, title, and navigation.
# When used with children (the expected case), it transcludes those children
# in an hbox after the space reserved for navigation.

screen game_menu(title):

    # Add the backgrounds.
    add GAME_MENU_BACKGROUND
    add GAME_MENU_DARKEN

    vbox:
        style_group "interface"

        label title:
            # position the title.
            xpos 5 * SCALE
            ysize 12 * SCALE

            # text_ properties are used to style the text.
            text_size HUGE_SIZE
            text_color ACCENT_COLOR
            text_yalign 0.5

        frame:
            style "interface_frame"

            bottom_margin 3 * SCALE

            hbox:

                # Reserve space for the navigation section.
                null width PANE_WIDTH
                add NARROW_LINE

                transclude

    use navigation

    textbutton _("Return"):
        style "nav_button"
        action Return()
        xpos 5 * SCALE
        ypos config.screen_height - 3 * SCALE
        yanchor 1.0


screen save:

    tag menu

    use game_menu(_("Save")):
        text "Saves go here."

screen load:

    tag menu

    use game_menu(_("Load")):
        text "Saves go here."


screen preferences:

    tag menu

    use game_menu(_("Preferences")):
        frame:
            style "preference_frame"

            left_padding 5 * SCALE
            right_padding 2 * SCALE
            top_padding 2 * SCALE

            has vbox

            grid 4 1:
                style_group "choice_preference"
                xfill True

                vbox:
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    label _("Transitions")
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")

                vbox:
                    label _("Skip")
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")

                vbox:
                    label _("After Choices")
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")

            null height 5 * SCALE

            grid 2 1:
                style_group "bar_preference"
                xfill True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    style_group "bar_preference"

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_preference_button"


    # add "game_menu.png" alpha .1

style preferences_frame is interface_frame

style preference_button:
    left_padding 2 * SCALE
    selected_background Solid(ACCENT_COLOR, xsize=SCALE // 2)
    selected_hover_background Solid(HOVER_COLOR, xsize=SCALE // 2)
    xoffset 2

style choice_preference_button:
    top_margin SCALE

style choice_preference_button:
    size_group "preferences"

style bar_preference_slider:
    xsize .75

style bar_preference_label:
    top_margin int(1.5 * SCALE)
    bottom_margin SCALE / 2

style bar_preference_button:
    yalign 1.0

style mute_preference_button:
    top_margin int(1.5 * SCALE)
