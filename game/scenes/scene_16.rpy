
label scene_16:
    scene black 
    with dissolve
    "{i}Later That Night..{/i}"

    scene bg 3
    with dissolve

    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    "{i}Callista is on her bed, talking to Lucky.{/i}"

    show lucky worried right
    show callista focused left 
    with dissolve

    c "You don’t usually call me during this time."
    c "Did something bad happen?"

    #show lucky worried at right
    #show callista sad at left
    show callista sad left 

    j "Well, my bag got stolen today."

    c "Wait, really?"
    c "Are you okay?"

    show callista happy left 

    j "Yes I’m fine."
    j "Bisma helped me to get it back."

    c "Well then, why did you call me?"

    show callista thinking left 

    j "I’m just feeling a bit indecisive."
    j "Bisma has helped me a lot but I’m still not sure whether he is the right person for me."
    j "Do you think he’s the right one for me?"

    show lucky normal right 

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

    show callista focused left 

    j "Okay, I have."
    
    c "Now that your head is thinking clearly, what should your mindset be now?"

    j "I should be wise in choosing a boyfriend."

    c "Great! Now wh—"

    hide callista
    hide lucky
    with dissolve

    "{i}Callista’s phone is ringing.{/i}"

    show callista focused left
    show lucky normal right
    with dissolve

    j "{i}It’s Kazuo.{/i}"
    j "Lucky, I’m sorry, but I think I have to go now."
    j "I forgot that I have a collab with Kazuo today."

    c "It’s okay, we can continue to talk later."
    c "Go do your job."

    hide lucky
    with dissolve
    
    "{i}Lucky ends the call and Callista picks up Kazuo’s call.{/i}"

    #show kazuo normal at right

    v "Where are you, Callista? I’m already waiting."

    j "I’m sorry, I’m going to stream as soon as I can."
    j "Talk to you later in Discord."

    hide kazuo
    hide callista
    with dissolve

    "{i}Callista hastily ends the call and turns on the computer.{/i}"

    stop music
    return