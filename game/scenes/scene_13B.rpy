define kazuoVoiceScene13 = "audio/Dubs/V-W/Scene 13/"

label scene_13B:
    scene bg 2
    with dissolve

    play sound "audio/Sound Effects/sfx3.mp3"

    show kazuo focused right
    show callista focused left 
    with dissolve

    voice kazuoVoiceScene13+"Scene_13_V_1_Final.mp3"
    v "Hi, Callista. Thank you for wanting to meet me now."

    #show kazuo normal at right
    #show callista normal at left

    j "Hi, Kazuo. So why do you want to tell me?"

    v "I have a news that I wanted to tell you."

    j "What is it?"

    v "It’s a big secret of mine, so will you keep this information a secret?"

    j "Of course. Why would I betray one of my best friends?"
    j "What are you hiding?"
    j "You’re acting really strange."

    voice kazuoVoiceScene13+"Scene_13_V_2_Final.mp3"
    v "Well then, are you paying attention to the video call?"

    j "Of course."

    #hide callista
    hide kazuo
    with dissolve

    "{i}Kazuo opens his camera and shows his real face.{/i}"

    #show callista surprised at left
    show darren normal right
    with dissolve

    j "Kazuo! What are you doing?"
    j "What if anyone else saw you?"

    $ Darren_Reveal = True

    #show darren happy

    voice kazuoVoiceScene13+"Scene_13_V_3_Final.mp3"
    w "Also, my name isn’t Kazuo. It’s Darren."
    
    j "Why would you tell me that?"
    j "You’ve hidden your name and appearance for years. Why would you show it now?"

    w "Because I trusted you, Callista."

    #show callista normal

    j "But still, you should’ve kept your appearance hidden."
    j "What if the person you’re telling this to recorded your face and spread it to the internet?"

    #show darren normal

    w "I know you wouldn’t do that, Callista."

    j "That’s true, but what if someone else did that?"

    w "You’re the only one who has seen my face, so that secret is still hidden."

    j "So I’m the first one to see your face?"

    voice kazuoVoiceScene13+"Scene_13_V_4_Final.mp3"
    w "Yep, and probably the last one too."

    j "Why do you trust me so much?"

    #show darren happy

    w "Because you’re my closest friend that I ever had."
    w "I know I could trust you because since the beginning, I could see the kindness inside your heart."

    show callista blushing left #show callista blush

    j "That’s nice to hear."
    j "Thank you for the compliment."

    #show darren normal

    voice kazuoVoiceScene13+"Scene_13_V_5_Final.mp3"
    w "Well, thank you for being in this call. I’m gonna go now."

    show callista focused left #show callista normal

    j "Wait, so you’re telling me to be in this call just for that?"

    w "Yep, I’m going now."

    hide darren #hide darren
    with dissolve

    play sound "audio/Sound Effects/sfx4.mp3"
    j "Wait—"

    #music play "discord.mp3" loop = false

    #show callista normal at center

    j "Such a peculiar person. Why would he do that?"
    j "{i}Did he really trust me that much?{/i}"
    j "What is his name again?"
    j "Oh yeah, Darren."

    show callista blushing left #show callista blush

    j "That’s such a good name too."
    j "What am I thinking? I should just rest now."

    jump scene_14B

    return