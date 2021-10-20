
label scene_9B:
    scene
    "*Callista calls Lucky*"

    #show callista normal

    j "Hey Lucky, thanks for answering my call."

    #show callista normal at left
    #with move
    #show lucky worried at right

    c "What is it, Callista? Is there something wrong?"

    #show callista sad

    j "Not really…."
    j "Okay, I do have a problem."
    j "I felt bad about something that I did today."

    c "What is it? Just tell me everything and we could figure this out together."

    j "Well, I may have done something bad to one of my friends."

    #show lucky normal

    c "Who?"

    j "It’s about Bisma…."

    c "What’s wrong about him?"

    j "He didn’t do anything wrong, it’s me who did something wrong to him."

    #show lucky worried

    c "What did you do?"

    j "I was supposed to watch the Band Unit performance with him this evening, but I didn’t."
    j "Bisma invited me to watch the Band Unit performance, but Kazuo offered me to collab with him at the same time as the performance."
    j "So I chose to collab with Kazuo because he’s one of my closest friends."
    j "I felt so bad not accepting Bisma’s invite."

    c "Callista, you shouldn’t feel bad. You can’t do two things at once and you have to choose one."
    c "It’s not your fault if you can’t do one of the things your friends offered."
    c "In fact, we’ve been friends with Bisma for a year, right? I’m sure he will be fine if you don’t accept this offer."

    j "You’re probably right."
    j "But I still feel bad for him."

    c "Hey, don’t worry. I’m sure Bisma will understand if you tell him your condition."
    pause(1.0)
    c "You have told him, right?"

    j "No, I haven’t"

    c "Well, you must have at least said sorry to him, right?"

    j "I haven’t either."

    #show lucky angry

    c "Then what are you doing?"
    c "Go talk to Bisma now!"
    c "I will go now so you can talk with him."
    c "Bye."

    #hide lucky
    #hide callista

    "*Lucky hangs Callista’s call*"

    #show callista thinking

    j "Lucky is right. I should talk to him right now."

    #hide callista

    "*Callista calls Bisma*"

    #show callista normal at left

    j "Hi, Bisma. Sorry to bother you this late."

    #show bisma normal at right

    b "You don’t usually call me, what’s the matter?"

    #show callista sad

    j "I just wanted to say that I’m sorry that I couldn’t join you to watch the Band Unit performance today."
    j "I have a VTuber collab at the exact same time as the performance so I wouldn't go there with you."

    #show bisma sad

    b "It’s okay, Callista. I understand that your job is busy."
    b "I would love it if you could come with me, but I understand. Job is more important than a band performance."

    #show bisma happy

    b "So, how did the stream go?"

    #show callista happy

    j "It went really well."
    j "I played lots of games and even managed to win some."

    #show bisma sad

    b "It’s good to hear you have a great time."
    b "Glad you enjoyed it."

    pause(0.5)
    "*There was a silence between them*"
    pause(0.5)

    #show bisma normal

    b "Well it’s already late. I should just sleep now."
    b "Bye, Callista."

    #show callista normal

    j "Bye, Bisma. Have a good sleep."

    return