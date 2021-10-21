
label scene_3:
    scene bg bedroom: #scene bg phone (?)
        zoom 0.9
    pause(1.0)

    show dummyJ wonder at left#show callista normal at left
    with dissolve #with move

    "*Callista checks her phone*"

    show dummyC happy at right: #show lucky happy at right
        xalign 0.9
    with dissolve #with moveIn

    c "Looking forward to meeting you all tomorrow!"
    c "Callista, remember what I told you about Bisma?"

    j "Of course."

    hide dummyJ #hide callista
    hide dummyC #hide lucky
    show dummyB confused #show bisma confused

    b "What did you two say about me?"

    hide dummyB #hide bisma
    show dummyC normal #show lucky normal

    c "It’s nothing."
    c "Callista, if you’re still worried, stay away from Bisma and stay near me."

    hide dummyC #hide lucky
    show dummyB confused #show bisma confused

    b "Seriously, what did you say about me? Am I scary?"

    hide dummyB #hide bisma
    show dummyJ smile at left #show callista laugh at left
    show dummyC happy at right: #show lucky laugh at right
        xalign 0.9

    j "Hahaha"

    c "Of course not, Bisma. We’re just joking with you."
    
    hide dummyJ #hide lucky
    show dummyC normal at center #show lucky normal at center
    with move 

    c "BTW, looking at the schedule for tomorrow, there's free time after the opening ceremony."
    c "I think we should eat lunch together."

    show dummyC normal at left #show lucky normal at left
    with move #with move
    show dummyB neutral at right #show bisma normal at right
    #with moveIn

    b "Eat at the canteen?"

    c "The canteen will be too busy. Let’s eat at the park behind the university."

    b "Sounds good. Do you agree, Callista?"

    hide dummyC #hide lucky
    show dummyJ wonder at left #show callista normal at left
    #with moveIn

    j "Of course."

    b "Guess it’ll be pretty awkward for me. You two have met each other and you haven’t met me directly."

    show dummyB smile #show bisma happy
    b "Well, I’m looking forward to meeting you all."

    show dummyJ smile #show callista happy
    j "Looking forward to meet you too \\\^o^/ "

    hide dummyJ #hide callista
    show dummyC normal at left #show lucky
    #with moveIn

    c "Anyway, I’m going to sleep."
    c "Zzzzz"

    b "Guess I’m gonna sleep too."
    b "Zzzzz"

    scene bg bedroom:
        zoom 0.9
    "*Callista turns off her phone*"

    show dummyJ wonder
    j "*I guess tomorrow will be a big day for me. I’m finally able to go to university again.*"
    j "*Am I ready to spend time normally again? To meet friends that I haven’t really known well?*"
    j "*I’m glad I know Lucky, he always help me find new friends. Without him, I won’t even know Bisma.*"
    j "*Hope tomorrow goes well.*"

    return