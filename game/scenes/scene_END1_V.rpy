
label scene_END1_V:
    scene bg 8
    with dissolve

    play music "audio/Musics/4-Amusement Park_How It Began.mp3" volume 0.45

    "{i}Callista is standing in the front of the amusement park.{/i}"

    show callista focused center
    with dissolve

    j "Where’s Darren? He’s supposed to be here now."

    hide callista
    with dissolve

    "{i}Callista waited for another hour, but Darren never came.{/i}"

    show callista sad left
    with dissolve
    
    j "Maybe I should just leave."

    show bisma normal right #show bisma normal
    with moveinright

    b "Hi there, Callista."
    b "What are you doing here?"

    #hide bisma
    show callista focused left 

    j "You scared me, Bisma"

    #show callista normal at left
    #show bisma normal at right

    j "I’m just waiting for Darren, he’s supposed to be here an hour ago."

    b "Who’s Darren?"

    j "It’s unimportant."
    j "It’s sad that he still hasn't come yet."

    b "Well, whoever that guy is, he’s an asshole for leaving you alone."
    b "Instead of waiting here, why don’t you come with me?"

    j "{i}I don’t think Darren is coming.{/i}"
    j "{i}I guess there’s nothing wrong with going with Bisma.{/i}"
    j "But do you still have an extra ticket?"

    show bisma happy right 

    b "Of course. I kept it just in case you suddenly want to go with me, just like now. "

    show bisma energetic right 

    b "Let’s go inside then."

    #show callista energetic

    j "Let’s go."

    hide callista
    hide bisma
    with dissolve

    "{i}Bisma and Callista spends their entire day together in the amusement park.{/i}"
    "{i}They ride the roller coaster together and scream out their lungs.{/i}"
    "{i}But the sun must set and it’s the time for them to leave.{/i}"

    show callista happy left 
    show bisma happy right 
    with dissolve

    j "Thank you so much for today, Bisma."
    j "I really enjoyed today."

    #show callista happy at left
    #show bisma happy at right

    b "It has been such a great time spending time with you."
    b "Also, I wanted you to come to a special place next week."

    show callista focused left 

    j "Where is it?"

    #show bisma normal right 

    b "It’s a secret. I will bring you there when the time comes."
    b "I know about that place because of someone."

    j "Okay then, Bisma. I will surely come with you."
    j "Well, the sun’s setting and I have to go."
    j "Good bye for now, Bisma."

    b "Good bye for now too, Callista."

    hide bisma
    hide callista
    with dissolve

    "{i}Bisma and Callista went to their own home.{/i}"

    show callista focused center
    with dissolve 

    j "{i}I still don’t see Darren anywhere today. Maybe he really did forget about me.{/i}"

    scene black
    with dissolve

    "{i}The Next Day.{/i}"

    scene 7
    with dissolve

    show callista focused center
    with dissolve

    j "Why is Darren not answering any of my calls or texts?"
    j "Where did he go?"
    j "I was supposed to collab with him today."
    j "{i}Is he angry at me for not going to the amusement park with him.{/i}"
    j "Well, if he doesn't want to collab with me today, maybe I could just play music with Bisma."

    hide callista
    with dissolve

    "{i}Callista calls Bisma.{/i}"

    #show bisma normal
    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    b "Hey, Callista. Why are you calling me at this time?"

    #show bisma normal at right
    #show callista normal at left

    j "I was supposed to stream with Kazuo today, but he didn’t answer my text."
    j "Do you want to be a guest in my stream?"
    j "We could play music together."

    b "Sure, it’ll be a great experience."

    #hide callista
    #hide bisma
    scene bg 2
    with dissolve

    "{i}Callista introduces Bisma to her audience and starts playing music together.{/i}"
    "{i}Then they talk after the streams end.{/i}"

    show callista focused left
    show bisma normal right
    with dissolve

    j "So you’re aren’t telling me where we’re gonna go next weekend?"

    b "Not yet."
    b "Well, it’s already night and you should rest."
    b "I could see you using all of your energy playing music today."

    j "Yeah, maybe I was too excited."
    j "Well, see you soon then."
    j "Bye, Bisma."

    b "Bye, Callista."

    stop music
    scene bg 3
    with dissolve

    "{i}Callista sit on her bed and checks her phone.{/i}"

    show callista focused center 
    with dissolve

    j "Wait, that can’t be."
    j "Kazuo is streaming right now."
    j "Then why did he ignore my message?"
    j "{i}Is it my fault?{/i}"
    j "{i}No, remember what Lucky said.{/i}"
    j "{i}The past is gone, I should just focus on the future.{/i}"
    j "This is just the end of a path, a new chance will come to me."
    j "I should just move on and let Kazuo do his own thing."
    j "Not everything could stay the same forever."

    scene black
    with dissolve

    "{i}The Next Weekend.{/i}"

    scene bg 9
    with dissolve

    "{i}Bisma brings Callista to a place near a cliff with a wonderful view of the sea.{/i}"
    "{i}they sit on a bench facing to the sea.{/i}"

    play music "audio/Musics/5-Tempat Indah_Memories of Love.mp3" volume 0.45

    show callista focused left 
    show bisma normal right 
    with dissolve

    j "This place is really beautiful."
    j "Why do you want to bring me here?"

    #show callista normal at left
    #show bisma normal at right

    b "I want to tell you something."

    j "What is it?"

    b "Do you want to go on a date with me?"

    show callista thinking left

    j "…"
    pause(1.0)

    show callista happy left 

    j "Of course, after everything you’ve done."

    show bisma happy right 

    b "I’m so happy, I’m out of words."

    hide callista
    hide bisma
    with dissolve

    "{i}They both keep smiling to each other, but then Callista’s smile fade away.{/i}"

    show callista focused left
    show bisma normal right
    with dissolve

    b "Hey, Callista, is there something wrong?"

    j "There’s nothing wrong."

    b "Then why do you look worried all of a sudden?"

    show callista sad left 

    voice "audio/Dubs/J-H/Bad ending/Bad Ending_HJ_Final.mp3"
    j "I...I don’t think I made the right choice…"
    j "…."

    scene black

    "{i}The End..?{/i}"

    stop music
    return