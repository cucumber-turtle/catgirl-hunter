################################################################################
## First arc
################################################################################
define c = Character("Clio", color="#f5e3b0", image="c")

# Character images
image c unamused = "characters/clio_unamused.png"
image c = "characters/clio.png"

# Character side images
image side c unamused = "icons/clio_side_unamused.png"
image side c = "icons/clio_side.png"

label first_clio:
    scene bg_whitespace

    play music "audio/spacedust.mp3"

    show c
    c "Why hello there, cutie."

    b "This is Clio, treat her with respect."

    show c unamused
    c unamused "Funny you say that now, Bel. Stop talking, you're confusing cutie."

    menu:
        "I'm not confused...":
            show c
            c "Ah, really? Bel needs to be quiet anyway."
        "Treat her with respect?":
            mc "How am I supposed to be respectful when you want me to hunt her?"
            show c
            c "Yes! That is exactly it. You're either respectful or you're not."
            c "I'm glad you're more reasonable than the guy that brought you here."

    c "Anyway... welcome to Asylum. I'm Clio. I own the library here."

    mc "So you're a librarian?"

    c "Kind of. But it's not work. It's just my living space."
    c "You'll understand what I mean later."

    mc "You know I'm meant to hunt you... why aren't you scared?"

    c "Should I be scared?"

    menu:
        "Yes":
            c "I don't know why I should be scared, but here, this is fun.
            The others are excited to meet you as well."
        "No":
            c "Yes, you don't look scary to me. You look docile, cutie."

    b confused "Okaaaay. Are you playing or not?"

    show c unamused
    c unamused "Yes."

    show c
    c "I'll explain the rules. If you win, that means you caught me.
    If you lose... well..."

    b excited "I'll laugh at you."

    show c unamused
    c unamused "...He'll laugh at you."
    show c
    c "Are you ready to play? If not, you can come back later."

    menu:
        "Yes, I'm ready":
            c "Great!"
            jump card_game_clio
        "No. I'll come back later":
            c "Okay, see you later cutie."

    return

label card_game_clio:
    call screen game_clicker(None)
