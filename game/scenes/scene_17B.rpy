
label scene_17B:
    scene bg streaming

    #show kazuo normal

    v "Are you ready yet, Callista?"

    #hide kazuo
    #show callista normal

    j "Yeah, just let me use the VTuber model first."

    #hide callista
    pause(1.0)
    #show hazu normal

    h "Okay, now it’s on."
    h "We should start now."

    #show hazu normal at left
    #show kazuo normal at right

    v "Are you sure?"
    v "You aren’t focused."

    h "I’m very sure. I’m just pretty tired after today."

    v "I mean, we can postpone this stream a bit if you want to talk about it."

    h "It’s okay. We can talk about it after the stream."

    v "Okay then."

    #hide kazuo
    #hide hazu

    "*Kazuo and Hazu-Chan streams together again*"
    "*They have a great time, but it’s getting late and Hazu-Chan aren’t focused at the game*"

    #show hazu tired at left
    #show kazuo normal at right

    h "I’m getting tired, maybe we should end the stream now."

    v "Yeah, good bye everyone."
    v "Thank you for coming to our stream."

    #show hazu happy

    h "Bye everyone!"

    scene bg discord

    #show darren serious

    w "Now that stream ends. Do you want to talk about what happened?"

    #show darren serious at right
    #show callista tired at left

    j "Yeah. Earlier today, a thief stole my bag."

    #show darren normal

    w "Did you get it back?"

    #show callista normal

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
    #$ Skor +=
    
    j "Oh…, that’s great."

    #show darren thinking

    w "You don’t sound very excited. Is there something wrong?"

    #show callista tired

    j "No, maybe it’s just me who’s tired."

    #show darren normal

    w "Oh, okay."
    w "You should sleep now then."

    j "You’re right. I should rest now."

    w "Oh yeah, one more thing."
    w "Prepare for the unexpected."

    #show callista normal

    j "What does that me—"

    #hide darren
    #play sound "discord.mp3"

    return

label scene_17B_choice2:
    #$ Skor -= 

    #show callista surprised

    j "Wait Really?"

    #show callista happy

    j "That’s awesome."

    w "Yeah, I think it will be good if we meet together."

    j "Sure, what kind of place?"
    j "A cafe? A park? Something else?"

    w "I already have something in mind, just you wait."

    j "Okay then, keep your secrets."

    #show callista tired

    j "*yawn*"

    w "I think you should rest now."
    w "You looked very tired."

    j "You’re right. I should rest now."

    w "Oh yeah, one more thing."
    w "Prepare for the unexpected."

    j "What does that me—"

    #hide darren
    #play sound "discord.mp3"

    return