define callistaVoiceScene6 = "audio/Dubs/J-H/Scene 6/"
define kazuoVoiceScene6 = "audio/Dubs/V-W/Scene 6/"

label scene_6:
    scene black
    with dissolve
    "{i}Later That Night.{/i}"

    scene bg 2
    with dissolve
    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45
    play sound "audio/Sound Effects/sfx3.mp3"
    "{i}Callista chats with Kazuo.{/i}"

    #show kazuo normal
    voice kazuoVoiceScene6+"Scene 6_V_1_Final.mp3"
    v "So, how’s the first day?"

    #show kazuo normal at right
    #with move
    #show callista happy at left

    j "It’s fun and exciting, but it is a little more crowded than what I hoped it to be."
    j "Overall, It’s great to finally meet my friends again."

    v "Who did you meet?"

    j "You know, Lucky, my best friend, my VTuber model illustrator."
    j "Also, I finally met with Bisma, my college friend during online school."

    v "What is he like?"

    #show callista normal

    j "Doesn’t look bad, very energetic, and fun."
    j "We went to the Student Activity Unit Open House and signed up with Lucky to the Band Unit."

    v "I’m sure that will be fun. But, one question." 
    v "Is Bisma your type? People who play in a band usually give that \“handsome guy\” aura." 
    
    voice kazuoVoiceScene6+"Scene 6_V_2_Final.mp3"
    v "Do you find him attractive?"

    stop music
    menu:
        "Maybe….":
            jump maybe
        "Not at all.":
            jump not_at_all

    return

label maybe:
    $ Skor += 10
    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    voice callistaVoiceScene6+"Scene 6_HJ_1_Final.mp3"
    j "Maybe…."

    #show callista happy
    pause(1.0)
    voice kazuoVoiceScene6+"Scene 6_V_3_Final.mp3"
    v "Huh, interesting."

    #show callista normal
    voice callistaVoiceScene6+"Scene 6_HJ_2_Final.mp3"
    j "What? Are you jealous?"

    v "Not at all."
    v "BTW, do you want to collab again tomorrow?"

    #show callista thinking

    voice callistaVoiceScene6+"Scene 6_HJ_3_Final.mp3"
    j "I dunno. The schedule for tomorrow’s college is not set yet."
    j "I’ll think about it okay."

    v "Okay then, good night. Have a good sleep."

    #show callista normal

    j "You too."

    #hide kazuo

    "*Callista ends their call*"

    j "Guess I better sleep to prepare myself for tomorrow."

    stop music
    return

label not_at_all:
    $ Skor -= 10
    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    voice callistaVoiceScene6+"Scene 6_HJ_4_Final.mp3"
    j "Not at all."

    voice kazuoVoiceScene6+"Scene 6_V_4_Final.mp3"
    v "Well, that’s a surprise."

    #show callista angry
    voice callistaVoiceScene6+"Scene 6_HJ_5_Final.mp3"
    j "What? Do you think just because I said someone is handsome, I automatically liked him?"

    voice kazuoVoiceScene6+"Scene 6_V_5_Final.mp3"
    v "No, you got it all wrong."
    v "I just wanted to know so I can set my schedule to not mess too much with yours."
    v "BTW, do you want to collab again tomorrow?"

    #show callista thinking

    j "I dunno. The schedule for tomorrow’s college is not set yet."
    j "I’ll think about it okay."

    v "Okay then, good night. Have a good sleep."

    j "You too."

    #hide kazuo

    "*Callista ends their call*"

    #show callista tired
    j "Guess I better sleep to prepare myself for tomorrow."

    stop music
    return