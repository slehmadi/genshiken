
label scene_10:
    scene
    "*Callista is in class, listening to the college lecture*"

    #show callista thinking

    j "*Why can’t I focus on this class?*"
    j "*Why do I keep thinking about Bisma and Kazuo?*"
    j "*I must focus.*"

    #hide callista

    "*Callista tried to focus on the lecture, but her focus fade away in a few minutes*"

    #show callista thinking

    j "*What is wrong with me?*"
    j "*All of this college life is affecting too much of my life.*"
    j "*I managed to get a lot of friends with the help of Lucky. He’s always happy to help me.*"
    j "*Bisma is nice and with his musical skills, he will be quite popular. When he’s popular, will I be able to talk to him again?*"
    j "*Kazuo is very nice too. We have collabed a lot and I enjoy streaming with him. He’s fun to talk with, but I don’t know if our friendship is real or just for job purposes*"
    j "*Why am I thinking about all of this inside class?*"

    #hide callista

    "*The lecture ends just as Callista stops thinking about them*"

    #show callista normal

    j "Great, I just wasted my time in class, now I have to study more at home."
    j "Well, maybe I could rest a bit now."

    #hide callista

    j "*Callista checks her phone*"

    #show callista normal

    j "*There’s a message from Kazuo*"
    j "*I just remember, I was supposed to be in a call with him soon*"
    j "*If I run home, it should be enough time to arrive in time*"

    #show callista normal at left
    #with move
    #show bisma normal at right
    #with moveinright

    b "Hey, Callista. How are you?"

    #show callista surprised

    j "Oh hi, Bisma. You surprised me."

    #show callista normal

    j "I’m good."

    b "I wanted to talk to you for a bit."
    b "Are you in a rush right now?"

    menu:
        "Talk with Bisma and arrive late to Kazuo’s call.":
            jump talk_with_bisma
        "Run home and arrive in time for Kazuo’s call.":
            jump run_home

    return

label talk_with_bisma:
    $ Skor += 10

    j "No, I can talk."
    j "What’s the matter?"

    b "Since we register in the Band Unit, I want to know more about your skills in playing the keyboard."

    j "Well, I have been playing it since I was a kid."
    j "Lucky often ruins my training whenever he comes over to my home."
    j "You can see some of the songs I play on my stream VOD."

    #show bisma happy

    b "Wow, I have been playing guitar since I was a kid too."
    b "With Lucky, I’m sure we will be a great team in the Band Unit."
    b "Also have you heard the rumor?"

    #show callista thinking

    j "What rumor?"

    #show bisma normal

    b "Every Unit has an assignment for the one who registers."

    #show callista surprised

    j "Wait, really?"

    b "Yes, the seniors told me."

    #show callista normal

    j "Do we know what kind of assignment is gonna be?"

    b "Currently not. Guess we have to wait."
    b "Well, instead of  that, why don’t we talk about something more fun."
    b "So, what’s your favorite song to play?"

    #hide callista
    #hide bisma

    "*Bisma and Callista went on to talk for almost an hour*"
    "*After that, Callista quickly went home and talk to Kazuo*"
    
    scene bg ruangstream

    "*Kazuo seems upset but the frown quickly fade away as both of them talk*"

    return

label run_home:
    $ Skor -= 10

    j "I’m really sorry, but I’m in a hurry."

    b "Oh okay then, talk to you later."

    scene black

    "*Callista runs home and quickly opens her Discord*"

    scene bg ruangstream

    #show kazuo normal

    v "Oh, hi, Callista. Glad you are on time."
    v "Just a few minutes ago I was thinking you wouldn’t come."
    v "So, how’s the lecture?"

    #show kazuo normal at right
    #with move
    #show callista tired at left

    j "It’s pretty boring and I can’t focus on it."

    #show kazuo happy

    v "Well then, to clear your mind, I have good news."

    #show callista thinking

    j "What is it?"

    v "We’re having a sponsor for our next collab."

    #show callista happy

    j "That’s really good."

    #hide callista
    #hide kazuo

    "*Callista dan Kazuo talks more for a bit before Kazuo ends the call*"

    return