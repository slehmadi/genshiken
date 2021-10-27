
label scene_14A:
    scene bg campuss park
    
    "*Callista is walking through the university’s park*"

    #show callista tired

    j "College is pretty tiring today. I have a lot of tiresome homework, especially the lab report."
    j "Maybe I could get fresh air for a bit then get to work."

    #hide callista

    "*Callista sees a person on the other side of the park.*"

    #show callista normal

    j "*Isn’t that Bisma?*"

    #hide callista

    "*Bisma notices Callista and runs to her*"

    #show bisma happy

    b "Hi, Callista. What are you doing here?"

    #show bisma happy at right
    #show callista normal at left

    j "Just taking a whiff of fresh air before doing my homework."
    j "What are you doing here then?"

    #show bisma normal

    b "Just enjoying the beauty of this place."

    j "What beauty?"

    b "You."

    menu:
        "That’s…so nice of you":
            jump scene_14A_choice1
        "Huh?":
            jump scene_14A_choice2

    return

label scene_14A_choice1:
    $ Skor += 10

    #show callista blush

    j "That’s so nice of you."

    b "Well, do you want to take a walk together?"

    j "Sure."

    #hide bisma
    #hide callista

    "*Bisma and Callista enjoyed their time walking together, but it’s getting late*"

    #show callista normal

    j "The sun is gonna set. I should go home now."

    b "Do you want me to accompany you?"
    b "Just in case something bad happens."

    j "Sure."

    return

label scene_14A_choice2:
    $ Skor -= 10

    #show callista angry

    j "How dare you say that?"

    b "I’m sorry. I know that’s not appropriate for me to say."

    j "Glad that you admit your wrongdoing."

    b "Where are you going now?"

    #show callista normal

    j "I was just taking in the fresh air, but now I’m gonna go home and do my homework."

    b "Well, may I accompany you to your home as a form of apology?"
    b "Just in case something bad happens."

    j "Fine then, you could."

    return