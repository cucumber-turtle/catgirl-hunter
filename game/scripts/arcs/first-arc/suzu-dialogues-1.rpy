################################################################################
## First arc
## Suzu's dialogue
################################################################################
define s = Character("Suzu", color="#ffac44", image="s")

# Character images
image s = "characters/suzu.png"

# Character side images
image side s = "icons/suzu_side.png"

label first_suzu_1:
    scene bg_whitespace

    play music "audio/spacedust.mp3"

    show s
    s "Oooooooh~ a newbie!"

    jump first_roya_1

    return