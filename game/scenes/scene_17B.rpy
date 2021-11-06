define callistaVoiceScene17B = "audio/Dubs/J-H/Scene 17/"
define kazuoVoiceScene17B = "audio/Dubs/V-W/Scene 17/"

label scene_17B:
    scene bg 2

    show kazuo focused center
    with dissolve

    voice kazuoVoiceScene17B+"Scene 17_V_1_Final.mp3"
    v "Are you ready yet, Callista?"

    hide kazuo
    show callista focused center
    with dissolve

    j "Yeah, just let me use the VTuber model first."

    hide callista
    with dissolve
    pause(1.0)
    show hazu focused left 
    with dissolve

    h "Okay, now it’s on."
    h "We should start now."

    #show hazu normal at left
    #show kazuo normal at right
    show kazuo focused right
    with dissolve

    voice kazuoVoiceScene17B+"Scene 17_V_2_Final.mp3"
    v "Are you sure?"
    v "You aren’t focused."

    h "I’m very sure. I’m just pretty tired after today."

    v "I mean, we can postpone this stream a bit if you want to talk about it."

    h "It’s okay. We can talk about it after the stream."

    voice kazuoVoiceScene17B+"Scene 17_V_3_Final.mp3"
    v "Okay then."

    hide kazuo
    hide hazu
    with dissolve

    "{i}Kazuo and Hazu-Chan streams together again.{/i}"
    "{i}They have a great time, but it’s getting late and Hazu-Chan aren’t focused at the game.{/i}"

    show hazu focused left #show hazu tired at left
    show kazuo focused right #show kazuo normal at right

    h "I’m getting tired, maybe we should end the stream now."

    voice kazuoVoiceScene17B+"Scene 17_V_4_Final.mp3"
    v "Yeah, good bye everyone."
    v "Thank you for coming to our stream."

    show hazu happy left

    h "Bye everyone!"

    hide hazu
    hide kazuo
    with dissolve

    "{i}The Stream End...{/i}"

    show darren serious right
    show callista tired left 

    w "Now that stream ends. Do you want to talk about what happened?"

    #show darren serious at right
    #show callista tired at left

    j "Yeah. Earlier today, a thief stole my bag."

    show darren normal right

    w "Did you get it back?"

    show callista focused left 

    j "Yes, Bisma helped me."
    j "I’m glad that the thief didn’t steal anything else."

    w "I’m glad you’re okay too."
    w "But that doesn’t explain why you aren’t focused."

    j "I’m just thinking about something."

    w "Well, if you need my help, just call me okay."

    j "It’s okay. Lucky has been helping me sort things out."

    w "Since the stream is over, I have something to tell you."

    j "What is it?"

    w "Next week, I’m coming to your city."

    menu:
        "Oh...":
            jump scene_17B_choice1
        "That’s great!":
            jump scene_17B_choice2

    return

label scene_17B_choice1:
    $ Skor += 10
    
    voice callistaVoiceScene17B+"Scene 17_HJ_1_Final.mp3"
    j "Oh…, that’s great."

    show darren confused right #show darren thinking

    w "You don’t sound very excited. Is there something wrong?"

    show callista tired left #show callista tired

    j "No, maybe it’s just me who’s tired."

    show darren normal right #show darren normal

    w "Oh, okay."
    w "You should sleep now then."

    j "You’re right. I should rest now."

    w "Oh yeah, one more thing."
    w "Prepare for the unexpected."

    show callista focused left #show callista normal

    j "What does that me—"

    hide darren #hide darren
    with dissolve
    play sound "audio/Sound Effects/sfx4.mp3"
    pause .2

    return

label scene_17B_choice2:
    $ Skor -= 10
    show callista happy left 

    voice callistaVoiceScene17B+"Scene 17_HJ_3_Final.mp3"
    j "Wait Really?"

    #show callista happy

    j "That’s awesome."

    w "Yeah, I think it will be good if we meet together."

    j "Sure, what kind of place?"
    j "A cafe? A park? Something else?"

    w "I already have something in mind, just you wait."

    j "Okay then, keep your secrets."

    show callista tired left 

    j "{i}yawn.{/i}"

    w "I think you should rest now."
    w "You looked very tired."

    j "You’re right. I should rest now."

    w "Oh yeah, one more thing."
    w "Prepare for the unexpected."

    j "What does that me—"

    hide darren
    with dissolve
    play sound "audio/Sound Effects/sfx4.mp3"
    pause .2

    return