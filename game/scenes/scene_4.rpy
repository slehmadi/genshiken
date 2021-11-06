define callistaVoiceScene4 = "audio/Dubs/J-H/Scene 4/"
define luckyVoiceScene4 = "audio/Dubs/C/Scene_4_C.mp3"

label scene_4:
    scene black
    with dissolve
    "{i}The Next Day.{/i}"

    scene bg 4
    with dissolve
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45

    "{i}Callista went to her university for the first time and watched the opening ceremony.{/i}"

    pause(.3)

    show callista focused left
    with dissolve

    "{i}It’s now lunch time.{/i}"

    #show callista normal
    #pause(1.0)
    #hide callista
    #show lucky happy
    hide callista
    show lucky happy right

    voice luckyVoiceScene4
    c "Callista, over here!"

    pause .3
    #hide dummyC #hide lucky
    show callista happy left #show callista happy
    with moveinleft

    voice callistaVoiceScene4+"Scene 4_HJ_1_Final.mp3"
    j "Lucky! It’s great to finally meet you again! It’s been ages since we last met."

    hide callista #hide callista
    hide lucky

    "{i}Callista hugs Lucky{/i}"
    pause(1.0)

    show callista happy left
    show lucky normal right
    with dissolve
    pause .3

    c "I’m so glad we could met again. I’m tired of just meeting you through video call."

    j "I’m tired of that too."
    j "Also, thank you for wanting to make my next VTuber model. You really are an artistic person."
    j "BTW, where’s Bisma?"

    b "I’m over here!"

    hide callista #hide callista
    hide lucky #hide lucky
    #show bisma happy

    show bisma happy center
    with dissolve
    "{i}Bisma run towards Callista and Lucky{/i}"
    pause .2

    hide bisma #show lucky surprised
    show lucky surprised right

    c "Bisma, is that really you? I would've never guessed you would look like that."

    #hide dummyC#hide lucky
    show callista happy left

    voice callistaVoiceScene4+"Scene 4_HJ_2_Final.mp3"
    j "Yeah, you look cool."

    hide lucky #hide callista
    show bisma happy right
    with moveinright

    b "Thank you for the compliment."
    b "Glad to finally meet you."

    #show bisma happy at right
    #with move
    #show lucky normal at left
    hide callista
    show lucky normal left

    c "Let’s just eat. We can talk while eating."

    hide bisma
    hide lucky
    with dissolve

    "{i}They sat under the tree and eat their lunch.{/i}"

    show bisma normal right

    b "So, what have you all been doing during the online school?"

    #show bisma normal at right
    #with move
    #show lucky normat at left
    show lucky normal left

    c "Just making illustrations for my best friend here. Other than that, I’m just studying."

    b "How about you, Callista?"

    hide lucky #hide lucky
    show callista happy left

    j "I spent my time streaming as a VTuber."

    show bisma thinking right#show bisma surprised

    b "Really, that’s so cool. What did you stream?"

    j "Games and sometimes I make music."
    j "I’m not that good at both though."

    show bisma energetic right#show bisma energetic

    b "You like music too?"
    b "I have always wanted to make music as a band."

    hide callista #hide callista
    show lucky normal left

    c "Well, that’s great because next on our schedule is the Student Activity Unit Open House. I think there’s a Band Unit there."
    c "Bisma, you could join me there. I’ve always wanted to be a singer. What will you play?"

    #show bisma energetic

    b "The guitar of course. I can only play that instrument."

    c "How about you, Callista? Do you want to join us?"

    hide lucky #hide lucky
    hide bisma #hide bisma
    show callista thinking left

    voice callistaVoiceScene4+"Scene 4_HJ_3_Final.mp3"
    j "I’m not quite sure yet."

    #show dummyJ at left #show callista thinking at left
    #with move
    show lucky normal right

    c "Well there’s still plenty of time to think. I think you’ll be the perfect keyboardist."

    j "I’m pretty sure there are better options for a keyboardist than me."

    hide lucky #hide lucky
    show bisma normal right
    b "I haven’t heard you play, but I’m sure you’re not bad at playing it."
    b "You could improve your skills along the way."

    hide bisma #hide bisma
    show lucky happy right

    c "The three of us will make the perfect band. C’mon, join us."

    j "Let’s just see what the Band Unit looks like, then I’ll think about it again."

    show lucky normal right #show lucky normal

    c "You’re right, we don’t know anything about the Band Unit yet."
    c "Guess we have to wait a few more minutes until the event starts."
    c "Shall we go there now?"

    hide callista #hide callista
    show bisma normal left

    b "Yeah, we should probably go there now."

    hide lucky #hide lucky
    hide bisma #hide bisma
    with dissolve

    "{i}They packed up their lunch and headed to the Art Convention Building.{/i}"

    stop music
    return