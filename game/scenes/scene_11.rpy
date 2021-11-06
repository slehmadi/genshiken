define callistaVoiceScene11 = "audio/Dubs/J-H/Scene 11/"
define kazuoVoiceScene11 = "audio/Dubs/V-W/Scene 11/"

label scene_11:
    scene bg 7 #maybe? dunno
    with dissolve

    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    show lucky normal right #show lucky normal
    with dissolve

    c "Hey, Callista, check your email from me."

    #show lucky normal at right
    #with move
    #show callista normal at left
    show callista focused left 
    with dissolve

    j "Is the new VTuber outfit finished?"

    c "Yes, I hope you liked it."

    j "Wow, you work really fast."
    j "Thank you for doing this for me. I really like the new outfit."

    c "Thank you."
    c "So anyway, I’m gonna go now."
    c "See you later, Callista"

    j "See you later too."

    hide lucky #hide lucky
    with dissolve
    #show callista normal at center

    j "{i}This new outfit is really good. I should ask another person’s opinion.{/i}"

    show callista thinking left #show callista thinking

    voice callistaVoiceScene11+"Scene 11_HJ_1_Final.mp3"
    j "{i}Should I ask Kazuo or just share the new outfit on my Instagram?{/i}"

    stop music
    menu:
        "Just upload it to Instagram.":
            jump scene_11_choice1
        "Ask Kazuo’s opinion first.":
            jump scene_11_choice2

    return

label scene_11_choice1:
    $ Skor += 10
    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    voice callistaVoiceScene11+"Scene 11_HJ_2_Final.mp3"
    j "I should just upload it."

    hide callista
    with dissolve

    "{i}Callista sends the new VTuber outfit to Instagram.{/i}"
    "{i}Bisma instantly commented on it.{/i}"

    # (uhm.... kita tunjukin aja charanya atau biarin aja??)
    #show bisma normal at right

    b "Wow! The outfit looks really great."
    b "I think it really fits you."

    #show callista at left

    j "Thank you for the compliment."

    b "So are you gonna change your streaming model on your next stream?"

    j "Not yet, I think I will use it when the next month starts. I think that’ll be the perfect time."
    j "Okay then, that’s all that I want to ask."

    b "Okay then, see you later."
    b "Bye, Callista!"

    j "Bye, Bisma."

    stop music
    return

label scene_11_choice2:
    $ Skor -= 10
    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    voice callistaVoiceScene11+"Scene 11_HJ_3_Final.mp3"
    j "I should ask Kazuo’s opinion first."

    hide callista

    "{i}Callista sends the new VTuber model to Kazuo.{/i}"

    j "Hi, Kazuo. This is my new VTuber outfit, what do you think?"

    #show kazuo normal at right

    voice kazuoVoiceScene11+"Scene 11_V_1_Final.mp3"
    v "Wow! The outfit looks really great."
    v "I think it really fits you."

    j "Thank you for the compliment."

    voice kazuoVoiceScene11+"Scene 11_V_2_Final.mp3"
    v "So are you gonna change your streaming model on our next stream?"

    j "Not yet, I think I will use it when the next month starts. I think that’ll be the perfect time."
    j "Okay then, that’s all that I want to ask."

    v "Okay then, see you later."

    voice kazuoVoiceScene11+"Scene 11_V_3_Final.mp3"
    v "Bye, Callista!"

    j "Bye, Kazuo."

    stop music
    return

