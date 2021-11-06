define kazuoVoiceScene2 = "audio/Dubs/V-W/Scene 2/"
define callistaVoiceScene2 = "audio/Dubs/J-H/Scene 2/"

label scene_2:
    scene black
    with dissolve
    "{i}A year later...{/i}"
    "{i}Hazu-chan and Kazuo is in a heated game of Apex Legends.{/i}"

    scene bg 2
    with dissolve

    pause(1.0)
    show kazuo focused left
    with dissolve

    v "There’s one team nearby. We should hide here for a while."

    show hazu focused right
    with dissolve

    h "Okay. I can hear them too."

    show kazuo confused left #show kazuo confused
    voice kazuoVoiceScene2+"Scene 2_V_1_Final.mp3"
    v "What happened? Suddenly there are only four teams left."

    show hazu surprised right #show hazu surprise
    voice callistaVoiceScene2+"Scene 2_HJ_1_Final.mp3"
    h "Woah, I just noticed that too."

    voice kazuoVoiceScene2+"Scene 2_V_2_Final.mp3"
    v "Wait, are they coming to us?"
    v "..."
    
    show kazuo focused left #show kazuo panic
    v "They’re coming, they’re coming."

    show hazu focused right #show hazu intense
    h "I’m using my ult."

    #show dummyV angry #show kazuo intense
    voice kazuoVoiceScene2+"Scene 2_V_3_Final.mp3"
    v "Nice. I’m throwing a grenade."

    #show dummyV neutral #show kazuo focused
    v "They’re coming close. Let’s fight them here."

    show hazu focused right #show hazu focused
    h "Understood."

    play sound "audio/Sound Effects/sfx1.mp3" volume 0.5
    "{i}They do an intense battle.{/i}"

    stop sound fadeout 0.2
    v "One down. Be careful! There’s an enemy near you."

    show hazu sad right #show hazu sad
    voice callistaVoiceScene2+"Scene 2_HJ_2_Final.mp3"
    h "Oh no I died! He’s so low!"

    v "Leave it to me."

    play sound "audio/Sound Effects/sfx1.mp3" volume 0.5
    "{i}Kazuo shoot all enemies infront them.{/i}"

    stop sound fadeout 0.2
    show hazu happy right #show hazu happy
    h "Nice! You got them! You killed both of them with ease!"
    h "So this is how playing with a Master rank feels like."
    
    #show dummyV happy #show kazuo happy
    v "Nah, that’s just a rusty play by me."

    # #show kazuo normal
    v "Hold on, let me res you."

    show hazu happy right #show hazu happy
    h "Thank youuu."

    v "There’s only two teams left. Let's go, Hazu. We can win this game."

    show hazu focused right #show hazu normal
    h "Great, I will be helping you from behind."

    v "Wait, I saw a player. I think he’s playing solo."
    v "He went to the top of that building. Let me try to snipe him."

    play sound "audio/Sound Effects/sfx2.mp3" volume 0.5
    "{i}Kazuo snipe enemy in building using his kraber.{/i}"

    stop sound fadeout 0.2
    v "I hit him! His armor broke. I’m gonna chase him."

    h "Wait! I need to heal first."

    v "Don’t worry, I’ll let you get the last hit."
    v "Hazu, over here!"
    v "He’s coming to you."

    play sound "audio/Sound Effects/sfx2.mp3" volume 0.5
    "{i}Kazuo prevent the enemy who comes after hazu.{/i}"

    stop sound fadeout 0.2
    v "I hit him again! He’s so low."

    show hazu surprised right #show hazu surprised
    h "Oh, wait! Aaah, he’s here!"

    play sound "audio/Sound Effects/sfx1.mp3" volume 0.5
    "{i}Hazu gives her best to kills the enemy infornt her.{/i}"

    stop sound fadeout 0.2
    #show dummyV happy #show kazuo happy
    v "You got him, Hazu!"

    show hazu happy right #show hazu happy
    h "WOOO! I got him!"
    h "We are the Champions!"

    voice kazuoVoiceScene2+"Scene 2_V_4_Final.mp3"
    v "Nice! GG!"

    voice callistaVoiceScene2+"Scene 2_HJ_3_Final.mp3"
    h "Woah, GG!"
    h "I never thought I would be able to be the Champions."
    h "Kazuo! You carried me really hard in that game. Thank youuu."

    v "Nah, we won because of you, Hazu. You got that last kill."

    h "Holy crap, we just won an Apex Legends game. Thank you, Kazuo!"
    h "I feel like I should give you something in return."

    v "I don’t need anything, tho."
    v "But yeah, that was a lot of fun."

    voice callistaVoiceScene2+"Scene 2_HJ_4_Final.mp3"
    h "Yeah, that was so fun."
    h "Oh my god! Thank you so much for all the superchat, guys!"
    h "I never imagined my first win to be on stream."

    v "That’s good isn’t it? Everyone just saw the birth of a new Apex Predator."

    show hazu energetic right #show hazu energetic
    voice callistaVoiceScene2+"Scene 2_HJ_5_Final.mp3"
    h "Sure. Yes. Listen guys, on the next stream, I will be playing ranked."
    h "And in one week, I will become a Predator!"
    h "Actually, what the hell am I saying?"

    show hazu laugh right #show hazu laugh
    h "Where does this confidence come all of the sudden? Hahaha"

    #show kazuo laugh
    v "Well, we’ll see about that, hahaha."

    #show dummyV neutral #show kazuo normal
    v "Anyway, what a way to end this stream. Damn, we’ve been streaming for four hours."
    v "I thought we would just play Minecraft for today’s stream. Never thought we would close it like this."

    show hazu focused right #show hazu normal
    h "Thankfully the Minecraft server went down halfway through the stream, ahaha, otherwise I won’t experience my first win."
    h "Anyways, I think we should close the stream now. It’s already late."
    h "Gosh, I should pay more attention to my stream duration."

    show hazu happy right #show hazu happy
    h "And Kazuo, thank you for collabing with me tonight."

    #show dummyV happy #show kazuo happy
    v "Thank you to you too, Hazu. It’s been a fun stream."

    h "Well then. We will stop the stream now. Thank you so much for coming in."
    h "Again, thank you for all the superchat, I will be reading them on my next stream."
    h "Kazuo, do you have anything to say?"

    v "Thank you for coming to our stream. We appreciate all the support and love."

    show kazuo confused left #show kazuo confused
    v "And umm…what else…"

    h "I think that’s it? Anyway, have a good night everyone! Sleep well." 
    h "And we will see you guys in the next stream. Bye bye!"

    v "Bye bye!"

    scene black
    with dissolve
    "{i}...{/i}"
    scene bg 2
    with dissolve

    play music "audio/Musics/2-Kamar_Easy Feeling.mp3" volume 0.45

    show callista focused left
    with dissolve

    voice callistaVoiceScene2+"Scene 2_HJ_6_Final.mp3"
    j "Fuaah, that was a fun stream."

    show callista tired left #show callista tired
    j "I feel kinda sleepy now."

    show kazuo focused right
    with dissolve

    voice kazuoVoiceScene2+"Scene 2_V_5_Final.mp3"
    v "Thank god it ended. I’m a bit worried there because you said earlier that your college will start tomorrow."
    
    #show kazuo focused
    v "You should take a rest. It’s already this late."

    j "I know. But you know, kazuo, no college students sleep early these days."
    j "I bet my friends are still awake right now."

    #show dummyV happy #show kazuo laugh
    v "Oh, wow. I thought you don’t have any friends in college."

    show callista mad left #show callista angry
    j "..."

    v "What’s with that silence? I’m just joking."
    v "Isn’t that what you always told me?"

    #show callista smirk
    voice callistaVoiceScene2+"Scene 2_HJ_7_Final.mp3"
    j "Hmmph, what are you saying?"
    j "I do have friends…"
    j "…well, two friends, not including you."

    #show kazuo focused
    v "Then isn’t tomorrow a great chance to make lots of friends?"
    v "You said you like to spend time alone, but…"
    v "...I know that  you’re feeling kinda lonely at times, right?"

    #show callista surprised
    j "How can you say that? Can you read my mind or something?"

    v "It’s just my instinct."

    show callista thinking left #show callista confused
    j "Huhh…"

    v "In the end, I don’t want to told you everything about what you should do."
    v "Just do things that you likes and try your best at achieving your goals."
    v "That’s just a little advice from me."

    #show callista thinking
    j "Yeah…"

    v "Even if things don’t go well, or if you feel lonely again, you can always play games with me, right?"

    show callista happy left #show callista smile
    j "Yeah…, thanks for the words."

    #show dummyV neutral #show kazuo normal
    v "Okay then, I think I will go now."
    v "Thanks for collab. Sleep well, Callista, and have a good night.\nBye!"

    j "Okay, bye!"

    play sound "audio/Sound Effects/sfx4.mp3"
    hide kazuo
    with dissolve

    show callista thinking left #show callista thinking
    j "{i}Huh…, guess I better check on my friends.{/i}"

    return