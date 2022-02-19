define bismaVoiceScene7 = "audio/Dubs/B/Scene_7_B_Final.mp3"
define callistaVoiceScene7 = "audio/Dubs/J-H/Scene 7/"

label scene_7:
    scene black
    with dissolve
    "{i}The Next Day{/i}"
    
    scene bg 4
    with dissolve

    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45
    #show lucky happy
    show lucky happy right
    with dissolve
    c "Callista! Finally you came."

    #hide lucky
    show callista happy left #show callista happy
    with moveinleft

    j "Thank you Lucky for wanting to meet me here."

    #show callista normal at left
    #with move
    show lucky worried right #show lucky worried at right

    c "Hey, I’m always ready to help. So, why do you want to talk to me?"

    show callista sad left #show callista sad

    j "I just felt a bit overwhelmed because of yesterday."
    j "It feels weird having to spend time outside again and meet a lot of new friends."

    c "I understand that things could be overwhelming because of sudden change, but..."
    c "I’m pretty sure you’ll quickly adapt and not feel overwhelmed anymore."
    c "But if you do feel overwhelmed again, search for me and I’ll help you."
    c "I mean, that’s what best friends are for, right?"

    show callista focused left #show callista normal

    j "Thank you, Lucky. I could always trust you."
    j "Also may I ask you something?"

    show lucky normal right #show lucky normal

    c "Sure. What is it?"

    j "What is your opinion on Bisma and Kazuo?"

    c "Well, I think both of them are good friends for you."
    c "You used to idolize Kazuo, now you collab with him often. What’s not great about that?"
    c "Bisma is very cool too. We could spend time in a band with him."
    c "Why do you ask about my opinions anyway?"

    j "Nothing."

    "{i}Out of the sudden, Bisma came running to Lucky and Callista.{/i}"
    hide callista #hide callista
    hide lucky #hide lucky
    with dissolve
    show bisma normal right #show bisma normal
    with moveinright

    b "Finally I found you both."

    #show bisma normal at right
    #with move
    #show lucky at left
    show lucky normal left 
    with dissolve

    c "What is it, Bisma?"

    show bisma happy right #show bisma happy
    
    b "The Band Unit is gonna make a performance this evening."
    b "I think it’ll be cool if we watch it together."

    show lucky sad left #show lucky sad

    c "Sorry, but I can’t do that. I have a job to do."
    c "But I think Callista is free, right?"

    hide lucky #hide lucky
    show callista thinking left #show callista thinking at left

    j "I don’t know…"
    j "...I’m not quite sure."
    j "*The performance is at the exact same time as my collab. What should I do?*"

    voice bismaVoiceScene7
    b "C’mon, it’ll be fun. So, what do you think?"

    stop music
    menu:
        "Join Bisma to the Band Unit performance":
            jump join_bisma_band
        "Go home and accept Kazuo’s offer to collab with him again.":
            jump go_home_kazuo

    return

label join_bisma_band:
    $ Skor += 30
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45

    show callista focused left
    voice callistaVoiceScene7+"Scene 7_HJ_1_Final.mp3"
    j "Fine, I guess I’ll join you."

    b "That’s great, we should go to Art Convention Building now."

    j "Is it okay if I left you, lucky?"

    hide bisma #hide bisma
    show lucky happy right #show lucky happy at right

    c "Go ahead and just enjoy the performance."
    c "I’ll just go back to my home and do my work."

    show callista happy left #show callista happy

    j "Okay then, see you later, Lucky!"

    hide lucky #hide lucky
    with moveoutright 
    show bisma happy right #show bisma happy at right
    with moveinright

    b "See you later too, Lucky!"

    j "{i}I hope Kazuo isn’t mad about this.{/i}"

    hide callista#hide callista
    hide bisma #hide bisma
    with dissolve

    scene black
    "{i}Bisma and Callista went to the Art Convention Building.{/i}"

    call scene_8A from _call_scene_8A
    call scene_9A from _call_scene_9A

    stop music
    return

label go_home_kazuo:
    $ Skor -= 30
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45
    #show callista sad
    show callista sad left
    j "I’m really sorry, but I don’t think I could."

    show bisma sad right #show bisma sad

    b "hat’s a shame. Guess I’ll watch it alone then."
    b "Good bye then, see you tomorrow."

    hide bisma #hide bisma
    with moveoutright

    "{i}Bisma left for the Art Convention Building.{/i}"

    show lucky focused right #show lucky normal at right

    c "Why did you refuse his offer?"

    show callista focused left 
    j "I have my own reasons."

    c "Okay then."
    c "Well, since I have a job to do, it’ll be best if we end this talk for now."

    j "Yeah, I have things to do too."

    show lucky happy right #show lucky happy

    c "Okay then, see you later, Callista!"

    show callista happy left #show callista happy

    j "See you later too!"

    hide lucky #hide lucky
    with moveoutright

    "{i}Lucky left Callista alone in the university’s park{/i}"

    show callista focused center #show callista normal at center
    with move

    j "Guess I should contact Kazuo that I will collab with him again."

    hide callista 

    "{i}Callista sends a message to Kazuo and he answers it almost instantly. He agrees to do another collab this evening.{/i}"

    show callista focused center 

    j "{i}I hope Bisma isn’t mad that I refused his invite.{/i}"

    call scene_8B from _call_scene_8B
    call scene_9B from _call_scene_9B

    stop music
    return