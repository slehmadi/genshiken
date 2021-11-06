
label scene_15:
    scene bg 4
    with dissolve

    "{i}Bisma and Callista go together, but suddenly ..{/i}"

    pause(0.5)
    with hpunch

    "{i}..a thief steals Callista’s bag{/i}"
    play music "audio/Musics/6-Intense.mp3" volume 0.45

    show callista mad left
    with dissolve

    j "Thief!"

    #hide callista
    #show bisma normal
    show bisma normal right
    with dissolve

    b "Don't worry, I will catch him."

    hide bisma
    with moveoutright

    "{i}Bisma dashes to the thief across the park.{/i}"

    hide callista
    with moveoutright

    "{i}Callista runs chasing them, but she couldn’t keep up.{/i}"

    show callista focused center
    with dissolve

    j "They are really fast."
    j "Hopefully Bisma can catch the thief."

    hide callista
    with dissolve

    stop music

    "{i}The thief and Bisma are gone for a long time, then Bisma shows up.{/i}"
    "{i}Callista runs to him.{/i}"

    show bisma normal right #show callista happy
    with moveinright
    show callista happy center:
        xzoom -1
    with moveinleft

    j "Bisma! You got my bag back."
    j "Did you catch the thief?"

    #show callista happy at left
    #show bisma normal at right
    show callista happy left 

    b "No, he got away."
    b "Hey, at least I managed to save your bag, right?"

    j "Thank you for your help. How can I repay this?"

    b "Well, I do have an extra ticket to the amusement park next week."
    b "Will you go there with me?"

    j "After your help, of course I would."

    show bisma happy right #show bisma happy

    b "Great then."
    b "So, are we still going or are you just gonna stand here?"

    show callista focused left #show callista normal

    j "Oh right. Yeah, let's go."

    hide callista
    hide bisma

    "{i}Bisma and Callista go together and talk during the walk.{/i}"

    return