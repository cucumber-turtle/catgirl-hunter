################################################################################
## Map mini exploration
################################################################################
default kitchen_perm = False
default bedroom_perm = False
default library_perm = False

init python:
    def check_floor_permission(floor):
        if floor is "floor1":
            return kitchen_perm
        elif floor is "floor2":
            return bedroom_perm
        elif floor is "floor3":
            return library_perm

label first_mini_explore:
    scene bg_whitespace
    play music "audio/Waltz in G flat major, Op. 70 no. 1.mp3"
    call screen area_map(True)

# Placeholders until I need to use them

label navigate_floor1:
    "pressed 1"
    return

label navigate_floor2:
    "pressed 2"
    return

label navigate_floor3:
    "pressed 3"
    return
