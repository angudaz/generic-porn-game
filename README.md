# generic-porn-game
cool porn game

# notes for zex
If you want to make a true/false statement, go to where everything is defined and put it under the current true/false statements.
If you're making choices like questions, make a label named whatever (label (name):), make a menu (menu:), and follow it with text

example:

```
define variable = False
Capitalization matters here btw


This is the label you jump back to
label text:
    This is the choices
    menu:
        This is the text that appears at the bottom of the screen
        "Choose shit"
        
        These are the choices.  Make sure the colon is at the end of each one.
        "Choice one":
            "Text"
            The line below jumps back to the choices
            jump text
        "Choice two":
            The line below checks to see if "variable" is set to True.  It jumps to else if its not.
            if variable:
                "text"
                jump text
            else
                "text 2"
                The line below changes "variable" to True.  If you run this again, it'll show "text" instead of "text 2"
                $ variable = True
                jump text
        The line below will prevent you from using the choice unless "variable" is set to True.
        "Choice three" if variable:
            "mmm pineapple"
            jump text
        
        "I dont wanna choose":
            The line below jumps to the label below it
            jump text2

It'll continue with no choices when it jumps to the line below.
label text2:
    "im text"
```

