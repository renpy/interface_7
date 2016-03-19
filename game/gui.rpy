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
define gui.ACCENT_COLOR = "#eebb00"

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

# The small color is used for small buttons, which need to be brighter/darker
# to achieve the same effect.
define gui.IDLE_SMALL_COLOR = "#aaaaaa"

# The color used for a text button when it cannot be selected.
define gui.INSENSITIVE_COLOR = "#55555580"

# The color used for dialogue and menu choice text.
define gui.TEXT_COLOR = "#ffffff"
define gui.CHOICE_COLOR = "#cccccc"

# The images used for the main and game menus.
define gui.MAIN_MENU_BACKGROUND = "gui/main_menu.jpg"
define gui.GAME_MENU_BACKGROUND = "gui/game_menu.jpg"


################################################################################
# Style reset.

style say_label:
    clear

style window:
    clear

style say_vbox:
    clear

style say_who_window:
    clear

style say_two_window_vbox:
    clear

style menu_choice:
    clear

style input:
    clear

style hyperlink_text:
    clear

################################################################################
# Style common user interface components.

# Used for full-sized buttons, like navigation buttons.
style button:
    ypadding 2
    xpadding 2
    background Frame("gui/button.png")
    hover_background Frame("gui/button_hover.png")

style button_text:
    size gui.scale(24)
    color gui.IDLE_COLOR
    insensitive_color gui.INSENSITIVE_COLOR
    selected_color gui.SELECTED_COLOR
    hover_color gui.HOVER_COLOR
    selected_hover_color gui.HOVER_COLOR

# Used for checkbox-like buttons:
style check_button:
    left_padding gui.scale(22)
    foreground Frame("gui/button_unchecked.png", 22, 0)
    selected_foreground Frame("gui/button_checked.png", 22, 0)

style radio_button is check_button

# Used for medium-sized buttons, like sound test and mute buttons.
style medium_button:
    background Frame("gui/medium_button.png")
    hover_background Frame("gui/medium_button_hover.png")

style medium_button_text is button_text

# Used for small-sized buttons, like file picker page navigation.
style small_button:
    background Frame("gui/small_button.png")
    hover_background Frame("gui/small_button_hover.png")

style small_button_text is button_text

style label_text:
    color gui.ACCENT_COLOR
    size gui.scale(24)

style prompt_text:
    color gui.TEXT_COLOR
    size gui.scale(24)

style bar:
    ysize gui.scale(30)

    left_bar Frame("gui/bar_left.png")
    right_bar Frame("gui/bar_right.png")

style scrollbar:
    ysize gui.scale(10)

    left_bar Frame("gui/scrollbar.png")
    thumb Frame("gui/scrollbar_thumb.png")
    right_bar Frame("gui/scrollbar.png")

    hover_left_bar Frame("gui/scrollbar_hover.png")
    hover_thumb Frame("gui/scrollbar_hover_thumb.png")
    hover_right_bar Frame("gui/scrollbar_hover.png")

style slider:
    ysize gui.scale(30)

    left_bar Frame("gui/slider.png")
    thumb "gui/slider_thumb.png"
    right_bar Frame("gui/slider.png")

    hover_left_bar Frame("gui/slider_hover.png")
    hover_thumb "gui/slider_hover_thumb.png"
    hover_right_bar Frame("gui/slider_hover.png")

style vbar:
    xsize gui.scale(30)
    bar_vertical True

    top_bar Frame("gui/bar_top.png")
    bottom_bar Frame("gui/bar_bottom.png")

style vscrollbar:
    xsize gui.scale(10)
    bar_vertical True
    bar_invert True

    top_bar Frame("gui/vscrollbar.png")
    thumb Frame("gui/vscrollbar_thumb.png")
    bottom_bar Frame("gui/vscrollbar.png")

    hover_top_bar Frame("gui/vscrollbar_hover.png")
    hover_thumb Frame("gui/vscrollbar_hover_thumb.png")
    hover_bottom_bar Frame("gui/vscrollbar_hover.png")

style vslider:
    xsize gui.scale(30)
    bar_vertical True

    top_bar Frame("gui/vslider.png")
    thumb "gui/vslider_thumb.png"
    bottom_bar Frame("gui/vslider.png")

    hover_top_bar Frame("gui/vslider_hover.png")
    hover_thumb "gui/vslider_hover_thumb.png"
    hover_bottom_bar Frame("gui/vslider_hover.png")

style frame:
    background "#000000"

style empty_gui_frame is default

