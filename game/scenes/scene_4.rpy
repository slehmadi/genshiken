define callistaVoiceScene4 = "audio/Dubs/J-H/Scene 4/"
define luckyVoiceScene4 = "audio/Dubs/C/Scene_4_C.mp3"

label scene_4:
    scene black
    "The Next Day"

    scene bg 4
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.15

    "*Callista went to her university for the first time and watched the opening ceremony.*"

    pause(1.0)

    "*It’s now lunch time*"

    #show callista normal
    #pause(1.0)
    #hide callista
    show dummyC happy #show lucky happy

    voice luckyVoiceScene4
    c "Callista, over here!"

    hide dummyC #hide lucky
    show dummyJ smile #show callista happy

    voice callistaVoiceScene4+"Scene 4_HJ_1_Final.mp3"
    j "Lucky! It’s great to finally meet you again! It’s been ages since we last met."

    hide dummyJ #hide callista

    "*Callista hugs Lucky*"
    pause(1.0)

    show dummyJ smile at left #show callista normal at left
    show dummyC normal at right #show lucky normal at right
    pause .3

    c "I’m so glad we could met again. I’m tired of just meeting you through video call."

    j "I’m tired of that too."
    j "Also, thank you for wanting to make my next VTuber model. You really are an artistic person."
    j "BTW, where’s Bisma?"

    b "I’m over here!"

    hide dummyJ #hide callista
    hide dummyC #hide lucky
    show dummyB smile #show bisma happy
    pause .5

    "*Bisma run towards Callista and Lucky*"

    hide dummyB #show lucky surprised
    show dummyC surprised

    c "Bisma, is that really you? I would've never guessed you would look like that."

    hide dummyC#hide lucky
    show dummyJ smile #show callista happy

    voice callistaVoiceScene4+"Scene 4_HJ_2_Final.mp3"
    j "Yeah, you look cool."

    hide dummyJ#hide callista
    show dummyB smile at right#show bisma happy

    b "Thank you for the compliment."
    b "Glad to finally meet you."

    #show bisma happy at right
    #with move
    #show lucky normal at left
    show dummyC normal at left

    c "Let’s just eat. We can talk while eating."

    hide dummyB
    hide dummyC

    "*They sat under the tree and eat their lunch*"

    show dummyB neutral at right#show bisma normal

    b "So, what have you all been doing during the online school?"

    #show bisma normal at right
    #with move
    #show lucky normat at left
    show dummyC normal at left

    c "Just making illustrations for my best friend here. Other than that, I’m just studying."

    b "How about you, Callista?"

    hide dummyC #hide lucky
    show dummyJ smile at left #show callista at left

    j "I spent my time streaming as a VTuber."

    #show bisma surprised

    b "Really, that’s so cool. What did you stream?"

    j "Games and sometimes I make music."
    j "I’m not that good at both though."

    show dummyB smile #show bisma energetic

    b "You like music too?"
    b "I have always wanted to make music as a band."

    hide dummyJ #hide callista
    show dummyC normal at left #show lucky normal at left

    c "Well, that’s great because next on our schedule is the Student Activity Unit Open House. I think there’s a Band Unit there."
    c "Bisma, you could join me there. I’ve always wanted to be a singer. What will you play?"

    #show bisma energetic

    b "The guitar of course. I can only play that instrument."

    c "How about you, Callista? Do you want to join us?"

    hide dummyC #hide lucky
    hide dummyB #hide bisma
    show dummyJ wonder #show callista thinking

    voice callistaVoiceScene4+"Scene 4_HJ_3_Final.mp3"
    j "I’m not quite sure yet."

    show dummyJ at left #show callista thinking at left
    #with move
    show dummyC normal at right #show lucky normal at right

    c "Well there’s still plenty of time to think. I think you’ll be the perfect keyboardist."

    j "I’m pretty sure there are better options for a keyboardist than me."

    hide dummyC #hide lucky
    show dummyB neutral at right #show bisma normal at right

    b "I haven’t heard you play, but I’m sure you’re not bad at playing it."
    b "You could improve your skills along the way."

    hide dummyB #hide bisma
    show dummyC happy at right #show lucky happy at right

    c "The three of us will make the perfect band. C’mon, join us."

    j "Let’s just see what the Band Unit looks like, then I’ll think about it again."

    show dummyC normal #show lucky normal

    c "You’re right, we don’t know anything about the Band Unit yet."
    c "Guess we have to wait a few more minutes until the event starts."
    c "Shall we go there now?"

    hide dummyJ #hide callista
    show dummyB neutral at left #show bisma normal at left

    b "Yeah, we should probably go there now."

    hide dummyC #hide lucky
    hide dummyB #hide bisma

    "*They packed up their lunch and headed to the Art Convention Building*"

    stop music
    return