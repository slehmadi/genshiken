
label scene_13A:
    scene black
    with dissolve
    "{i}The Next Day.{/i}"

    scene bg 5
    with dissolve

    "{i}Callista went as quickly as she can to the Art Convention Building.{/i}"

    #show callista normal

    j "Oh no, I’m late."

    "{i}Callista arrived at the building.{/i}"

    show callista tired center #show callista tired
    with dissolve

    j "Sorry, I’m late."

    hide callista #hide callista
    show bisma happy center #show bisma happy
    with dissolve

    b "Oh hi, Callista. Finally you came."

    hide bisma #hide callista
    with dissolve
    #hide bisma

    "{i}Callista looks at the room, but there’s something missing.{/i}"

    show callista focused left
    show bisma normal right
    with dissolve

    j "Where’s Lucky?"

    show bisma sad right #show bisma sad

    b "Sadly he got sick suddenly. So it’s just the two of us today."

    show callista sad left #show callista sad

    j "{i}Lucky suddenly sick? That’s weird.{/i}"

    show callista focused left #show callista normal

    j "Well, then. Let’s start making the assignment."

    play music "audio/Musics/8-Sabuga_Night Run Away.mp3" volume 0.45

    j "So, do you have any ideas for the assignment?"

    show bisma happy right #show bisma normal

    b "I have a few."

    hide bisma
    hide callista
    with dissolve

    "{i}Bisma went on to tell Callista all of his ideas.{/i}"

    show callista focused left
    show bisma happy right
    with dissolve

    j "All of those ideas are great! But I think the first idea would fit the best for both of us."

    show bisma energetic right 

    b "Okay then, let’s start making some tunes."

    show bisma happy right 

    b "Hope we can make a lot of progress today."

    j "Yeah. It will make Lucky have an easier time singing."

    hide callista
    hide bisma
    with dissolve

    "{i}They both walk to the stage and prepare their instruments.{/i}"

    show callista focused left
    show bisma normal right
    with dissolve

    b "I’ll lead with the guitar first. You follow me, okay?"

    j "Sure."

    hide callista
    hide bisma
    with dissolve

    "{i}They played harmoniously until the end.{/i}"
    "{i}Bisma can’t stop looking at Callista.{/i}"

    show bisma happy right
    show callista focused left 
    with dissolve 

    b "Woah, that was a lot of fun."
    b "Callista, you’re so good at the keyboard."

    #hide bisma
    show callista blushing left

    j "Thank you. You’re so good at the guitar too."
    j "Too bad Lucky couldn’t come today."

    show callista focused left
    show bisma normal right

    b "Yeah, but at least we have created a song today."
    b "Just need a bit of polishing and Lucky’s voice, then our Band Unit assignment is done."

    show callista happy right 

    j "It’s good that we could finish the assignment this quickly."
    j "Glad I’m on your team."

    show bisma energetic right

    b "Glad you’re on my team too."
    b "Our teamwork is really great."

    show callista tired left 

    j "Well, I’m tired and I have to go now."

    show callista happy left 

    j "See you next week, Bisma!"

    b "See you next week too!"

    hide callista
    hide bisma
    with dissolve

    scene black
    with dissolve
    "{i}After a tiring day, Bisma and Callista went to their homes.{/i}"

    stop music
    jump scene_14A

    return