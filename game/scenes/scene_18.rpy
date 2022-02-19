define callistaVoiceScene18 = "audio/Dubs/J-H/Scene 18/"
define luckyVoiceScene18 = "audio/Dubs/C/Scene_18_C.mp3"

label scene_18:
    scene bg 3
    with dissolve

    "{i}Callista calls Lucky again.{/i}"
    
    #show callista normal
    #pause(0.3)
    #show callista normal at left
    #show lucky normal at right

    show lucky normal right 
    show callista focused left 
    with dissolve

    c "Hey, I watched your stream and you looked unfocused."
    c "Are you still thinking about what I said?"

    show callista sad left 

    j "Yeah."
    j "I’m very torn about Bisma and Kazuo."
    j "Both of them are very nice to me, but I have done bad things to them too."
    j "I don’t know if they will like me or not because of my wrongdoing."

    c "Hey, don’t worry."
    c "Don’t dwell on your past self."

    show lucky happy right 

    c "I’ve seen you change during these past few days and It’s been impacting you for the better."

    show callista thinking left 

    j "Wait, really?"

    play music "audio/Musics/2-Kamar_Easy Feeling.mp3"

    show lucky normal right 

    c "Yes. I see that you’re more comfortable in public now and your skills are increasing rapidly."
    c "What you’ve been through these past few days, have made you a better person."

    show callista happy left 

    j "Thank you for the compliment."

    show callista thinking left 

    j "I’m so focused on Bisma and Kazuo that I didn’t notice that."

    c "So whether Bisma or Kazuo like you or not, you’ve been a better person and that’s great."
    c "Now that your past has made you a better person, you have to choose a future that will make you a better person too."
    c "So, choose carefully on {b}who{/b} you’re gonna go with."

    show callista happy left 

    j "Thank you so much Lucky for the words."
    j "You’ve been a great help for my problems."
    j "You really are my best— "

    #play sound "doorsbell.mp3"
    hide callista
    hide lucky
    with dissolve

    "{i}Callista’s doorbell rings.{/i}"

    show callista focused left
    show lucky normal right
    with dissolve

    c "Why is your doorbell ringing?"

    j "I don’t know."
    j "I think I saw a courier on my front door."
    j "Hold on a minute."

    hide callista
    hide lucky
    with dissolve

    "{i}Callista opens the door and take a package from the courier.{/i}"

    show callista focused left
    show lucky normal right
    with dissolve

    c "Did you just get a package in the dead of night?"

    j "Yeah, that’s weird."
    j "It says here that the package is from Kazuo."

    c "Really? Open it."
    c "What’s inside?"

    hide callista
    hide lucky
    with dissolve

    "{i}Callista opens the package.{/i}"

    show callista focused left
    show lucky normal right
    with dissolve

    j "It’s a letter from him."
    j "He said that he wanted to meet me at the amusement park next week."
    j "There’s also a picture of the tickets."

    c "But isn’t Kazuo far from us?"

    j "He did say that he will come to my city next week."

    c "So will you go with him?"

    show callista thinking left 

    j "I’m not sure."

    c "Why?"

    j "Bisma also invited me to come to the same amusement park at the exact same time."

    c "Well, you have to sacrifice one, there’s no other option."
    c "It’s your final chance now."

    stop music

    voice luckyVoiceScene18
    c "Do you want to go with Bisma or Kazuo?"

    menu:
        "Go to the amusement park with Bisma.":
            jump scene_18_choice1
        "Go to the amusement park with Kazuo.":
            jump scene_18_choice2

    return

label scene_18_choice1:
    $ Skor += 30
    $ choose_with = "B"

    voice callistaVoiceScene18+"Scene 18_HJ_1_Final.mp3"
    j "I guess...I will go with Bisma."

    c "Well you have chosen."
    c "Let’s hope that this will be the best for your future."
    c "Okay, I’m going to sleep and you should too."
    c "Bye, Callista."

    show callista focused left 

    j "Bye, Lucky."

    hide lucky
    with dissolve

    "{i}Lucky ends Callista’s call.{/i}"

    show callista thinking left 

    j "{i}Have I really made the correct choice?{/i}"
    j "I shouldn’t think about it much and just go to sleep."

    return

label scene_18_choice2:
    $ Skor -= 30
    $ choose_with = "V"

    voice callistaVoiceScene18+"Scene 18_HJ_2_Final.mp3"
    j "I guess...I will go with Kazuo."

    c "Well you have chosen."
    c "Let’s hope that this will be the best for your future."
    c "Okay, I’m going to sleep and you should too."
    c "Bye, Callista."

    show callista focused left

    j "Bye, Lucky."

    hide lucky
    with dissolve

    "{i}Lucky ends Callista’s call.{/i}"

    show callista thinking left 

    j "{i}Have I really made the correct choice?{/i}"
    j "I shouldn’t think about it much and just go to sleep."

    scene black
    with dissolve

    "{i}Next Weekend..{/i}"

    return