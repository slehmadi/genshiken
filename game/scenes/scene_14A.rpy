define callistaVoiceScene14A = "audio/Dubs/J-H/Scene 12/"

label scene_14A:
    scene black
    with dissolve
    "{i}Weekend..{/i}"

    scene bg 4
    with dissolve

    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45
    
    "{i}Callista is walking through the university’s park.{/i}"

    show callista tired center #show callista tired
    with dissolve

    j "College is pretty tiring today. I have a lot of tiresome homework, especially the lab report."
    j "Maybe I could get fresh air for a bit then get to work."

    hide callista #hide callista
    with dissolve

    "{i}Callista sees a person on the other side of the park.{/i}"

    show callista focused center
    with dissolve

    j "{i}Isn’t that Bisma?{/i}"

    hide callista
    with dissolve

    "{i}Bisma notices Callista and runs to her.{/i}"

    show callista focused left
    with dissolve
    show bisma energetic right 
    with moveinright

    b "Hi, Callista. What are you doing here?"

    #show bisma happy at right
    #show callista normal at left

    j "Just taking a whiff of fresh air before doing my homework."
    j "What are you doing here then?"

    show bisma happy right

    b "Just enjoying the beauty of this place."

    stop music

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
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45

    show callista blushing left 

    voice callistaVoiceScene14A+"Scene 14_HJ_1_Final.mp3"
    j "That’s so nice of you."

    b "Well, do you want to take a walk together?"

    j "Sure."

    hide bisma
    hide callista
    with dissolve

    "{i}Bisma and Callista enjoyed their time walking together, but it’s getting late.{/i}"

    show callista focused left 
    show bisma smile right 
    with dissolve

    j "The sun is gonna set. I should go home now."

    b "Do you want me to accompany you?"
    b "Just in case something bad happens."

    j "Sure."

    stop music
    return

label scene_14A_choice2:
    $ Skor -= 10
    play music "audio/Musics/3-Taman_Dog and Pony Show.mp3" volume 0.45

    show callista mad left

    voice callistaVoiceScene14A+"Scene 14_HJ_2_Final.mp3"
    j "How dare you say that?"

    b "I’m sorry. I know that’s not appropriate for me to say."

    j "Glad that you admit your wrongdoing."

    b "Where are you going now?"

    show callista focused left #show callista normal

    j "I was just taking in the fresh air, but now I’m gonna go home and do my homework."

    b "Well, may I accompany you to your home as a form of apology?"
    b "Just in case something bad happens."

    j "Fine then, you could."

    stop music
    return