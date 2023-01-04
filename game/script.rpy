# Characters (when you go to use these, blank usually describes the
# scene, is used to make sound effects, etc.  If you want to make
# the characters say something in their head, put the abbreviation
# thats defined and make all the text surrounded in {i}{/i}.
#
# Yelling can be emphasized with {b}{/b}
# Empasis without yelling is {u}{/u}
# If you'd like to use other ways of emphasis, read the docs > Text
# > Stylizing and Text Tags

define blank = Character(" ")
define m = Character("Mary Lisa the Demon Slayer (real)")
define j = Character("James the Jame")
define qm = Character("???")
define p = Character("Patricia the Pratricisnt")
define je = Character("Jennifer the Jennifurt")
image the end = Movie(play="VID20211228WA0001.webm", size=(1920, 1080))

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
    # Intro

    scene black
    blank "You are currently surrounded in a void of darkness."
    blank "You have no idea where you are."
    blank "You hear a distant voice call out to you."
    qm "..."
    qm "{i}Hello?{/i}"
    blank "The voice starts to get gradually louder."
    qm "Wake up"
    blank "You begin to feel like the dark void is moving"
    # scene white
    blank "{b}{i}SLAP{/i}{/b}"
    blank "The dark void disappears as you begin to regain conciousness"
    qm "Finally"
    blank "You see a mysterious figure on top of you.  You cant make out any notable features due to the sheer force of her slap causing your vision to be messed up."
    blank "Get fucked, {b}IDIOT!{/b}"
    qm "You've been knocked out for awhile."
    blank "The mysterious figure gets off of you"
    # scene bedroom
    blank "You look around the room.  It appears to be a bedroom of some sort."
    blank "You proceed to fumble out of the bed and get back on your feet."
    show eileen happy
    blank "You see this mysterious figure in full"
    #first option here
    qm "Seggs?"
    j "Sure"
    scene seggs
    blank "You begin to seggs"
    j "damn, that pussy fire"
    scene seggsrancid
    j "damn, nevermind that pussy rancid"

    # End

    show the end
    m "The End"

    # Make sure to NOT USE RETURN unless its at the end.
    # The game will end if you put return.

    return
