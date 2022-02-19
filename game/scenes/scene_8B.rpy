define callistaVoiceScene8B = "audio/Dubs/J-H/Scene 8/"
define kazuoVoiceScene8B = "audio/Dubs/V-W/Scene 8/"

label scene_8B:
    scene bg 2
    with dissolve 

    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45
    "{i}Callista went back to home and quickly chat with Kazuo{/i}"

    play sound "audio/Sound Effects/sfx3.mp3"

    show callista focused left #show callista normal
    with dissolve

    voice callistaVoiceScene8B+"Scene 8_HJ_5_Final.mp3"
    j "Sorry I didn’t get to accept your offer earlier."

    #show callista normal at left
    #with move
    #show kazuo normal at right
    show kazuo focused right 
    with dissolve

    v "It’s okay, there’s still time before the stream starts."
    v "College must have been so busy that you forgot to answer my offer."

    show callista sad left #show callista sad

    j "It’s not that busy. It’s just that I felt overwhelmed by the sudden change of lifestyle."

    #show kazuo laugh

    voice kazuoVoiceScene8B+"Scene 8B_V_1_Final.mp3"
    v "Hey, at least it’s better than online school, right?"

    show callista focused left #show callista normal

    voice callistaVoiceScene8B+"Scene 8_HJ_6_Final.mp3"
    j "You’re right. I did enjoy the first time I set foot in the university."

    #show kazuo normal

    voice kazuoVoiceScene8B+"Scene 8B_V_2_Final.mp3"
    v "Well, would you look at the time?"
    v "It’s almost time for us to start streaming."

    hide kazuo #hide kazuo
    hide callista #hide callista
    with dissolve 

    "{i}Callista uses her VTuber model.{/i}"

    show hazu happy left #show hazu happy at left
    show kazuo focused right #show kazuo normal at right
    with dissolve

    h "You’re right. Hope this stream went well."
    h "I’m gonna start the stream now."

    #hide hazu
    hide hazu
    hide kazuo
    with dissolve

    "{i}Hazu-Chan and Kazuo went on to play a lot of games in their stream.{/i}"
    "{i}They both seems happy throughout the whole stream.{/i}"
    "{i}They have been playing for hours and the stream has ended.{/i}"

    show callista focused left #show callista normal at left
    show kazuo focused right #show kazuo happy at right

    voice kazuoVoiceScene8B+"Scene 8B_V_3_Final.mp3"
    v "Wow, that’s a great stream today."
    v "It might be our best stream yet."

    show callista happy left #show callista happy

    voice callistaVoiceScene8B+"Scene 8_HJ_6_Final.mp3"
    j "You’re right."
    j "We won so many games in that stream."

    v "Well, I have been enjoying this stream."
    v "Hope that I could collab with you again in the near future."

    j " I would love to collab with you again."
    
    v "It’s already late, so I have to go."
    v "Bye, Callista!"

    voice callistaVoiceScene8B+"Scene 8_HJ_7_Final.mp3"
    j "Bye, kazuo!"

    play sound "audio/Sound Effects/sfx4.mp3"
    hide kazuo #hide kazuo
    hide callista #hide callista
    with dissolve

    "{i}Callista closed her chat with Kazuo happily, but she felt something wrong inside her heart.{/i}"

    stop music 
    return