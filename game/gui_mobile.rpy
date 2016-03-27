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

screen choice_preferences():

    variant [ "android", "ios" ]

    grid 2 1:
        xfill True

        vbox:
            style_prefix "radio_pref"
            label _("Rollback Side")
            textbutton _("Disable") action Preference("rollback side", "disable")
            textbutton _("Left") action Preference("rollback side", "left")
            textbutton _("Right") action Preference("rollback side", "right")

        vbox:
            style_prefix "check_pref"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))


screen help():

    variant "touch"

    tag menu

    default device = "touch"

    use game_menu(_("Help")):

        style_prefix "help"

        vbox:
            spacing gui.scale(15)

            hbox:

                textbutton _("Touch") action SetScreenVariable("device", "touch")

            if device == "touch":
                use touch_help


screen touch_help():

    hbox:
        label _("Touch")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Touch Rollback Side")
        text _("Rolls back to earlier dialogue.")

