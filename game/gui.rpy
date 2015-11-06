# This file is in the public domain. Feel free to modify it as a basis
# for your own interface.

################################################################################
# Sizes
#
# These will need to be changed if you change the size of the game. Remember
# to click "Window" in preferences to ensure the window itself is resized.

# The width and height of the screen.
define config.screen_width = 1280
define config.screen_height = 720

# Scale factor for various sizes. 1.0 is the default size
define gui.SCALE_FACTOR = config.screen_width / 1280.0

# The size of text in text buttons and labels.
define gui.HUGE_SIZE = gui.scale(50)
define gui.XLARGE_SIZE = gui.scale(28)
define gui.LARGE_SIZE = gui.scale(24)
define gui.NORMAL_SIZE = gui.scale(22)
define gui.SMALL_SIZE = gui.scale(16)

define gui.WINDOW_HEIGHT = gui.scale(268)

################################################################################
# Colors
#
# The colors of various aspects of the interface.

# An accent color used throughout the interface.
define gui.ACCENT_COLOR = "#00b8c3"

# define gui.HOVER_COLOR = "#00cad6"
# define gui.MUTED_COLOR = "#00373a"
# define gui.HOVER_MUTED_COLOR = "#00494e"

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

################################################################################
# Window, Frame, Pane, and Menu backgrounds

# The background of the main menu and game menu.
define gui.MAIN_MENU_BACKGROUND = "main menu.jpg"
define gui.GAME_MENU_BACKGROUND = "game menu.jpg"

# Solid colors that are overlaid on those backgrounds to darken or lighten
# them.
define gui.MAIN_MENU_DARKEN = "#000000cc"
define gui.GAME_MENU_DARKEN = "#000000cc"

# The background of the window containing dialogue from characters.
define gui.WINDOW_BACKGROUND = "#000000cc"

define gui.CHOICE_BACKGROUND = Frame("choice.png", gui.scale(35), gui.scale(0))
define gui.CHOICE_HOVER_BACKGROUND = Frame(gui.recolor("choice.png", gui.ACCENT_COLOR), gui.scale(35), gui.scale(0))

define gui.INPUT_BACKGROUND = Frame("input.png", gui.scale(35), gui.scale(0))

define gui.SKIPPING_BACKGROUND = Frame(gui.recolor("skipping.png", gui.ACCENT_COLOR), gui.scale(35), gui.scale(0))

# Vertical lines made up of the accent color.
define gui.VERTICAL_SEPARATOR = gui.vline(gui.ACCENT_COLOR, 3)

################################################################################
# Style common user interface components.

style button_text:
    size gui.NORMAL_SIZE
    color gui.IDLE_COLOR
    insensitive_color gui.INSENSITIVE_COLOR
    selected_color gui.SELECTED_COLOR
    hover_color gui.HOVER_COLOR
    selected_hover_color gui.HOVER_COLOR

style label_text:
    color gui.ACCENT_COLOR

style interface_frame is default

style bar:
    ysize gui.scale(30)
    left_bar Solid(gui.ACCENT_COLOR)
    right_bar Solid(gui.MUTED_COLOR)
    hover_left_bar Solid(gui.HOVER_COLOR)
    hover_right_bar Solid(gui.HOVER_MUTED_COLOR)

style slider is bar

################################################################################
# Derived constants.
define gui.PANE_WIDTH = gui.scale(280)



screen say(who, what, side_image=None, two_window=False):
    style_group "say"

    window:
        id "window"
        yminimum 190

        fixed:
            fit_first "height"

            vbox:
                xsize gui.scale(744)
                xpos gui.WINDOW_HEIGHT

                null height gui.scale(20)

                if who:
                    text who id "who"
                else:
                    text " " id "who"

                null height gui.scale(10)

                text what id "what"

            use quick_menu

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

style window:
    background Frame("textbox.png", 0, 0)
    yminimum gui.scale(190)

style say_vbox:
    spacing 0

style say_label:
    size gui.scale(30)
    bold False

screen quick_menu(**properties):
    hbox:
        xalign 1.0
        ypos gui.scale(7)
        spacing gui.scale(20)
        properties properties

        iconbutton "rollback":
            caption _("rollback")
            action Rollback()

        iconbutton "skip":
            caption _("skip")
            action Skip()
            alternate Skip(fast=True, confirm=True)

        iconbutton "auto":
            caption _("auto")
            action Preference("auto-forward", "toggle")

        iconbutton "save":
            caption _("save")
            action ShowMenu("save")
            alternate QuickSave()

        iconbutton "load":
            caption _("load")
            action ShowMenu("load")
            alternate QuickLoad()

        iconbutton "preferences":
            caption _("preferences")
            action ShowMenu("preferences")

        iconbutton "history":
            caption _("history")

        iconbutton "menu":
            caption _("menu")
            action ShowMenu()

        # This has been added to ensure there's spacing between the
        # last icon and the right end of the game.
        null

style iconbutton:
    xsize gui.scale(25)
    ysize gui.scale(42)

style iconbutton_text:
    xalign 0.5
    size gui.SMALL_SIZE
    color "#0000"
    selected_idle_color gui.SELECTED_COLOR
    hover_color gui.ACCENT_COLOR
    selected_hover_color gui.SELECTED_COLOR

