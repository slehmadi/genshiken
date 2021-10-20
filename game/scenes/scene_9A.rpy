
label scene_9A:
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

    j "It’s about Kazuo…."

    c "What’s wrong about him?"

    j "He didn’t do anything wrong, it’s me who did something wrong to him."

    #show lucky worried

    c "What did you do?"

    j "I was supposed to collab with him this evening, but I didn’t."
    j "Bisma invited me to watch the Band Unit performance, but Kazuo offered me to collab with him at the same time as the performance."
    j "So I went with Bisma to the Band Unit Performance because I don’t want to seem antisocial to a friend I just saw yesterday."
    j "I felt so bad not accepting Kazuo’s offer."

    c "Callista, you shouldn’t feel bad. You can’t do two things at once and you have to choose one."
    c "It’s not your fault if you can’t do one of the things your friends offered."
    c "In fact, you’ve collab with Kazuo multiple times, right? I’m sure he will be fine if you don’t collab with him just this once."

    j "You’re probably right."
    j "But I still feel bad for him."

    #show lucky normal

    c "Hey, don’t worry. I’m sure Kazuo will understand if you told him your condition."
    pause(1.0)
    c "You have told him, right?"

    j "No, I haven’t."

    c "Well, you must have at least say sorry too him, right?"

    j "I haven’t either."

    #show lucky angry

    c "Then what are you doing?"
    c "Go talk to Kazuo now!"
    c "I will go now so you can talk with him."
    c "Bye"

    #hide lucky
    #hide callista

    "*Lucky hangs Callista’s call*"

    #show callista thinking

    j "Lucky is right. I should talk to him right now."

    #hide callista

    "*Callista calls Kazuo*"

    #show callista normal at left

    j "Hi, Kazuo. Sorry to bother you this late."

    #show kazuo normal at right

    v "You don’t usually call me this late, what’s the matter?"

    #show callista sad

    j "I just want to say that I’m really sorry that I couldn’t collab with you today."
    j "Bisma invited me to watch the Band Unit performance and it’s at the exact same time as our collab that you offered me."

    #show kazuo sad

    v "It’s okay, Callista. I understand that college is busy."
    v "I would have enjoyed our collab today, but I understand. College is more important than collabing."

    #show kazuo happy

    v "So how’s the performance? Is it good?"

    #show callista happy

    j "It’s a really great performance. Wish you could see it too."
    j "Glad that I joined that Student Activity Unit."
    j "I also spent some time with Bisma after the performance, trying out the instrument that’s still up on the stage."

    #show kazuo sad

    v "It’s good to hear you have a great time."
    v "Glad you enjoyed it."

    pause(0.5)
    "*There was a silence between them*"
    pause(0.5)

    #show kazuo normal

    v "Well it’s already late. I should just sleep now."
    v "Bye, Callista."

    #show callista normal

    j "Bye, Kazuo. Have a good sleep."

    return