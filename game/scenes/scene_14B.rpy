define callistaVoiceScene14B = "audio/Dubs/J-H/Scene 12/"

label scene_14B:
    scene black
    with dissolve
    "{i}Weekend..{/i}"

    scene bg 4
    with dissolve

    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45

    "{i}Callista is walking through the university's park.{/i}"

    show callista tired center #show callista tired
    with dissolve

    j "College is pretty tiring today. I have a lot of tiresome homework, especially the lab report."
    j "Maybe I could get fresh air for a bit then get to work."

    hide callista #hide callista
    with dissolve

    "{i}Callista sees a person on the other side of the park.{/i}"

    stop music
    show callista focused center #show callista
    with dissolve

    j "{i}Isn’t that Bisma?{/i}"

    hide callista
    with dissolve

    "{i}Bisma notices Callista, then Callista come to him{/i}"

    show bisma sad right #show bisma sad
    with dissolve

    b "Hi, Callista. What are you doing here?"

    #show bisma sad at right
    #show callista normal at left
    show callista focused left 
    with moveinleft

    j "I was just taking a whiff of fresh air, but since you’re here, I want to say something."

    show bisma normal right #show bisma normal

    b "If it’s about the Band Unit assignment, then forget about it."

    j "Look, I’m really sorry about that. It’s my fault."

    show bisma sad right #show bisma sad

    b "It’s okay. Too bad I and Lucky couldn’t finish it in time."

    j "It’s all my fault. I should’ve come to help you."

    b "It’s not important anymore. We still got accepted at the Band Unit."
    b "So, let’s forget about that assignment."

    j "{i}He looks really sad.{/i}"

    voice callistaVoiceScene14B+"Scene 14_HJ_3_Final.mp3"
    j "{i}Should I do something to cheer him up?{/i}"

    menu:
        "Offer him to eat together at a restaurant near your home.":
            jump scene_14B_choice1
        "Apologize.":
            jump scene_14B_choice2

    return

label scene_14B_choice1:
    $ Skor += 10
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45

    show callista sad left 
    voice callistaVoiceScene14B+"Scene 14_HJ_4_Final.mp3"
    j "I’m really sorry, okay."

    show callista focused left 

    j "As an apology, I would love to treat you with food from a restaurant near my home."
    j "How about that?"

    show bisma normal right 

    b "Well, I am hungry right now."
    b "Okay then, let’s go there."

    stop music
    return

label scene_14B_choice2:
    $ Skor -= 10

    show callista sad left 
    voice callistaVoiceScene14B+"Scene 14_HJ_4_Final.mp3"
    j "I’m really sorry, okay."

    show bisma normal right 

    b "It’s okay. I have forgiven you."

    #hide callista
    #hide bisma

    pause .2
    "{i}There is an awkward silence between them.{/i}"

    show callista focused left
    #show bisma normal at right

    j "Well, since the sun is setting, I have to go back to my home now."

    b "Go alone? I can’t let you do that."
    b "What if something bad happens?"

    j "Well, would you go with me?"

    b "Sure."

    return