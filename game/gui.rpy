################################################################################
# Sizes
#
# These will need to be changed if you change the size of the game. Remember
# to click "Window" in preferences to ensure the window itself is resized.

# The width and height of the screen.
define config.screen_width = 1280
define config.screen_height = 720

################################################################################
# Colors
#
# The colors of various aspects of the interface.

# An accent color used throughout the interface.
define gui.ACCENT_COLOR = "#00b8c3"

# define gui.HOVER_COLOR = "#00cad6"
# define gui.MUTED_COLOR = "#00373a"
# define gui.HOVER_MUTED_COLOR = "#00494e"

# TODO: Replace with the generated colors.
define gui.HOVER_COLOR = Color(gui.ACCENT_COLOR).tint(.6)
define gui.MUTED_COLOR = Color(gui.ACCENT_COLOR).shade(.4)
define gui.HOVER_MUTED_COLOR = Color(gui.ACCENT_COLOR).shade(.6)

# The color used for a text button when it is selected but not focused.
# A button is selected if it is the current screen or preference value
define gui.SELECTED_COLOR = "#ffffff"

# The color used for a text button when it is neither selected nor hovered.
define gui.IDLE_COLOR = "#555555"

# The color used for a text button when it cannot be selected.
define gui.INSENSITIVE_COLOR = "#55555580"

# The color used for dialogue and menu choice text.
define gui.TEXT_COLOR = "#ffffff"
define gui.CHOICE_COLOR = "#cccccc"

# The images used for the main and game menus.
define gui.MAIN_MENU_BACKGROUND = "gui/main_menu.jpg"
define gui.GAME_MENU_BACKGROUND = "gui/game_menu.jpg"


################################################################################
# Style common user interface components.

style button_text:
    size gui.scale(22)
    color gui.IDLE_COLOR
    insensitive_color gui.INSENSITIVE_COLOR
    selected_color gui.SELECTED_COLOR
    hover_color gui.HOVER_COLOR
    selected_hover_color gui.HOVER_COLOR

style label_text:
    color gui.ACCENT_COLOR

style bar:
    ysize gui.scale(30)
    left_bar Solid(gui.ACCENT_COLOR)
    right_bar Solid(gui.MUTED_COLOR)
    hover_left_bar Solid(gui.HOVER_COLOR)
    hover_right_bar Solid(gui.HOVER_MUTED_COLOR)

style slider is bar

# ...
style interface_frame is default


################################################################################
# Say

screen say(who, what, side_image=None, two_window=False):
    style_group "say"

    window:
        id "window"

        vbox:
            xsize gui.scale(744)
            xalign 0.5

            null height gui.scale(5)

            if who:
                text who id "who" xoffset gui.scale(-10)
            else:
                text " " id "who"

            null height gui.scale(5)

            text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

style window:
    background "gui/textbox.png"
    ysize gui.scale(185)

style say_label:
    size gui.scale(30)
    bold False

# It'll probably be better to fix this up in the legacy style system.
style say_vbox:
    spacing 0


################################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input
screen input(prompt):
    style_group "input"

    window:

        vbox:
            xsize gui.scale(744)
            xalign 0.5

            null height gui.scale(5)

            text " " style "say_label"

            null height gui.scale(5)

            text prompt style "input_prompt"

            input id "input"

style input:
    color gui.ACCENT_COLOR


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_group "choice"

    vbox:
        for caption, action, chosen in items:
            textbutton caption action action

# Use the narrator to speak menu captions.
define config.narrator_menu = True

style choice_vbox:

    # Center the choices horizontally, then offset them a bit.
    xalign 0.5

    # Center the choices vertically in the area above the text window.
    ypos gui.scale(270)
    yanchor 0.5

    # Add some space between choices.
    spacing gui.scale(22)

style choice_button is default:
    background Frame("gui/choice_button.png", 0, 5)
    hover_background Frame("gui/hover_choice_button.png", 0, 5)

    xsize gui.scale(790)
    xpadding gui.scale(100)

    ypadding gui.scale(11) / 2

style choice_button_text:
    color gui.CHOICE_COLOR
    hover_color gui.TEXT_COLOR

    # Center the text.
    xalign 0.5
    text_align 0.5
    layout "subtitle"

################################################################################
# Quick Menu

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Log")
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Prefs") action ShowMenu('preferences')

style quick_button:
    background None
    xpadding 10

style quick_button_text:
    size gui.scale(14)

init python:
    config.overlay_screens.append("quick_menu")


################################################################################
# Navigation
#
# This screen serves to navigate within the main and game menus.

screen navigation():

    vbox:
        style_group "nav"

        xpos gui.scale(50)
        xmaximum gui.scale(230)

        yalign 0.5
        spacing gui.scale(12)


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

        textbutton _("Help") action ShowMenu("help")

        textbutton _("Quit") action Quit(confirm=not main_menu)


style nav_button:
    xfill True

style nav_button_text:
    size gui.scale(24)


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

    add gui.MAIN_MENU_BACKGROUND
    add "gui/main_menu_darken.png"

    # The actual contents of the main menu are in the navigation screen, above.
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
    if main_menu:
        add gui.MAIN_MENU_BACKGROUND
    else:
        add gui.GAME_MENU_BACKGROUND

    add "gui/game_menu_darken.png"

    vbox:
        style_group "interface"

        label title:
            # position the title.
            xpos gui.scale(50)
            ysize gui.scale(120)

            # text_ properties are used to style the text.
            text_size gui.scale(50)
            text_color gui.ACCENT_COLOR
            text_yalign 0.5

        frame:
            style "interface_frame"

            bottom_margin gui.scale(30)

            hbox:

                # Reserve space for the navigation section.
                null width gui.scale(280)

                # add gui.VERTICAL_SEPARATOR

                transclude

    use navigation

    textbutton _("Return"):
        style "nav_button"
        action Return()
        xpos gui.scale(50)
        ypos config.screen_height - gui.scale(30)
        yanchor 1.0



screen preferences:

    tag menu

    use game_menu(_("Preferences")):
        frame:
            style "interface_frame"

            left_padding gui.scale(50)
            right_padding gui.scale(20)
            top_padding gui.scale(20)

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

            null height gui.scale(25)

            # If a second row of preferences is desired, the preferences can
            # be added here.

            null height gui.scale(25)

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

style choice_preference_label:
    ysize gui.scale(30)

style choice_preference_label_text:
    size gui.scale(24)
    yalign 1.0

style preference_button:
    left_padding gui.scale(20)
    selected_background Solid(gui.ACCENT_COLOR, xsize=gui.scale(5))
    selected_hover_background Solid(gui.HOVER_COLOR, xsize=gui.scale(5))
    xoffset gui.scale(2)

style choice_preference_button:
    top_margin gui.scale(10)

style choice_preference_button:
    size_group "preferences"

style bar_preference_slider:
    xsize .75

style bar_preference_label:
    top_margin gui.scale(10)
    bottom_margin gui.scale(3)
    ysize gui.scale(30)

style bar_preference_label_text:
    size gui.scale(24)
    yalign 1.0

style bar_preference_button:
    yalign 1.0

style mute_preference_button:
    top_margin gui.scale(15)
