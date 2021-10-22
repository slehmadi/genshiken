
label scene_11:
    scene bg room #maybe? dunno

    #show lucky normal

    c "Hey, Callista, check your email from me."

    #show lucky normal at right
    #with move
    #show callista normal at left

    j "Is the new VTuber outfit finished?"

    c "Yes, I hope you liked it."

    j "Wow, you work really fast."
    j "Thank you for doing this for me. I really like the new outfit."

    c "Thank you."
    c "So anyway, I’m gonna go now."
    c "See you later, Callista"

    j "See you later too."

    #hide lucky
    #show callista normal at center

    j "*This new outfit is really good. I should ask another person’s opinion.*"

    #show callista thinking

    j "*Should I ask Kazuo or just share the new outfit on my Instagram?*"

    menu:
        "Just upload it to Instagram.":
            jump scene_11_choice1
        "Ask Kazuo’s opinion first.":
            jump scene_11_choice2

    return

label scene_11_choice1:
    $ Skor += 10

    #hide callista

    "*Callista sends the new VTuber outfit to Instagram*"
    "*Bisma instantly commented on it*"

    # (uhm.... kita tunjukin aja charanya atau biarin aja??)
    #show bisma normal at right

    b "Wow! The outfit looks really great."
    b "I think it really fits you."

    #show callista at left

    j "Thank you for the compliment."

    b "So are you gonna change your streaming model on your next stream?"

    j "Not yet, I think I will use it when the next month starts. I think that’ll be the perfect time."
    j "Okay then, that’s all that I want to ask."

    b "Okay then, see you later."
    b "Bye, Callista!"

    j "Bye, Bisma."

    return

label scene_11_choice2:
    $ Skor -= 10

    j "I should ask Kazuo’s opinion first."

    #hide callista

    "*Callista sends the new VTuber model to Kazuo*"

    #show callista normal at left

    j "Hi, Kazuo. This is my new VTuber outfit, what do you think?"

    #show kazuo normal at right

    v "Wow! The outfit looks really great."
    v "I think it really fits you."

    j "Thank you for the compliment."

    v "So are you gonna change your streaming model on our next stream?"

    j "Not yet, I think I will use it when the next month starts. I think that’ll be the perfect time."
    j "Okay then, that’s all that I want to ask."

    v "Okay then, see you later."
    v "Bye, Callista!"

    j "Bye, Kazuo."

    return

