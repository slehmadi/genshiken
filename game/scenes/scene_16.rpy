
label scene_16:
    scene bg room

    "*Callista is on her bed, talking to Lucky*"

    #show lucky worried

    c "You don’t usually call me during this time."
    c "Did something bad happen?"

    #show lucky worried at right
    #show callista sad at left

    j "Well, my bag got stolen today."

    c "Wait, really?"
    c "Are you okay?"

    #show callista happy

    j "Yes I’m fine."
    j "Bisma helped me to get it back."

    c "Well then, why did you call me?"

    #show callista thinking

    j "I’m just feeling a bit indecisive."
    j "Bisma has helped me a lot but I’m still not sure whether he is the right person for me."
    j "Do you think he’s the right one for me?"

    #show lucky normal

    c "First of all, I need you to answer this question."
    c "Are you actually attracted to him or do you just want to be in a relationship?"

    j "…"
    j "Well, after you said it. I somewhat just want to be in a relationship."
    j "Well, I do have my own reasons alright."
    j "I just don’t want people to think that I’m antisocial just because I’m not in a relationship."

    c "Who said that you’re antisocial just because you’re not in a relationship?"

    j "...., no one…."

    c "Exactly."
    c "You don’t have to worry about getting a boyfriend quickly."
    c "You should fix your mind set and instead think carefully on {b}who{/b} you’re gonna date."
    c "Now, I want you to take a step back and take a deep breath."

    #show callista normal

    j "Okay, I have."
    
    c "Now that your head is thinking clearly, what should your mindset be now?"

    j "I should be wise in choosing a boyfriend."

    c "Great! Now wh—"

    #hide callista
    #hide lucky
    #play sound "phone.mp3"

    #show callista normal at left
    #show lucky normal at right

    j "*It’s Kazuo.*"
    j "Lucky, I’m sorry, but I think I have to go now."
    j "I forgot that I have a collab with Kazuo today."

    c "It’s okay, we can continue to talk later."
    c "Go do your job."

    #hide lucky
    
    "*Lucky ends the call and Callista picks up Darren’s call*"

    #show darren normal at right

    w "Where are you, Callista? I’m already waiting."

    j "I’m sorry, I’m going to stream as soon as I can."
    j "Talk to you later in Discord."

    #hide darren
    #hide callista

    "*Callista hastily ends the call and turns on the computer*"

    return