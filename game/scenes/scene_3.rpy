
label scene_3:
    scene
    #show callista normal
    "*Callista checks her phone*"

    #show callista normal at left
    #with move
    #pause(2.0)
    #show lucky happy at right
    #with moveIn

    c "Looking forward to meeting you all tomorrow!"
    c "Callista, remember what I told you about Bisma?"

    j "Of course."

    #hide callista
    #hide lucky
    #show bisma confused

    b "What did you two say about me?"

    #hide bisma
    #show lucky normal

    c "It’s nothing."
    c "Callista, if you’re still worried, stay away from Bisma and stay near me."

    #hide lucky
    #show bisma confused

    b "Seriously, what did you say about me? Am I scary?"

    #hide bisma
    #show callista laugh at left
    #show lucky laugh at right

    j "Hahaha"

    c "Of course not, Bisma. We’re just joking with you."
    
    #hide lucky
    #show lucky normal at center

    c "BTW, looking at the schedule for tomorrow, there's free time after the opening ceremony."
    c "I think we should eat lunch together."

    #show lucky normal at left
    #with move
    #show bisma normal at right
    #with moveIn

    b "Eat at the canteen?"

    c "The canteen will be too busy. Let’s eat at the park behind the university."

    b "Sounds good. Do you agree, Callista?"

    #hide lucky
    #show callista normal at left
    #with moveIn

    j "Of course."

    b "Guess it’ll be pretty awkward for me. You two have met each other and you haven’t met me directly."

    #show bisma happy
    b "Well, I’m looking forward to meeting you all."

    #show callista happy
    j "Looking forward to meet you too \\\^o^/ "

    #hide callista
    #show lucky
    #with moveIn

    c "Anyway, I’m going to sleep."
    c "Zzzzz"

    b "Guess I’m gonna sleep too."
    b "Zzzzz"

    scene
    "*Callista turns off her phone*"

    j "*I guess tomorrow will be a big day for me. I’m finally able to go to university again.*"
    j "*Am I ready to spend time normally again? To meet friends that I haven’t really known well?*"
    j "*I’m glad I know Lucky, he always help me find new friends. Without him, I won’t even know Bisma.*"
    j "*Hope tomorrow goes well.*"

    return