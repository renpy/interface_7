init offset = 1

screen quick_menu():

    variant "touch"

    # Ensure this appears on top of other screens.
    zorder 100

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Menu") action ShowMenu()
        textbutton _("Auto") action Preference("auto-forward", "toggle")

style quick_button:
    variant "touch"

    background None
    xpadding gui.scale(60)
    top_padding gui.scale(14)
