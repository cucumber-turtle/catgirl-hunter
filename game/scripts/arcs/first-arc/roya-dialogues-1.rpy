################################################################################
## First arc
## Roya's dialogue
################################################################################
define r = Character("Roya", color="#c47b97", image="r")

# Character images
image r = "characters/roya.png"

# Character side images
image side r = "icons/roya_side.png"

label first_roya_1:
    scene bg_whitespace

    play music "audio/spacedust.mp3"

    show r
    r "...Hi"