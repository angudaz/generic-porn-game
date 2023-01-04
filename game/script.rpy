# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define blank = Character(" ")
define m = Character("Mary Lisa the Demon Slayer (real)")
define j = Character("James the Jame")
define qm = Character("???")
define p = Character("Patricia the Pratricisnt")
define je = Character("Jennifer the Jennifurt Slayer")
image eileen movie = Movie(play="VID20211228WA0001.webm", size=(1920, 1080))

# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text "Random Retards on the Internet presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(3)

    show text "{b}Generic Porn Game{/b}"
    with Pause(2)

    hide text with dissolve
    with Pause(3)

    return

label start:

    scene black
    blank "You wake up in a "
    show eileen happy
    qm "Seggs?"
    show eileen movie
    m "The End"

    return
