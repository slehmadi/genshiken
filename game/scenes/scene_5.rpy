define callistaVoiceScene5 = "audio/Dubs/J-H/Scene 5/"
define bismaVoiceScene5 = "audio/Dubs/B/Scene_5_B_Final.mp3"

label scene_5:
    pause 0.1
    scene bg 5
    pause 0.3
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.15

    "*Callista, Lucky, and Bisma arrived at the Art Convention Building*"
    "*The room is filled with different stands from every Student Activity Unit*"
    "*They all walk around multiple times, looking at every Unit*"

    show dummyB neutral at right: #show bisma normal
        xzoom -1

    b "Alright, we have seen about three fourths of the Student Activity Unit here."
    b "What stand should we visit next?"

    #show bisma normal at right
    #with move
    #show callista normat at left
    show dummyJ smile at left

    j "We’ve visited a lot of stands. I think that’s enough for us to visit."

    show dummyC normal #show lucky normal

    c "Yeah. We’ve visited the Art Unit, the Band Unit, The Sports Unit, even other Units that’s pretty weird."
    c "I mean, who wants to join the Pop Culture Enthusiast Unit, right?"

    b "So, you guys are joining the Band Unit, right?"

    c "Yeah, and I think I’ll join the Art Unit too."
    c "How about you, Callista?"

    show dummyJ wonder #show callista thinking

    voice callistaVoiceScene5+"Scene 5_HJ_1_Final.mp3"
    j "I’m still not quite sure."

    c "Well, I have to go to the bathroom now."
    c "You two should just visit other stands while waiting for me."

    hide dummyC #hide lucky
    with dissolve #with dissolve

    "*Lucky goes to the toilet*"

    b "So, Callista, what stand do you wanna visit?"

    voice callistaVoiceScene5+"Scene 5_HJ_2_Final.mp3"
    j "I dunno. Let’s just start walking."

    hide dummyJ #hide callista
    hide dummyB #hide bisma

    "*Bisma and Callista walk across the row of stands*"

    show dummyJ smile at left #show callista normal at left
    show dummyB neutral at right: #show bisma normal at right
        xzoom -1

    b "I heard from Lucky that you sometimes play a keyboard on your streams. Is that correct?"

    voice callistaVoiceScene5+"Scene 5_HJ_3_Final.mp3"
    j "Yeah that’s true. I do that sometimes."

    b "So why don’t you join the Band Unit with us?"

    show dummyJ wonder #show callista thinking

    voice callistaVoiceScene5+"Scene 5_HJ_4_Final.mp3"
    j "I’m still thinking about it."
    j "If no other Unit excites me, then I’ll probably join the Band Unit with you and Lucky"

    b "I’m very sure you belong to the Band Unit."

    show dummyB smile #show bisma happy

    b "Lucky said that your keyboarding skills are amazing."

    show dummyJ smile #show callista normal

    j "Lucky sometimes praises people too much."

    show dummyJ sad #show callista sad

    j "My skills aren’t that great."

    #show bisma energetic

    b "C’mon, have more confidence in yourself."
    b "I’m sure you’re talented at playing the keyboard. you’ll be perfect for the Band unit."

    show dummyJ smile #show callista smile (if exist)

    voice callistaVoiceScene5+"Scene 5_HJ_5_Final.mp3"
    j "Well, if you said so."
    j "Then I will join the Band Unit."

    show dummyB neutral #show bisma normal

    voice bismaVoiceScene5
    b "BTW, Callista. Have you had a boyfriend before?"

    stop music
    menu:
        "Can you guess?":
            jump can_you_guess
        "Why would you ask that":
            jump why_would_you_ask_that

    return

label can_you_guess:
    $ Skor += 10
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.15

    voice callistaVoiceScene5+"Scene 5_HJ_6_Final.mp3"
    j "can you guess?"

    show dummyB confused #show bisma thinking

    b "Let me think."
    b "You have one?"

    #show callista happy

    j "Nope, you’re wrong."
    j "I never even thought about having a boyfriend before."

    show dummyB neutral #show bisma normal

    b "Somehow, that’s not surprising."

    show dummyJ upset #show callista angry

    j "Are you joking with me?"
    j "Well, I’m gonna pick up a few brochures from the Band Unit."

    hide dummyB #hide bisma
    with dissolve
    #show calista normal
    pause 0.3
    show dummyJ wonder at center
    with move
    
    j "*Why did he want to know whether I have a boyfriend or not?*"

    hide dummyJ #hide callista

    "*Callista left to pick up a few brochures and come back to Bisma who’s talking with Lucky*"
    "*After the Open House Unit finishes, they all then split up and went back to each of their home*"

    stop music
    return

label why_would_you_ask_that:
    $ Skor -= 10
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.15

    voice callistaVoiceScene5+"Scene 5_HJ_7_Final.mp3"
    j "Why would you ask that?"

    show dummyB confused #show bisma thinking

    b "Umm…"
    b "I dunno. I just see that you and Lucky are quite close."

    #show callista normal

    j "It’s not quite appropriate to ask that on the first day of meeting someone."
    j "But no, I never had a boyfriend before."
    j "Lucky is just my best friend."

    show dummyB neutral #show bisma normal

    b "I see. You’re a cold type of person."

    show dummyJ upset #show callista angry

    j "I-It’s not like that."
    j "I’m just busy with my job and education."
    j "Also, I’m gonna pick up a few brochures from the Band Unit."

    hide dummyB #hide bisma
    with dissolve
    #show calista normal
    pause 0.3
    show dummyJ wonder at center
    with move

    j "*Why did he want to know whether I have a boyfriend or not?*"

    hide dummyJ #hide callista

    "*Callista left to pick up a few brochures and come back to Bisma who’s talking with Lucky*"
    "*They all then split up and went back to each of their home*"

    stop music
    return