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
# j is for line 119, stick with jf for the rest of the game.
define j = Character("James")
define jf = Character("James the Jame")
define qm = Character("???")
define p = Character("Patricia the Pratricisnt")
define je = Character("Jennifer the Jennifurt")
image the end = Movie(play="VID20211228WA0001.webm", size=(1920, 1080))
#these last two are for options1. refer to line 73
define known_name = False
define memory =  False

#You boot the game
label splashscreen:
    scene black
    with Pause(1)

    show text "Random Retards on the Internet presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    play sound [ "<silence 2.9>", "audio/vineboom.mp3" ]
    with Pause(3)

    show text "{b}Generic Porn Game{/b}"
    with Pause(2)

    hide text with dissolve
    stop sound
    with Pause(2)

    return

#You start the game
label start:
    # Intro
    stop audio
    stop music
    stop sound
    # need to add these cause too lz to find out what channel main menu music is on
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
    # scene bedroom (add blur effect)
    blank "You look around the room.  It appears to be a bedroom of some sort."
    play sound "audio/stumbleoutofbed.mp3" noloop
    blank "You proceed to fumble out of the bed and get back on your feet as you regain your vision."
    # scene bedroom (no blur)
    show eileen happy
    blank "You see this mysterious figure in full"
    m "My name is Mary Lisa the Demon Slayer, but you can call me Mary"
    qm "Hello, Mary."
    #first option here
    label options1:
        menu:
        # 8 spaces because its a diff branch
            "Choose a question"

        # Colon and more spaces after cause its a diff branch (again). 12 for question, 16 for known_name if/else, 20 for dialogue)
        # Ill add images later -josh
            "Saul Goodman":
                jump saulgoodmanend
            "Where am I?":
                if known_name:
                    jf "Where am I?"
                    m "You are currently in my house.  Be glad that I saved you from the situation you were in."
                    jump options1
                else:
                    qm "Where am I?"
                    m "You are currently in my house.  Be glad that I saved you from the situation you were in."
                    jump options1
            "What happened?":
                if known_name:
                    jf "What happened?"
                    m "You were being attacked by succubi."
                    m "They were milking you dry, so I decided to nuke them."
                    m "Dont you remember?"
                    $ memory = True
                    jump options1
                else:
                    qm "What happened?"
                    m "You were being attacked by succubi."
                    m "They were milking you dry, so I decided to nuke them."
                    m "Dont you remember?"
                    $ memory = True
                    jump options1
            "Who am I?":
                if known_name:
                    jf "Who am I?"
                    m "I just told you, retard."
                    jump options1
                else:
                    qm "Who am I?"
                    m "I believe you go by James, but your full name is James the Jame"
                    $ known_name = True
                    m "Did that attack really fuck you up that hard?"
                    jf "I guess so."
                    m "Do you remember anything else?"
                    jf "..."
                    jf "Not really, no."
                    m "{i}Yikes.{/i}"
                    jump options1
            "Who are you to me?" if memory:
                if known_name:
                    jf "Who am you to me?"
                    m "Wow.  Cant believe you dont even remember your own party member."
                    jf "Sorry, Im just trying to remember stuff right now."
                    jump options1
                else:
                    qm "Who am you to me?"
                    m "Wow.  Cant believe you dont even remember your own party member."
                    qm "Sorry, Im just trying to remember stuff right now."
                    jump options1
            "No other questions":
                if known_name:
                    jf "I believe I dont have any other questions."
                    m "Okay.  In that case..."
                    jump options1end
                else:
                    qm "I believe I dont have any other questions."
                    m "Ok, James."
                    j "Wait... Thats my name?"
                    m "Well, thats what you go by.  Your full name is James the Jame."
                    m "..."
                    m "Did you not know that?"
                    jf "No."
                    m "Well, maybe you should've asked about it."
                    m "..."
                    m "Anyways..."
                    jump options1end
label options1end:
    qm "Seggs?"
    j "Sure"
    scene seggs
    blank "You begin to seggs"
    j "damn, that pussy fire"
    scene seggsrancid
    j "damn, nevermind that pussy rancid"

label saulgoodmanend:
    show the end
    blank "You've successfully destroyed everyone in the game.  GGWP"
    return
