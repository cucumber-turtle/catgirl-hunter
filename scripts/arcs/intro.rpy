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

    mc "...Where am I?"

    show b excited
    b "Welcome to my home!"

    show b confused

    python:
        mcname = renpy.input("What is your name?", length=12)
        mcname = mcname.strip()

        if not mcname:
             mcname = "Doggo"

    mc "My name is [mcname]"

    show b excited
    b excited "What a lovely name! I am Bel."

    show b
    b "Well now Coyote, since you’ve arrived, I’d like to ask you for a favour!"

    menu:
        "Why should I?":
            show b confused
            b confused "Does there need to be a reason why?"
            b confused "You obviously just want to be entertained."
            show b
        "Sure, I guess...":
            pass

    b "You are here to hunt cats. More specifically, I want you to catch and
    collect cat girls."

    show b excited
    b excited "We don’t have too many here at Asylum, but you won’t be disappointed..."

    show b
    b "Do you have any questions, Coyote?"

    menu:
        "Why do you call me coyote?":
            show b excited
            b excited "Because you’re hunting cats, obviously!"
        "Why is this place so empty?":
            show b confused
            b confused "Well, because I like it this way.
            Is there anything wrong with that?"

    show b excited
    b excited "Alright now, off you go. Enjoy yourself!"

    jump first_mini_explore
