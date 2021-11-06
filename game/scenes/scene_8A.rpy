define callistaVoiceScene8A = "audio/Dubs/J-H/Scene 8/"

label scene_8A:
    scene bg 5
    with dissolve
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.45
    "{i}Callista and Bisma arrived at the Art Convention Building.{/i}"

    show bisma happy right #show bisma happy
    with dissolve

    b "Wow, this place looks way better than I thought."

    #hide bisma
    show callista happy left #show callista happy
    with dissolve

    voice callistaVoiceScene8A+"Scene 8_HJ_1_Final.mp3"
    j "Yeah, this place looks cool. Can’t wait to see the performance."

    #hide callista
    #show bisma normal

    b "Look, the band is coming to the stage."
    b "The performance is about to start. We should take a seat now."

    hide callista #hide bisma
    hide bisma
    with dissolve

    "{i}Callista and Bisma sit next to each other and then the performance starts.{/i}"
    "{i}The place is filled with beautiful sounds and wonderful singing.{/i}"
    "{i}Then the performance ended and almost everyone left.{/i}"

    show bisma energetic right #show bisma energetic
    with dissolve

    b "That was an awesome performance. What do you think?"

    #show bisma energetic at right
    #with move
    #show callista energetic at left
    show callista happy left 

    j "It was really cool. I didn’t regret signing up to the Band Unit."

    b "Hey, let’s go up to the stage and play together."

    show callista thinking left #show callista thinking

    voice callistaVoiceScene8A+"Scene 8_HJ_2_Final.mp3"
    j "But I don’t think we could use the instruments before we fully joined the Unit."

    b "It’ll be fine. The performance is over anyway."

    voice callistaVoiceScene8A+"Scene 8_HJ_3_Final.mp3"
    j "I guess so…"

    b "C’mon, you’re so slow."

    hide bisma #hide bisma
    hide callista #hide callista
    with dissolve

    "{i}Bisma brought Callista to the stage.{/i}"
    "{i}Bisma picked up the guitar and started to play it.{/i}"

    show bisma happy right #show bisma normal at right
    show callista happy left #show callista normal at left
    with dissolve

    b "C’mon, Callista. Play the keyboard for me."

    voice callistaVoiceScene8A+"Scene 8_HJ_4_Final.mp3"
    j "Sure…."

    hide bisma #hide bisma
    hide callista #hide callista
    with dissolve

    "{i}Callista and Bisma plays together until the Band Unit leader disbanded them from the stage.{/i}"

    show bisma energetic right #show bisma happy at right
    show callista happy left #show callista happy at right
    with dissolve

    b "Well, that was fun."
    b "See you tomorrow, Callista."

    j "See you tomorrow too, Bisma."

    hide bisma #hide bisma
    hide callista #hide callista
    with dissolve 

    "{i}Callista went back home, but she felt something wrong inside her heart.{/i}"

    stop music
    return