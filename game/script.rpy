# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hazu-chan")
define j = Character("Callista")
define v = Character("Kazuo")
define w = Character("Darren")
define b = Character("Bisma")
define c = Character("Lucky")
define i = Character("Interviewer")


# The game starts here.
﻿
label start:

    call variables

    scene 1
    
    i "Welcome, Callista to Nico Show! How's your day?"

    #show callista happy

    j "It's been good."
    i "Great! Why don't you introduce yourself to the audience?"

    #show callista normal

    j "Hello! I’m Callista, a VTuber known as Hazu-Chan and a college student at BIT."
    i "That University is known for its hard tests. How do you balance work and study?"
    j "I have made a fixed schedule for streaming and studying so that I’m not left behind in my study and can still stream."
    i "Do you have any tutor for your study?"
    j "Currently not. I’m still able to study and find all of the references I need by myself."
    i "Wow, smart and talented. You’re one gifted person. So, may we know why you pursue a career as a VTuber?"

    #show callista happy

    j "I loved to watch many VTuber. I often watch their streams in my free time. I’m inspired to be like one of them and stream to an audience."
    j "I wanted to create a loving audience and entertain them. I also love to play games and sometimes make music."
    i "Such a wonderful intention. May we know who your inspiration is?"

    #show callista normal

    j "It’s actually another VTuber around my age. His VTuber name is Kazuo and I’ll love to stream with him some day."
    i "Interesting. I hope you will fulfil your dreams. So, moving on. Under the current situation, how does the pandemic affect your work and study?"

    #show callista sad

    j "The pandemic has impacted my life a lot."
    j "I have a harder time studying than I normally do. At college, it’s hard for me to find a new friend. I didn’t have many chances of talking to any of my classmates outside of class."

    #show callista happy
    j "’m glad I have a best friend, Lucky that’s always by my side. Also, she’s the one who made my VTuber model. You all should check her out."

    #show callista normal
    
    j "Despite all of that, I’m glad of the chances that appear because of the pandemic."
    j "Because I spent a lot more time inside, I started to think that I shouldn’t waste all of this free time, so I started to stream as a VTuber. Without it, I won’t be the VTuber that I am now."
    i "Such a lovely story we heard today. I think everyone should be inspired by J to not waste time and use it to better ourselves."
    i "So that’s it for today's interview.\nThank you, Callista, for coming here today.\nSee you all next time on Nico Show!"

    scene Opening

    scene 2-4

    scene 5
    menu:
        "nerima flirt":
            Skor += 10
        "nolak flirt":
            Skor -= 10

    scene 6
    menu:
        "suka":
            Skor += 10
        "ga":
            Skor -= 10

    scene 7
    menu:
        "ikut band bareng B":
            Skor += 30
            call Eight_Nine_A
        "collab bareng V":
            Skor -= 30
            call Eight_Nine_B

    scene 10
    menu:
        "ngobrol bareng B":
            Skor += 10
        "ngechat sama V":
            Skor -= 10

    scene 11
    menu:
        "nanya ke B":
            Skor += 10
        "nanya ke V":
            Skor -10

    scene 12
    menu:
        "ngerjain tugas ukm bareng B":
            Skor += 30
            call Thirteen_Fourteen_A
        "videocall bareng V":
            Skor -= 30
            call Thirteen_Fourteen_B

    scene 15-16

    if Skor > 0:
        call Seventeen_A
    else:
        call Seventeen_B

    scene 18
    menu:
        "ke amusement park bareng B":
            Skor += 30
        "ke amusement park bareng V":
            Skor -= 30

    if Skor > 49:
        jump END1
    elif Skor < -49:
        jump END2
    else:
        jump END3

label variables:
    $ Skor = 0
    return

label Eight_Nine_A:
    scene 8A
    scene 9A
    return
label Eight_Nine_B:
    scene 8B
    scene 9B
    return

label Thirteen_Fourteen_A:
    scene 13A
    scene 14A
    return
label Thirteen_Fourteen_B:
    scene 13B
    scene 14B
    return

label Seventeen_A:
    scene 17A
    return
label Seventeen_B:
    scene 17B
    return

label END1:
    scene END1
label END2:
    scene END2
label END3:
    scene END3
