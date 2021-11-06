define callistaVoiceScene10 = "audio/Dubs/J-H/Scene 10/"
define kazuoVoiceScene10 = "audio/Dubs/V-W/Scene 10/"
define bismaVoiceScene10 = "audio/Dubs/B/Scene_10_B_Final.mp3"

label scene_10:
    scene black
    with dissolve
    "{i}The Next Day.{/i}"

    scene bg 6
    with dissolve

    play music "audio/Musics/1-Kelas_Slow Steps.mp3" volume 0.45
    "{i}Callista is in class, listening to the college lecture.{/i}"

    show callista thinking center #show callista thinking
    with dissolve

    j "{i}Why can’t I focus on this class?{/i}"
    j "{i}Why do I keep thinking about Bisma and Kazuo?{/i}"
    j "{i}I must focus.{/i}"

    hide callista #hide callista
    with dissolve

    "{i}Callista tried to focus on the lecture, but her focus fade away in a few minutes.{/i}"

    show callista thinking center #show callista thinking
    with dissolve

    j "{i}What is wrong with me?{/i}"
    j "{i}All of this college life is affecting too much of my life.{/i}"
    j "{i}I managed to get a lot of friends with the help of Lucky. He’s always happy to help me.{/i}"
    j "{i}Bisma is nice and with his musical skills, he will be quite popular. When he’s popular, will I be able to talk to him again?{/i}"
    j "{i}Kazuo is very nice too. We have collabed a lot and I enjoy streaming with him. He’s fun to talk with, but I don’t know if our friendship is real or just for job purposes.{/i}"
    j "{i}Why am I thinking about all of this inside class?{/i}"

    hide callista
    with dissolve

    "{i}The lecture ends just as Callista stops thinking about them.{/i}"

    show callista focused center #show callista normal
    with dissolve

    j "Great, I just wasted my time in class, now I have to study more at home."
    j "Well, maybe I could rest a bit now."

    hide callista #hide callista
    with dissolve

    "{i}Callista checks her phone.{/i}"

    show callista focused center #show callista normal
    with dissolve

    j "{i}There’s a message from Kazuo.{/i}"
    j "{i}I just remember, I was supposed to be in a call with him soon.{/i}"
    j "{i}If I run home, it should be enough time to arrive in time.{/i}"

    show callista focused left #show callista normal at left
    with move #with move
    show bisma normal right #show bisma normal at right
    with moveinright #with moveinright

    b "Hey, Callista. How are you?"

    #show callista surprised

    j "Oh hi, Bisma. You surprised me."

    #show callista normal

    j "I’m good."

    b "I wanted to talk to you for a bit."

    voice bismaVoiceScene10
    b "Are you in a rush right now?"

    stop music
    menu:
        "Talk with Bisma and arrive late to Kazuo’s call.":
            jump talk_with_bisma
        "Run home and arrive in time for Kazuo’s call.":
            jump run_home

    return

label talk_with_bisma:
    $ Skor += 10
    play music "audio/Musics/1-Kelas_Slow Steps.mp3" volume 0.45

    voice callistaVoiceScene10+"Scene 10_HJ_1_Final.mp3"
    j "No, I can talk."
    j "What’s the matter?"

    b "Since we register in the Band Unit, I want to know more about your skills in playing the keyboard."

    j "Well, I have been playing it since I was a kid."
    j "Lucky often ruins my training whenever he comes over to my home."
    j "You can see some of the songs I play on my stream VOD."

    show bisma happy right #show bisma happy

    b "Wow, I have been playing guitar since I was a kid too."
    b "With Lucky, I’m sure we will be a great team in the Band Unit."
    b "Also have you heard the rumor?"

    show callista thinking left #show callista thinking

    j "What rumor?"

    show bisma normal right #show bisma normal

    b "Every Unit has an assignment for the one who registers."

    #show callista surprised

    j "Wait, really?"

    b "Yes, the seniors told me."

    #show callista normal

    j "Do we know what kind of assignment is gonna be?"

    b "Currently not. Guess we have to wait."
    b "Well, instead of  that, why don’t we talk about something more fun."
    b "So, what’s your favorite song to play?"

    hide callista #hide callista
    hide bisma #hide bisma
    with dissolve

    "{i}Bisma and Callista went on to talk for almost an hour.{/i}"
    "{i}After that, Callista quickly went home and talk to Kazuo.{/i}"
    
    stop music
    scene bg 2
    with dissolve

    "{i}Kazuo seems upset but the frown quickly fade away as both of them talk.{/i}"

    return

label run_home:
    $ Skor -= 10

    voice callistaVoiceScene10+"Scene 10_HJ_2_Final.mp3"
    j "I’m really sorry, but I’m in a hurry."

    b "Oh okay then, talk to you later."

    stop music
    scene black

    "{i}Callista runs home and quickly opens her Discord.{/i}"
    play sound "audio/Sound Effects/sfx3.mp3"

    scene bg 2
    with dissolve

    show kazuo focused right #show kazuo normal
    show callista focused left
    with dissolve

    voice kazuoVoiceScene10+"Scene10_V_1_Final.mp3"
    v "Oh, hi, Callista. Glad you are on time."
    v "Just a few minutes ago I was thinking you wouldn’t come."
    v "So, how’s the lecture?"

    #show kazuo normal at right
    #with move
    #show callista tired at left
    show callista tired left 

    j "It’s pretty boring and I can’t focus on it."

    #show kazuo happy

    voice kazuoVoiceScene10+"Scene10_V_2_Final.mp3"
    v "Well then, to clear your mind, I have good news."

    show callista thinking left #show callista thinking

    j "What is it?"

    v "We’re having a sponsor for our next collab."

    show callista happy left #show callista happy

    j "That’s really good."

    hide callista #hide callista
    hide kazuo #hide kazuo
    with dissolve

    "{i}Callista dan Kazuo talks more for a bit before Kazuo ends the call{/i}"

    return