
label scene_END2_B:
    scene bg 8
    with dissolve

    play music "audio/Musics/4-Amusement Park_How It Began.mp3" volume 0.45

    "{i}Callista is standing in the front of the amusement park.{/i}"

    show callista focused center
    with dissolve

    j "Where’s Bisma? He’s supposed to be here now."

    hide callista
    with dissolve

    "{i}Callista waited for another hour, but Bisma never came.{/i}"

    show callista sad left
    with dissolve
    
    j "Maybe I should just leave."

    show darren normal right #show bisma normal
    with moveinright

    w "Hi, Callista! What are you doing here?"

    #show darren normal at right
    #show callista normal at left
    show callista focused left 

    j "Oh, hi, Darren."
    j "I didn’t think I would meet you here."
    j "It feels weird meeting you in real life."

    show callista sad left 

    j "I was waiting for Bisma, but I don’t think he will show up anytime soon."

    w "Well, why don’t you go inside with me?"

    show callista focused left 

    j "Do you still have an extra ticket?"

    #show darren happy

    w "Of course, I kept it just for you."

    j "Wow, that’s so nice of you."

    w " Let’s go inside then."

    show callista happy left #show callista happy

    j "Yeah, let’s go."

    hide callista
    hide darren
    with dissolve

    "{i}Darren and Callista spends their entire day together in the amusement park.{/i}"
    "{i}They ride so many attraction and have lots of fun.{/i}"
    "{i}But the sun must set and it’s the time for them to leave.{/i}"

    #show darren happy
    show callista happy left 
    show darren normal right 

    w "It’s been such a wonderful day to spend time with you."

    #show darren happy at right
    #show callista happy at left

    j "It’s been wonderful meeting you too."

    #show darren normal

    w "Hey, are you free next weekend?"

    show callista focused left 

    j "Why?"

    w "I wanted to bring you to a beautiful place near this city."

    j "You’ve only arrived here for a few days and you already know places around this city?"

    w "I asked someone."
    w "Anyway, it’s probably best if we split here."
    w "The sun is already setting."

    show callista happy left 

    j "Yeah, well, meet you on our stream tomorrow."

    #show darren happy

    w "Meet you there too."
    w "Bye, Callista."

    j "Bye, Darren."

    hide darren
    hide callista
    with dissolve

    "{i}Darren and Callista went to their own home.{/i}"
    stop music

    show callista focused left
    with dissolve

    j "{i}I still don’t see Bisma anywhere today. Maybe he really did forget about me.{/i}"

    scene black
    with dissolve
    "{i}The Next Day.{/i}"

    scene bg 6
    with dissolve

    show callista focused left 
    show lucky normal right 
    with dissolve

    j "Where is Bisma?"
    j "He’s supposed to be here right now."
    j "We were supposed to study together."

    #show callista normal at left
    #show lucky normal at right

    c "Callista, you didn’t know yet?"

    j "Know what?"

    c "Bisma is currently performing in the Art Convention Building."

    j "Really?"
    j "Since when did he get so popular?"

    c "His popularity has increased drastically these past few days."
    c "Haven’t you noticed?"

    j "I didn’t."

    c "Well, do you want to see his performance?"

    j "Sure."

    scene bg 5
    with dissolve

    "{i}They arrive at the building in the middle of a performance.{/i}"
    "{i}On the stage, Bisma is playing the guitar with full energy.{/i}"

    show callista focused left 
    show lucky normal right 
    with dissolve

    j "He’s performing right now."
    j "But why didn't he invite me or tell me anything about this?"

    #show callista normal at left
    #show lucky normal at right

    c "Well, you have seen what you want to see."
    c "Guess we could study together until Bisma finishes his performance."

    j "Yeah."

    hide callista
    hide lucky
    with dissolve

    "{i}The day almost ends and Bisma never arrive to study together.{/i}"

    show callista focused left
    show lucky normal right
    with dissolve

    j "Guess he doesn’t want to study with us anymore."

    c "Well, I have to go now."
    c "Bye, Callista."

    j "Bye."

    scene bg 4

    "{i}Callista walk across the university’s park and sees Bisma.{/i}"

    #show callista

    j "He’s talking to a lot of girls."
    j "Wait, are they studying?"
    j "{i}Bisma really did forgot about me.{/i}"
    j "{i}Is it my fault?{/i}"
    j "{i}No, remember what Lucky said.{/i}"
    j "{i}The past is gone, I should just focus on the future.{/i}"
    j "This is just the end of a path, a new chance will come to me."
    j "I should just move on and let Bisma do his own thing."
    j "Not everything could stay the same forever."

    scene black
    with dissolve
    "{i}The Next Weekend.{/i}"

    scene bg 9
    with dissolve

    "{i}Darren brings Callista to a place near a cliff with a wonderful view of the sea.{/i}"
    "{i}they sit on a bench facing to the sea.{/i}"

    play music "audio/Musics/5-Tempat Indah_Memories of Love.mp3" volume 0.45
    #show callista normal
    show callista focused left 
    show darren normal right 
    with dissolve

    j "This place is really beautiful."
    j "Why do you want to bring me here?"

    #show callista normal at left
    #show darren normal at right

    w "I want to tell you something."
    
    j "What is it?"

    w "Do you want to go on a date with me?"

    show callista thinking left 

    j "…"
    pause(1.0)

    show callista happy left 

    j "Of course, after everything you’ve done."

    #show darren happy

    w " I’m so happy, I’m out of words."

    hide callista
    hide darren
    with dissolve

    "{i}They both keep smiling to each other, but then Callista’s smile fade away.{/i}"

    show callista focused left
    show darren normal right
    with dissolve

    w "Hay, Callista, is there something wrong?"

    j "There’s nothing wrong."

    w "Then why do you look worried all of a sudden?"

    show callista sad left 

    voice "audio/Dubs/J-H/Bad ending/Bad Ending_HJ_Final.mp3"
    j "I...I don’t think I made the right choice…"
    j "…."

    scene black
    "{i}The End..?{/i}"

    stop music
    return