style hyperlink_text:
    color gui.ACCENT_COLOR
    hover_color gui.HOVER_COLOR
    hover_underline True

style input:
    color gui.ACCENT_COLOR


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
                text " " id "who" xoffset gui.scale(-10)

            null height gui.scale(5)

            text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

style window:
    background "gui/textbox.png"
    xfill True
    xalign 0.5
    ysize gui.scale(185)
    yalign 1.0

style say_label:
    size gui.scale(30)


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

style input_prompt is text


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

style choice_button_text is default:
    color gui.CHOICE_COLOR
    hover_color gui.TEXT_COLOR

    # Center the text.
    xalign 0.5
    text_align 0.5
    layout "subtitle"

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            xsize gui.scale(800)
            xalign 0.5

            ypos gui.scale(10)
            ymaximum gui.scale(690)

            spacing gui.scale(10)


        vpgrid:
            cols 1
            yinitial 1.0

            # Display dialogue.
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id

                    has hbox:
                        yfill True
                        spacing gui.scale(20)

                    if who is not None:
                        text who id who_id

                    text what id what_id ypos gui.scale(7)

        # Displays the menu, if given. The menu may be displayed incorrectly
        # if config.narrator_menu is set to True, as it is above.
        if items:

            for caption, action, chosen in items:

                if action:
                    textbutton caption action action style "nvl_menu_button"
                else:
                    label caption style "nvl_menu_prompt"

    add SideImage() xalign 0.0 yalign 1.0

define config.nvl_list_length = 6

style nvl_dialogue:
    clear

style nvl_menu_button:
    clear
    left_padding gui.scale(20)

style nvl_menu_choice_button_text:
    clear

style nvl_entry:
    clear
    xfill True
    ysize gui.scale(115)

style nvl_label:
    clear
    xmaximum gui.scale(150)
    min_width gui.scale(150)
    text_align 1.0

style nvl_window is default:
    clear
    background "gui/nvl.png"
    xfill True
    yfill True


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
        style_prefix "nav_gui"

        xpos gui.scale(50)
        xmaximum gui.scale(227)

        yalign 0.5
        spacing gui.scale(8)

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Extras") action ShowMenu("extras")
        elif _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        else:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        textbutton _("Help") action ShowMenu("help")

        textbutton _("Quit") action Quit(confirm=not main_menu)


style nav_gui_button:
    xfill True



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
        style_prefix "gui"

        label title:
            # position the title.
            xpos gui.scale(50)
            ysize gui.scale(120)

            # text_ properties are used to style the text.
            text_size gui.scale(50)
            text_color gui.ACCENT_COLOR
            text_yalign 0.5

        frame:
            style "empty_gui_frame"
            bottom_margin gui.scale(30)

            hbox:

                # Reserve space for the navigation section.
                null width gui.scale(277)

                add "gui/vertical_separator.png"

                fixed:
                    transclude

    use navigation

    textbutton _("Return"):
        style_prefix "nav_gui"

        action Return()
        xpos gui.scale(50)
        xmaximum gui.scale(227)
        ypos config.screen_height - gui.scale(30)
        yanchor 1.0

