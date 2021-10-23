
label scene_15:
    scene bg road

    "*Bisma and Callista go together, but suddenly ..*"

    pause(0.5)
    with hpunch

    "*..a thief steals Callista’s bag*"

    #show callista angry

    j "Thief!"

    #hide callista
    #show bisma normal

    b "Don't worry, I will catch him."

    #hide bisma

    "*Bisma dashes to the thief across the park*"
    "*Callista runs chasing them, but she couldn’t keep up*"

    #show callista normal

    j "They are really fast."
    j "Hopefully Bisma can catch the thief."

    #hide callista

    "*The thief and Bisma are gone for a long time, then Bisma shows up*"
    "*Callista runs to him*"

    #show callista happy

    j "Bisma! You got my bag back."
    j "Did you catch the thief?"

    #show callista happy at left
    #show bisma normal at right

    b "No, he got away."
    b "Hey, at least I managed to save your bag, right?"

    j "Thank you for your help. How can I repay this?"

    b "Well, I do have an extra ticket to the amusement park next week."
    b "Will you go there with me?"

    j "After your help, of course I would."

    #show bisma happy

    b "Great then."
    b "So, are we still going or are you just gonna stand here?"

    #show callista normal

    j "Oh right. Yeah, let's go."

    #hide callista
    #hide bisma

    "*Bisma and Callista go together and talk during the walk*"

    return

    return