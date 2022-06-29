# The script for the game intro scene

init offset = -1

# Defining characters, their colours, and images
define b = Character("Bel", color="#ffffff", image="b")
define mc = Character("[mcname]", color="#f0b190", image="mc")

# Variable for player's name
default mcname = "???"

# Images for the characters defined above
image b excited = "characters/bel_excited.png"
image b surprised = "characters/bel_surprised.png"
image b confused = "characters/bel_confused.png"
image b = "characters/bel.png"

# Side images for the characters defined above
image side b excited = "icons/bel_side_excited.png"
image side b surprised = "icons/bel_side_surprised.png"
image side b confused = "icons/bel_side_confused.png"
image side b = "icons/bel_side.png"

image side mc excited = "icons/mc_excited.png"
image side mc = "icons/mc.png"

# The game starts here.

label start:

    scene bg_whitespace

    play music "audio/OnWaldenPond.mp3"

    show b

    b "You've created a new Ren'Py game."

    mc "Oh wow"

    python:
        mcname = renpy.input("What is your name?", length=12)
        mcname = mcname.strip()

        if not mcname:
             mcname = "Doggo"

    mc "My name is [mcname]"

    show b excited

    b excited "Once you add a story, pictures, and music, you can release it to the world!"

    jump mini_explore