screen file_picker(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:

            # This, and the fixed, ensures the input will get the enter event before
            # any of the buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.
            button:
                style_prefix "file_page_name_gui"

                key_events True
                xalign 0.5
                xpadding gui.scale(50)
                ypadding gui.scale(3)
                action page_name_value.Toggle()

                input:
                    value page_name_value

                    size gui.scale(24)
                    text_align 0.5
                    layout "subtitle"
                    color gui.ACCENT_COLOR
                    hover_color gui.HOVER_COLOR

            # The grid of file slots.
            grid 3 2:
                style_prefix "file_slot_gui"

                xalign 0.5
                yalign 0.5

                for i in range(6):
                    button:
                        action FileAction(i)

                        background "gui/idle_file_slot.png"
                        hover_background "gui/hover_file_slot.png"

                        # This include margins.
                        xsize gui.scale(296)
                        ysize gui.scale(226)

                        xpadding gui.scale(10)
                        ypadding gui.scale(10)

                        xmargin gui.scale(10)
                        ymargin gui.scale(5)

                        add FileScreenshot(i)

                        text FileTime(i, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty="Empty slot"):
                            style "file_slot_gui_button_text"
                            ypos 146

                        text FileSaveName(i):
                            style "file_slot_gui_button_text"
                            ypos 164

                        key "save_delete" action FileDelete(i)

            # Buttons to access other pages.
            hbox:
                style_prefix "file_page_gui"

                xalign 0.5
                yalign 1.0

                textbutton _("<") action FilePagePrevious()

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

screen load():

    tag menu

    use file_picker(_("Load"))

screen save():

    tag menu

    use file_picker(_("Save"))

define config.thumbnail_width = gui.scale(256)
define config.thumbnail_height = gui.scale(144)

style file_page_gui_button:
    xpadding gui.scale(7)
    ypadding gui.scale(3)

style file_slot_gui_button_text:
    size gui.scale(14)

    color gui.IDLE_SMALL_COLOR
    hover_color gui.HOVER_COLOR
    selected_color gui.SELECTED_COLOR

    xalign 0.5
    text_align 0.5
    layout "subtitle"


screen preferences:

    tag menu

    use game_menu(_("Preferences")):

        vbox:
            xpos gui.scale(50)
            ypos gui.scale(20)
            xsize gui.scale(930)

            grid 4 1:
                style_prefix "choice_pref_gui"
                xfill True

                vbox:
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    label _("Skip")
                    textbutton _("Unseen Dialogue") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                null

            null height gui.scale(25)

            # If a second row of preferences is desired, the preferences can
            # be added here.

            null height gui.scale(25)

            grid 2 1:
                style_prefix "bar_pref_gui"
                xfill True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

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
                        style "mute_pref_gui_button"

style choice_pref_gui_label:
    ysize gui.scale(30)

style choice_pref_gui_label_text:
    size gui.scale(24)
    yalign 1.0

style pref_gui_button:
    left_padding gui.scale(20)
    selected_background Solid(gui.ACCENT_COLOR, xsize=gui.scale(5))
    selected_hover_background Solid(gui.HOVER_COLOR, xsize=gui.scale(5))
    xoffset gui.scale(2)

style choice_pref_gui_button:
    top_margin gui.scale(10)

style choice_pref_gui_button:
    size_group "preferences"

style bar_pref_gui_slider:
    xsize gui.scale(350)

style bar_pref_gui_label:
    top_margin gui.scale(10)
    bottom_margin gui.scale(3)
    ysize gui.scale(30)

style bar_pref_gui_label_text:
    size gui.scale(24)
    yalign 1.0

style bar_pref_gui_button:
    yalign 1.0

style mute_pref_gui_button is gui_button:
    top_margin gui.scale(15)



##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    add "gui/yesno_darken.png"

    frame:
        style_prefix "yesno_gui"

        background "gui/yesno_background.png"
        xpadding gui.scale(75)
        ypadding gui.scale(50)
        xsize gui.scale(600)
        ysize gui.scale(250)
        xalign .5
        yalign .5

        has vbox:
            xalign .5
            yalign .5
            spacing gui.scale(30)

        label _(message):
            style "yesno_gui_prompt"
            xalign 0.5
            text_text_align 0.5
            text_layout "subtitle"

        hbox:
            xalign 0.5
            spacing gui.scale(100)

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

style yesno_gui_button:
    size_group "yesno"
    xpadding 25
    ypadding 10

style yesno_gui_button_text:
    xalign 0.5

define config.quit_action = Quit()


##############################################################################
# About
#
# A screen that gives copyright information about the game and Ren'Py.
screen about():

    tag menu

    use game_menu(_("About")):

        style_prefix "about_gui"

        viewport:

            scrollbars "vertical"
            mousewheel True
            draggable True

            side_xalign 0.5
            side_spacing gui.scale(20)

            xsize gui.scale(744)


            text gui.ABOUT

# Text that goes into the about screen. You can replace the first line
# with a series of lines that credit the creators of this game and the
# assets it uses.
#
# You need to leave the Ren'Py license info in, and we'd like it if you
# left the "Made with" credit.
define gui.ABOUT = _("""\
{b}[config.name]{/b}

Made with [renpy.version_string].

[renpy.license!t]""")


style about_gui_vscrollbar:
    unscrollable "hide"

##############################################################################
# Help
#
# A screen that gives information about key and mouse bindings.
screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help")):

        style_prefix "help_gui"

        vbox:
            xpos gui.scale(50)
            spacing gui.scale(15)

            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigates the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("H")
        text _("Hides the user interface.")

    hbox:
        label _("S")
        text _("Takes a screenshot.")

    hbox:
        label _("V")
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label ("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigates the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_gui_button:
    xpadding gui.scale(10)
    ypadding gui.scale(10)

style help_gui_label:
    xsize gui.scale(250)
    right_padding gui.scale(20)

style help_gui_label_text:
    size gui.scale(22)
    xalign 1.0
    text_align 1.0
