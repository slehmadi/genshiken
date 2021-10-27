
label scene_14B:
    scene bg campuss park

    "*Callista is walking through the university's park*"

    #show callista tired

    j "College is pretty tiring today. I have a lot of tiresome homework, especially the lab report."
    j "Maybe I could get fresh air for a bit then get to work."

    #hide callista

    "*Callista sees a person on the other side of the park.*"

    #show callista

    j "*Isn’t that Bisma?*"

    #hide callista

    "*Bisma notices Callista, then Callista come to him*"

    #show bisma sad

    b "Hi, Callista. What are you doing here?"

    #show bisma sad at right
    #show callista normal at left

    j "I was just taking a whiff of fresh air, but since you’re here, I want to say something."

    #show bisma normal

    b "If it’s about the Band Unit assignment, then forget about it."

    j "Look, I’m really sorry about that. It’s my fault."

    #show bisma sad

    b "It’s okay. Too bad I and Lucky couldn’t finish it in time."

    j "It’s all my fault. I should’ve come to help you."

    b "It’s not important anymore. We still got accepted at the Band Unit."
    b "So, let’s forget about that assignment."

    j "*He looks really sad*"
    j "*Should I do something to cheer him up?*"

    menu:
        "Offer him to eat together at a restaurant near your home.":
            jump scene_14B_choice1
        "Apologize.":
            jump scene_14B_choice2

    return

label scene_14B_choice1:
    $ Skor += 10

    #show callista sad

    j "I’m really sorry, okay."

    #show callista normal

    j "As an apology, I would love to treat you with food from a restaurant near my home."
    j "How about that?"

    #show bisma normal

    b "Well, I am hungry right now."
    b "Okay then, let’s go there."

    return

label scene_14B_choice2:
    $ Skor -= 10

    #show callista sad

    j "I’m really sorry, okay."

    #show bisma normal

    b "It’s okay. I have forgiven you."

    #hide callista
    #hide bisma

    "*There is an awkward silence between them*"

    #show callista normal at left
    #show bisma normal at right

    j "Well, since the sun is setting, I have to go back to my home now."

    b "Go alone? I can’t let you do that."
    b "What if something bad happens?"

    j "Well, would you go with me?"

    b "Sure."

    return