define callistaVoiceScene12 = "audio/Dubs/J-H/Scene 12/"

label scene_12:
    scene bg 3
    with dissolve

    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    # (wait artinya ini juga gk perlu nunjukin charanya yah???)
    #show bisma
    #show callista at left
    #show lucky at right

    "{i}Callista is chatting with Bisma and Lucky.{/i}"

    b "Guys, look at the Band Unit chat!"
    b "There’s an assignment."

    j "So the assignment is real."

    c "Why give us an assignment now?"
    c "We are already tired of college and its assignments, not to mention quizzes."
    c "So what’s the assignment? I wasn’t paying attention."

    b "We have to make a song as a team of 3."

    c "That’s perfect then, Callista, you’re in our team, right?"

    j "Of course."

    b "That’s great, so when should we make it?"

    c "I think tomorrow will be a great time."
    c "We don’t have too many things to do tomorrow evening."

    j "Yeah, that’ll be the perfect time."

    b "Okay then, it’s set."
    b "Meet you guys tomorrow!"

    j "Meet you tomorrow too!"

    c "Bye everyone."

    #hide bisma
    #hide lucky
    #hide callista
    stop music

    "{i}Callista is about to sleep, but then she receives a message from Kazuo.{/i}"

    # (ini juga gk perlu yah...)
    #show kazuo

    v "Hi, Callista, sorry to bother you this late, but are you free tomorrow?"

    #show kazuo at right
    #show callista at left

    j "What’s happening tomorrow?"

    v "I have something really important that I want to tell you."
    v "This is very personal to me, so I hope you could answer my call tomorrow evening."
    v "Bye for now."

    #hide kazuo
    #show callista at center

    j "Kazuo, wa—"
    j "{i}Tomorrow evening I have to do my Band Unit assignment.{/i}"
    j "{i}But Kazuo did tell this is very personal.{/i}"

    voice callistaVoiceScene12+"Scene 12_HJ_1_Final.mp3"
    j "{i}What should I do?{/i}"

    menu:
        "Do the Band Unit assignment.":
            jump scene_12_choice1
        "Meet with Kazuo on a call.":
            jump scene_12_choice2

    return

label scene_12_choice1:
    $ Skor += 30

    voice callistaVoiceScene12+"Scene 12_HJ_2_Final.mp3"
    j "Guess I have to do the assignment."
    j "Assignment is more important to do."
    j "I hope Kazuo doesn’t mind me doing my assignments."

    jump scene_13A

    return

label scene_12_choice2:
    $ Skor -= 30

    voice callistaVoiceScene12+"Scene 12_HJ_3_Final.mp3"
    j "Guess I will meet with Kazuo."
    j "I don’t want to disappoint Kazuo."
    j "I hope Bisma and Lucky can handle the assignment while I’m gone."

    jump scene_13B

    return