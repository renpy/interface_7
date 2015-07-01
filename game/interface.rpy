# This file is in the public domain. Feel free to modify it as a basis
# for your own interface.


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
    add "main_menu.png"

     # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

