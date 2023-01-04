# generic porn game
cool porn game

# notes for zex
GIT PULL BEFORE EDITING SHIT UNLESS WE'RE IN A CODESPACE.  GIT WONT LET YOU PUSH OTHERWISE AND/OR YOU'LL EDIT SHIT THAT I MIGHT'VE PUT.

GIT COMMIT -M "COMMENT" BEFORE PUSHING.  GIT WONT LET YOU PUSH OTHERWISE.


If you want to make a true/false statement, go to where everything is defined and put it under the current true/false statements.
If you're making choices like questions, make a label named whatever (label (name):), make a menu (menu:), and follow it with text

example:

```
define variable = False
# Capitalization matters here btw.  This is for choices later.


# This is the label you jump back to
label text:
    # This is the choices
    menu:
        # This is the text that appears at the bottom of the screen
        "Choose shit"
        
        # These are the choices.  Make sure the colon is at the end of each one.
        "Choice one":
            "Text"
            # The line below jumps back to the choices
            jump text
        "Choice two":
            # The line below checks to see if "variable" is set to True.  It jumps to else if its not.
            if variable:
                "text"
                jump text
            else
                "text 2"
                # The line below changes "variable" to True.  If you run this again, it'll show "text" instead of "text 2"
                $ variable = True
                jump text
        # The line below will prevent you from using the choice unless "variable" is set to True.
        "Choice three" if variable:
            "mmm pineapple"
            jump text
        
        "I dont wanna choose":
            # The line below jumps to the label below it
            jump text2

# It'll continue with no choices when it jumps to the line below.
label text2:
    "im text"

# Note: If you want characters to speak, define them like this:
# define (something to identify them, replace text and remove brackets) = Character("Name")
#
# you can also define the "variable" in "menu:" so its a temporary variable.  
# Dont do it if it's important to the entire story (Main characters,
# love meters, health, mana, etc.) because its only defined in that menu.
```

# Ideas

Maybe a love meter that's just a number that can be added/subtracted for extra options like sex?

Itll work something like this:
```
define lovemeter = 0

label choices:
    menu:
        "Choose smth idiot"
        
        "Sex":
            # This adds one to "lovemeter"
            $ lovemeter += 1
            jump choices
        "No sex":
            # This removes one to "lovemeter"
            $ lovemeter -= 1
            jump choices
        # This will only allow you to megasex if the lovemeter is greater than or equal to 10
        "Mega sex" if lovemeter >= 10:
            $ lovemeter += 100
            jump choices
        "Nigga sex":
            $ lovemeter -=300
            jump gameover
        "End":
            jump choicesend
            
label choicesend:
    "sex"
    return
label gameover:
    "You're really gonna nigga sex me?  I cant fucking believe this"
    "Game over"
    return
```

# Plot
```
Main Character List:
    James the Jame AKA James
    Mary Lisa the Demon Slayer (real) AKA Mary Lisa the Demon Slayer (fake) AKA Mary
    Patricia the Pratricisnt AKA Pat
    Jennifer the Jennifurt AKA Fer
    Guest Star Bunger AKA Pope Bunger
    
Places:
    Hadleigh (Village)
    Orrinshire (City)
    Mountmend (Village)
    Wolfpine (Abandoned Village)
    Aramoor (Village, overran by Orcs)
    Whitebridge (Bridge dividing the two islands, captured by the Humans)
    Peltragow (Village, owned by Orcs)
    Oakheart (City, owned by Orcs)
    Putlochry (Village, overran by Elves)
    Furness (Village, overran by Elves)
```

Story in order of events:

The main character is James the Jame.  He wakes up in a house he doesn't know by a person he doesn't know.  In reality, he just forgot everything about himself, his past, etc.  This is due to an attack that was executed on him by a group of succubi.  His "party member", Mary Lisa the Demon Slayer (real), "saved him" from the succubi and brought him to his house in Hadleigh, banking on the fact that he forgot everything by saying its her house.  Mary has effectively hit em' with that good succ, wrung him dry knowing that he'd forget everything, and is now faking a story that James doesn't know to keep sexing him FOR FREE while taking all his shit.

Story in full:

The year is 728.
