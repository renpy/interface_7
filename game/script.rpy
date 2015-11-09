# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

label main_menu:
    return

# The game starts here.
label start:

    # scene bg lwa desk
    scene bg mugen

    e "Is this particularly hard to read? No, I don't think so. Do you? But what happens when I add a lot more text to it - to the point where it wraps not once, not twice, but three times - leading to four lines in all. With more text like this."

    scene expression "#ccc"

    "..."

    $ renpy.input("Hello, how are you?")

label loop:
    "A"
    "B"
    "C"
    "D"
    jump loop

    menu:
        e "I made it back to what I can only assume is my dorm room. What should I be doing for the rest of the night?"

        "Cleaning my desk.":
            pass

        "Reading the Lemma Soft Forums.":
            pass

        "Figuring out why I'm trapped in a fantasy anime.":
            pass

    show expression Transform("dialogue.png", size=(1280, 720))

    menu:
        "This is choice 2.1":
            pass

        "This is choice 2.2":
            pass

        "This is choice 2.3":
            pass



    e "Hello, world.\nHello, world."

    e "At that time it was quite clear in my own mind that the Thing had come from the planet Mars, but I judged it improbable that it contained any living creature. I thought the unscrewing might be automatic."

    show expression Transform("dialogue.png", size=(1280, 720))

    e "At that time it was quite clear in my own mind that the Thing had come from the planet Mars, but I judged it improbable that it contained any living creature. I thought the unscrewing might be automatic."

