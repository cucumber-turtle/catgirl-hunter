################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.05 yalign 0.75


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 480
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

## Navigation map screen
##
## This is so the user can choose which area to go and jump to the appropriate
## scene in the game.

## Animation of Bel waving
image bel_waving:
    "misc/bel_navigation_2.png"
    pause 0.3
    "misc/bel_navigation_3.png"
    pause 0.3
    repeat

## The map for navigating between different areas in the game
## Navigating to places requires permission which the user gets from talking to characters
screen area_map(firstMap = False):
    add "backgrounds/bg_perspective2.png"

    imagebutton:
        xpos 448
        ypos 449
        idle "backgrounds/floor1_idle.png"
        hover "backgrounds/floor1_hover.png"
        action If(check_floor_permission("floor1"), Jump("navigate_floor1"),
        Notify("You need permission to enter the kitchen!"))

    imagebutton:
        xpos 431
        ypos 270
        idle "backgrounds/floor2_idle.png"
        hover "backgrounds/floor2_hover.png"
        action If(check_floor_permission("floor2"), Jump("navigate_floor2"),
        Notify("You need permission to enter Roya's room!"))

    imagebutton:
        xpos 443
        ypos 54
        idle "backgrounds/floor3_idle.png"
        hover "backgrounds/floor3_hover.png"
        action If(check_floor_permission("floor3"), Jump("navigate_floor3"),
        Notify("You need permission to enter the library!"))

    # If the map is shown at the start of the game
    # Clio is shown waiting
    if firstMap is True:
        imagebutton:
            xpos 900
            ypos 590
            idle "misc/clio_navigation_1small.png"
            hover "misc/clio_navigation_2.png"
            action Jump("first_clio")

    add "objects/chair.png" xpos 200 ypos 580

    imagebutton:
        xpos 200
        ypos 580
        idle "misc/bel_navigation_1.png"
        hover "bel_waving"
        action NullAction() # Clicking Bel should have no effect

# Clicker game
screen game_clicker(imageName):
    add "backgrounds/bg_whitespace.png"

    python:
        back = Card("back", [-1,-1], "none")
        emperor1 = Card("emperor", [0,0], "none")
        emperor2 = Card("emperor", [1,0], "none")
        priestess1 = Card("high_priestess", [0,1], "none")
        priestess2 = Card("high_priestess", [0,2], "none")
        moon1 = Card("moon", [0,3], "none")
        moon2 = Card("moon", [1,1], "none")
        devil1 = Card("devil", [1,2], "none")
        devil2 = Card("devil", [1,3], "none")

    grid 4 2:
        # An image button for every card
        # First row
        imagebutton:
            idle back.image # Back of card
            hover emperor1.image # Front of card
            action NullAction() # Clicking card should show front of card and match with other selected cards
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        # Second row
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        imagebutton:
            idle back.image
            hover emperor1.image
            action NullAction()
        
        xmargin 250
        ymargin 60
        spacing 50

    # REMOVE THIS AFTER FINISHING CODE FOR MINIGAME
    hbox:
        textbutton "Win" action Call("clio_win_1")
        textbutton "Lose" action Call("clio_lose_1")

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

    class Card:
        def __init__(self, card_type, position, transformation):
            self.type = card_type
            self.position = position
            self.transformation = transformation
            self.image = f"minigame/{self.type}.png"

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
