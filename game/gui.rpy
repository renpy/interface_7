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
define gui.SMALL_SIZE = gui.scale(18)


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

################################################################################
# Window, Frame, Pane, and Menu backgrounds

# The background of the main menu and game menu.
define gui.MAIN_MENU_BACKGROUND = "images/main menu.jpg"
define gui.GAME_MENU_BACKGROUND = "images/game menu.jpg"

# Solid colors that are overlaid on those backgrounds to darken or lighten
# them.
define gui.MAIN_MENU_DARKEN = "#000000cc"
define gui.GAME_MENU_DARKEN = "#000000cc"

# The background of the window containing dialogue from characters.
define gui.WINDOW_BACKGROUND = "#000000cc"

# Vertical lines made up of the accent color.
define gui.VERTICAL_SEPARATOR = Solid(gui.ACCENT_COLOR, xsize=gui.scale(3))
define gui.WIDE_VLINE = Solid(gui.ACCENT_COLOR, xsize=gui.scale(5))

################################################################################
# Style common user interface components.

style button_text:
    size gui.NORMAL_SIZE
    color gui.IDLE_COLOR
    insensitive_color gui.INSENSITIVE_COLOR
    selected_color gui.SELECTED_COLOR
    hover_color gui.HOVER_COLOR
    selected_hover_color gui.HOVER_COLOR

style label:
    ysize gui.scale(30)

style label_text:
    size gui.LARGE_SIZE
    color gui.ACCENT_COLOR
    yalign 1.0

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

    window:
        id "window"
        yminimum 190

        fixed:
            fit_first "height"

            vbox:
                xsize gui.scale(744)
                xpos gui.scale(268)

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
    background None # Frame("textbox.png", 0, 0)
    yminimum gui.scale(190)

style say_label:
    size gui.scale(28)
    bold False

screen quick_menu():
    hbox:
        xalign 1.0
        ypos gui.scale(7)
        xpos 1058

        iconbutton "save" caption _("Save") action ShowMenu("save")

style iconbutton:
    xsize gui.scale(25)
    ysize gui.scale(47)

style iconbutton_text:
    xalign 0.5
    size 15
    color "#0000"
    selected_idle_color gui.SELECTED_COLOR
    hover_color gui.ACCENT_COLOR
    selected_hover_color gui.SELECTED_COLOR
    insensitive_color gui.INSENSITIVE_COLOR

style iconbutton_icon:
    color gui.IDLE_COLOR
    selected_color gui.SELECTED_COLOR
    hover_color gui.ACCENT_COLOR
    selected_hover_color gui.ACCENT_COLOR
    insensitive_color gui.INSENSITIVE_COLOR

    yalign 1.0

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

        textbutton _("Help") action Help()

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
            style "preference_frame"

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


style preferences_frame is interface_frame

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

style bar_preference_button:
    yalign 1.0

style mute_preference_button:
    top_margin gui.scale(15)



################################################################################
# Utility Functions
#
# This code is run at -1, to ensure it's run before the code above.

init -1 python in gui:

    def scale(n):
        """
        Returns `n` scaled by gui.SCALE_FACTOR, rounded to the next-lowest
        integer.
        """

        return int(n * SCALE_FACTOR)