style iconbutton_icon:
    color gui.IDLE_COLOR
    selected_color gui.SELECTED_COLOR
    hover_color gui.ACCENT_COLOR
    selected_hover_color gui.ACCENT_COLOR
    insensitive_color gui.INSENSITIVE_COLOR

    yalign 1.0



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

    # If the say screen is not showing, show the quick menu at the bottom
    # of the screen.
    if not renpy.get_screen("say"):
        use quick_menu(yalign=1.0)

# Use the narrator to speak menu captions.
define config.narrator_menu = True

style choice_vbox:

    # Center the choices horizontally, then offset them a bit.
    xalign 0.5
    xoffset gui.scale(10)

    # Center the choices vertically in the area above the text window.
    ypos gui.scale(270)
    yanchor 0.5


    # Add some space between choices.
    spacing gui.NORMAL_SIZE

style choice_button is default:
    background gui.CHOICE_BACKGROUND
    hover_background gui.CHOICE_HOVER_BACKGROUND
    hover_foreground gui.vline(gui.TEXT_COLOR, 8)

    xsize gui.scale(765)
    xpadding gui.scale(25)

    ypadding gui.NORMAL_SIZE / 2

style choice_button_text:
    color gui.CHOICE_COLOR
    hover_color gui.TEXT_COLOR

screen skip_indicator:
    frame:
        ypos gui.scale(10)
        background gui.SKIPPING_BACKGROUND
        ypadding gui.SMALL_SIZE / 3
        left_padding gui.SMALL_SIZE
        right_padding gui.scale(50)

        has hbox:
            spacing gui.scale(6)

        text _("Skipping") size gui.SMALL_SIZE

        add skip_triangle(0)
        add skip_triangle(.2)
        add skip_triangle(.4)

transform skip_triangle(delay):
    gui.recolor("skip triangle.png", gui.TEXT_COLOR)
    zoom .66 * gui.SCALE_FACTOR
    ypos gui.scale(4)
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause 1.0
        repeat

##############################################################################
# Input
#
# Screen that's used to prompt for text input, inside and outside the game.

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"

        null height (gui.NORMAL_SIZE / 2)

        input id "input" style "input_text"

style input_window is default:
    clear

    # Center the choices horizontally, then offset them a bit.
    xalign 0.5
    xoffset gui.scale(10)

    # Center the choices vertically in the area above the text window.
    ypos gui.scale(270)
    yanchor 0.5

    background gui.INPUT_BACKGROUND
    hover_foreground gui.vline(gui.TEXT_COLOR, 8)

    xsize gui.scale(765)
    xpadding gui.scale(25)

    ypadding gui.NORMAL_SIZE

style input_prompt is default:
    clear

style input_text is default:
    clear

    color gui.ACCENT_COLOR
    adjust_spacing False


################################################################################
# Navigation
#
# This screen is not called directly, but included via the use statement. It
# provides the buttons on the left side of the screen, which make up the main
# menu and game menu navigation.

screen navigation():

    vbox:
        style_group "nav"

        xpos gui.scale(50)
        xmaximum gui.PANE_WIDTH - gui.scale(50)

        yalign 0.5
        spacing gui.LARGE_SIZE // 2


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


style nav_button_text:
    size gui.LARGE_SIZE


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

    hbox:
        style_group "interface"

        frame:
            background gui.MAIN_MENU_DARKEN
            xsize gui.PANE_WIDTH
            yfill True

        add gui.VERTICAL_SEPARATOR

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

    add gui.GAME_MENU_DARKEN

    vbox:
        style_group "interface"

        label title:
            # position the title.
            xpos gui.scale(50)
            ysize gui.scale(120)

            # text_ properties are used to style the text.
            text_size gui.HUGE_SIZE
            text_color gui.ACCENT_COLOR
            text_yalign 0.5

        frame:
            style "interface_frame"

            bottom_margin gui.scale(30)

            hbox:

                # Reserve space for the navigation section.
                null width gui.PANE_WIDTH
                add gui.VERTICAL_SEPARATOR

                transclude

    use navigation

    textbutton _("Return"):
        style "nav_button"
        action Return()
        xpos gui.scale(50)
        ypos config.screen_height - gui.scale(30)
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
    size gui.LARGE_SIZE
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
    size gui.LARGE_SIZE
    yalign 1.0

style bar_preference_button:
    yalign 1.0

style mute_preference_button:
    top_margin gui.scale(15)

################################################################################
# Help

screen help_entry(entry, mouse=None, key=None, touch=None, gamepad=None):

    python:
        help = [ ]

        if mouse:
            help.append(mouse)
        if key:
            help.append(key)
        if touch:
            help.append(touch)
        if gamepad:
            help.append(gamepad)

        help_text = __("{#help}, ").join(__(i) for i in help)

    if help:
        hbox:
            label entry
            text help_text

screen help():
    tag menu

    use game_menu(_("Help")):

        frame:
            style "interface_frame"

            has vbox

            use help_entry(_("Advance:"), _("Left-click"), _("Enter, Space"), _("Touch"), _("Gamepad A"))


################################################################################
# Utility Functions
#
# This code is run at -1, to ensure it's run before the code above.

init -1 python in gui:

    from store import im, Solid

    def scale(n):
        """
        Returns `n` scaled by gui.SCALE_FACTOR, rounded to the next-lowest
        integer.
        """

        return int(n * SCALE_FACTOR)

    def recolor(image, color):
        return im.MatrixColor(image, im.matrix.colorize(color, color))

    def vline(color, width):
        return Solid(color, xsize=scale(width))
