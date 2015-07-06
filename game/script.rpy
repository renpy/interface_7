# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

    show expression "game_menu.png"
    # show expression Transform("main_menu.png", size=(1280, 720))
    pause

    return
