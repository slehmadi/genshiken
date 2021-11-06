define callistaVoiceScene5 = "audio/Dubs/J-H/Scene 5/"
define bismaVoiceScene5 = "audio/Dubs/B/Scene_5_B_Final.mp3"

label scene_5:
    pause 0.1
    scene bg 5
    with dissolve

    pause 0.3
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.45

    "{i}Callista, Lucky, and Bisma arrived at the Art Convention Building.{/i}"
    "{i}The room is filled with different stands from every Student Activity Unit.{/i}"
    "{i}They all walk around multiple times, looking at every Unit.{/i}"

    show bisma normal right
    with dissolve

    b "Alright, we have seen about three fourths of the Student Activity Unit here."
    b "What stand should we visit next?"

    #show bisma normal at right
    #with move
    #show callista normat at left
    show callista focused left
    with dissolve

    j "We’ve visited a lot of stands. I think that’s enough for us to visit."

    hide bisma
    show lucky normal right #show lucky normal

    c "Yeah. We’ve visited the Art Unit, the Band Unit, The Sports Unit, even other Units that’s pretty weird."
    c "I mean, who wants to join the Pop Culture Enthusiast Unit, right?"

    hide callista
    show bisma normal left

    b "So, you guys are joining the Band Unit, right?"

    c "Yeah, and I think I’ll join the Art Unit too."
    c "How about you, Callista?"

    hide bisma
    show callista thinking left #show callista thinking

    voice callistaVoiceScene5+"Scene 5_HJ_1_Final.mp3"
    j "I’m still not quite sure."

    c "Well, I have to go to the bathroom now."
    c "You two should just visit other stands while waiting for me."

    hide lucky #hide lucky
    with dissolve #with dissolve

    "{i}Lucky goes to the toilet{/i}"

    show bisma normal right

    b "So, Callista, what stand do you wanna visit?"

    voice callistaVoiceScene5+"Scene 5_HJ_2_Final.mp3"
    j "I dunno. Let’s just start walking."

    hide callista #hide callista
    hide bisma #hide bisma
    with dissolve

    "{i}Bisma and Callista walk across the row of stands{/i}"

    show callista focused left #show callista normal at left
    show bisma normal right #show bisma normal at right
    with dissolve

    b "I heard from Lucky that you sometimes play a keyboard on your streams. Is that correct?"

    voice callistaVoiceScene5+"Scene 5_HJ_3_Final.mp3"
    j "Yeah that’s true. I do that sometimes."

    b "So why don’t you join the Band Unit with us?"

    show callista thinking left #show callista thinking

    voice callistaVoiceScene5+"Scene 5_HJ_4_Final.mp3"
    j "I’m still thinking about it."
    j "If no other Unit excites me, then I’ll probably join the Band Unit with you and Lucky"

    b "I’m very sure you belong to the Band Unit."

    show bisma happy right #show bisma happy

    b "Lucky said that your keyboarding skills are amazing."

    show callista focused left #show callista normal

    j "Lucky sometimes praises people too much."

    show callista sad left #show callista sad

    j "My skills aren’t that great."

    show bisma energetic right #show bisma energetic

    b "C’mon, have more confidence in yourself."
    b "I’m sure you’re talented at playing the keyboard. you’ll be perfect for the Band unit."

    show callista happy left #show callista smile (if exist)

    voice callistaVoiceScene5+"Scene 5_HJ_5_Final.mp3"
    j "Well, if you said so."
    j "Then I will join the Band Unit."

    show bisma smirk right #show bisma normal

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
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.45

    voice callistaVoiceScene5+"Scene 5_HJ_6_Final.mp3"
    j "can you guess?"

    show bisma thinking right #show bisma thinking

    b "Let me think."
    b "You have one?"

    #show callista happy

    j "Nope, you’re wrong."
    j "I never even thought about having a boyfriend before."

    show bisma normal right #show bisma normal

    b "Somehow, that’s not surprising."

    show callista mad left #show callista angry

    j "Are you joking with me?"

    show callista mad left:
        xzoom -1

    j "Well, I’m gonna pick up a few brochures from the Band Unit."

    hide bisma #hide bisma
    with moveoutright
    show callista mad center
    with move
    #show calista normal
    pause 0.3
    show callista thinking center
    
    j "{i}Why did he want to know whether I have a boyfriend or not?{/i}"

    hide callista #hide callista

    "{i}Callista left to pick up a few brochures and come back to Bisma who’s talking with Lucky.{/i}"
    "{i}After the Open House Unit finishes, they all then split up and went back to each of their home.{/i}"

    stop music
    return

label why_would_you_ask_that:
    $ Skor -= 10
    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.45

    voice callistaVoiceScene5+"Scene 5_HJ_7_Final.mp3"
    j "Why would you ask that?"

    show bisma thinking right #show bisma thinking

    b "Umm…"
    b "I dunno. I just see that you and Lucky are quite close."

    show callista focused left #show callista normal

    j "It’s not quite appropriate to ask that on the first day of meeting someone."
    j "But no, I never had a boyfriend before."
    j "Lucky is just my best friend."

    show bisma normal right #show bisma normal

    b "I see. You’re a cold type of person."

    show callista mad left #show callista angry

    j "I-It’s not like that."
    j "I’m just busy with my job and education."

    show callista mad left:
        xzoom -1

    j "Also, I’m gonna pick up a few brochures from the Band Unit."

    hide bisma #hide bisma
    with moveoutright
    show callista mad center
    with move
    #show calista normal
    pause 0.3
    show callista thinking center

    j "{i}Why did he want to know whether I have a boyfriend or not?{/i}"

    hide callista #hide callista

    "{i}Callista left to pick up a few brochures and come back to Bisma who’s talking with Lucky.{/i}"
    "{i}They all then split up and went back to each of their home.{/i}"

    stop music
    return