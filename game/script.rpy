# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

label main_menu:
    return


# The game starts here.
label start:
    e "Hello, world.\nHello, world."


    show expression Transform("dialogue.png", size=(1280, 720))
    pause
