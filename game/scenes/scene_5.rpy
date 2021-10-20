
label scene_5:
    "*Callista, Lucky, and Bisma arrived at the Art Convention Building*"
    "*The room is filled with different stands from every Student Activity Unit*"
    "*They all walk around multiple times, looking at every Unit*"

    #show bisma normal

    b "Alright, we have seen about three fourths of the Student Activity Unit here."
    b "What stand should we visit next?"

    #show bisma normal at right
    #with move
    #show callista normat at left

    j "We’ve visited a lot of stands. I think that’s enough for us to visit."

    #show lucky normal

    c "Yeah. We’ve visited the Art Unit, the Band Unit, The Sports Unit, even other Units that’s pretty weird."
    c "I mean, who wants to join the Pop Culture Enthusiast Unit, right?"

    b "So, you guys are joining the Band Unit, right?"

    c "Yeah, and I think I’ll join the Art Unit too."
    c "How about you, Callista?"

    #show callista thinking

    j "I’m still not quite sure."

    c "Well, I have to go to the bathroom now."
    c "You two should just visit other stands while waiting for me."

    #hide lucky
    #with dissolve

    "*Lucky goes to the toilet*"

    b "So, Callista, what stand do you wanna visit?"

    c "I dunno. Let’s just start walking."

    #hide callista
    #hide bisma

    "*Bisma and Callista walk across the row of stands*"

    #show callista normal at left
    #show bisma normal at right

    b "I heard from Lucky that you sometimes play a keyboard on your streams. Is that correct?"

    j "Yeah that’s true. I do that sometimes."

    b "So why don’t you join the Band Unit with us?"

    #show callista thinking

    j "I’m still thinking about it."
    j "If no other Unit excites me, then I’ll probably join the Band Unit with you and Lucky"

    b "I’m very sure you belong to the Band Unit."

    #show bisma happy

    b "Lucky said that your keyboarding skills are amazing."

    #show callista normal

    j "Lucky sometimes praises people too much."

    #show callista sad

    j "My skills aren’t that great."

    #show bisma energetic

    b "C’mon, have more confidence in yourself."
    b "I’m sure you’re talented at playing the keyboard. you’ll be perfect for the Band unit."

    #show callista smile (if exist)

    j "Well, if you said so."
    j "Then I will join the Band Unit."

    #show bisma normal

    b "BTW, Callista. Have you had a boyfriend before?"

    menu:
        "Can you guess?":
            jump can_you_guess
        "Why would you ask that":
            jump why_would_you_ask_that

    return

label can_you_guess:
    $ Skor += 10

    #show bisma thinking

    b "Let me think."
    b "You have one?"

    #show callista happy

    j "Nope, you’re wrong."
    j "I never even thought about having a boyfriend before."

    #show bisma normal

    b "Somehow, that’s not surprising."

    #show callista angry

    j "Are you joking with me?"
    j "Well, I’m gonna pick up a few brochures from the Band Unit."

    #hide bisma
    #show calista normal
    
    j "*Why did he want to know whether I have a boyfriend or not?*"

    #hide callista

    "*Callista left to pick up a few brochures and come back to Bisma who’s talking with Lucky*"
    "*After the Open House Unit finishes, they all then split up and went back to each of their home*"

    return

label why_would_you_ask_that:
    $ Skor -= 10

    #show bisma thinking

    b "Umm…"
    b "I dunno. I just see that you and Lucky are quite close."

    #show callista normal

    j "It’s not quite appropriate to ask that on the first day of meeting someone."
    j "But no, I never had a boyfriend before."
    j "Lucky is just my best friend."

    #show bisma normal

    b "I see. You’re a cold type of person."

    #show callista angry

    j "I-It’s not like that."
    j "I’m just busy with my job and education."
    j "Also, I’m gonna pick up a few brochures from the Band Unit."

    #hide bisma
    #show callista normal

    j "*Why did he want to know whether I have a boyfriend or not?*"

    #hide callista

    "*Callista left to pick up a few brochures and come back to Bisma who’s talking with Lucky*"
    "*They all then split up and went back to each of their home*"

    return