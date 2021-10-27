
label scene_17A:
    scene bg straming

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

    h "I’m very sure. Just start the stream already."

    v "Okay then."

    #hide kazuo
    #hide hazu

    "*Kazuo and Hazu-Chan streams together again, but something is off*"
    "*Hazu-Chan isn’t focused at the game and Kazuo seems down*"
    "*The chat started to notices it, then Hazu-Chan decided to ends her stream earlier*"

    scene bg discord

    #show callista normal

    j "Kazuo, you aren’t as funny to your audience today."
    j "Is there something wrong?"

    #show callista normal at left
    #show kazuo normal at right

    v "You too aren’t focused on the game."
    v "What’s happening?"

    #show callista tired

    j "It’s probably because it's already late and I’m tired."

    #show kazuo tired

    v "Yeah, I guess you’re right"
    v "I’m tired too."

    j "Well then, Kazuo. Guess I’m going to sleep."

    v "Just call me Darren."

    #show callista normal

    j "Wait, your name is Darren?"

    #show kazuo normal

    v "Yes. After so many collab that we did, I think it's time to tell you my name."

    j "Thank you for trusting me."
    j "Well, if that’s all you have to say, I’m going to sleep."

    v "Wait a sec."

    j "What is it?"

    v "I have a big news that I wanna tell you."

    #show callista thinking

    j "And it is?"

    v "I’m coming to your town next week."
    v "What do you think?"

    menu:
        "Oh...":
            jump scene_17A_choice1
        "That’s great!":
            jump scene_17A_choice2

    return

label scene_17A_choice1:
    $ Skor += 10

    #show callista normal

    j "Oh…, that’s great."

    v "You aren’t happy?"

    #show callista tired

    j "No, no. I’m very happy."
    j "Finally I’m able to meet you after many collabs we’ve been through."

    v "You seem tired. Maybe you should sleep now."

    j "Yeah, you’re right."

    v "Callista, one more thing."

    j "…"

    v "Prepare for the unexpected."

    j "I don’t know what that means."

    v "Don’t think about it, just rest now."
    v "I’m going to leave now so you can rest."
    v "Bye."

    return

label scene_17A_choice2:
    $ Skor -= 10

    #show callista happy

    j "That’s such great news."

    v "It’s good right."

    j "Finally I’m able to meet you in real life."

    #show callista normal

    j "But how am I gonna know how you look?"

    v "Well, I was gonna show my face a few days ago, but you didn’t answer my call."

    j "I’m really sorry, Kazuo. I had a Band Unit assignment that day and it’s pretty busy."

    v "I know, I understand."
    v "I’m gonna go now. Bye."
    v "Also, prepare for the unexpected."

    j "What does that me—"

    #hide kazuo
    #play sound "discord.mp3"

    return