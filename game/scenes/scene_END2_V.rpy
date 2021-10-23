
label scene_END2_V:
    scene bg amusementpark

    "*Callista is standing in the front of the amusement park*"

    #show callista thinking

    j "Where is Darren? He’s supposed to be here now."

    #hide callista
    #show darren happy

    w "Hi, Callista!"

    #show darren happy at right
    #show callista happy at left

    j "Darren! So happy to finally meet you for real."

    w "So happy to meet you too."

    #show darren normal

    w "This feels very weird."
    w "Well, why don’t we just go inside?"

    #show callista normal

    j "Sure, let’s go."

    #hide callista
    #hide darren

    "*Darren and Callista spends their entire day together in the amusement park*"
    "*They ride so many attraction and have lots of fun*"
    "*But the sun must set and it’s the time for them to leave*"

    #show darren happy

    w "It’s been such a wonderful day to spend time with you."

    #show darren happy at right
    #show callista happy at left

    j "It’s been wonderful meeting you too."

    #show darren normal

    w "Hey, are you free next weekend?"

    #show callista normal

    j "Why?"

    w "I wanted to bring you to a beautiful place near this city."

    j "You’ve only arrived here for a few days and you already know places around this city?"

    w "I asked someone."
    w "Anyway, it’s probably best if we split here."
    w "The sun is already setting."

    #show callista happy

    j "Yeah, well, meet you on our stream tomorrow."

    #show darren happy

    w "Meet you there too."
    w "Bye, Callista."

    j "Bye, Darren."

    #hide callista
    #hide darren

    "*Without their knowledge, Bisma was watching them from behind*"
    "*His heart is broken and he went far away from the amusement park*"

    scene black
    "-The Next Day-"

    scene bg classroom

    #show callista normal

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

    scene bg artconvention

    "*They arrive at the building in the middle of a performance*"
    "*On the stage, Bisma is playing the guitar with full energy*"

    #show callista normal

    j "He’s performing right now."
    j "But why didn't he invite me or tell me anything about this?"

    #show callista normal at left
    #show lucky normal at right

    c "Well, you have seen what you want to see."
    c "Guess we could study together until Bisma finishes his performance."

    j "Yeah."

    #hide callista
    #hide lucky

    "*The day almost ends and Bisma never arrive to study together*"

    #show callista normal at left
    #show lucky normal at right

    j "Guess he doesn’t want to study with us anymore."

    c "Well, I have to go now."
    c "Bye, Callista."

    j "Bye."

    scene bg campusspark

    "*Callista walk across the university’s park and sees Bisma*"

    #show callista

    j "He’s talking to a lot of girls."
    j "Wait, are they studying?"
    j "*Bisma really did forgot about me*"
    j "*Is it my fault?*"
    j "*No, remember what Lucky said.*"
    j "*The past is gone, I should just focus on the future.*"
    j "This is just the end of a path, a new chance will come to me."
    j "I should just move on and let Bisma do his own thing."
    j "Not everything could stay the same forever."

    scene black
    "-The Next Weekend-"

    scene bg beautifulplace

    "*Darren brings Callista to a place near a cliff with a wonderful view of the sea*"
    "*they sit on a bench facing to the sea*"

    #show callista normal

    j "This place is really beautiful."
    j "Why do you want to bring me here?"

    #show callista normal at left
    #show darren normal at right

    w "I want to tell you something."
    
    j "What is it?"

    w "Do you want to go on a date with me?"

    #show callista surprised

    j "…"
    pause(1.0)

    #show callista happy

    j "Of course, after everything you’ve done."

    #show darren happy

    w " I’m so happy, I’m out of words."

    #hide callista
    #hide darren

    "*They both keep smiling to each other, but then Callista’s smile fade away*"

    #show callista normal at left
    #show darren normal at right

    w "Hay, Callista, is there something wrong?"

    j "There’s nothing wrong."

    w "Then why do you look worried all of a sudden?"

    #show callista sad

    j "I...I don’t think I made the right choice…"
    j "…."

    scene black
    "{b}-The End-{/b}"

    return