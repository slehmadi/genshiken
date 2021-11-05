define interviewerVoice = "audio/Dubs/Interviewer/"
define callistaVoiceScene1 = "audio/Dubs/J-H/Scene 1/"

label scene_1:
    scene black #scene bg interviewRoom

    "VTuber agency is not rare nowadays"
    "In a room, sit two people facing each other, a girl and a man with suit."
    "..."

    scene bg 1
    play music "audio/Musics/1-Kelas_Slow Steps.mp3" volume 0.1

    voice interviewerVoice+"Scene 1_I_1_Final.mp3"
    i "Welcome, Callista to Nico Show! How's your day?"

    show callista normal #show callista happy

    voice callistaVoiceScene1+"Scene 1_HJ_1_Final.mp3"
    j "It's been good."

    voice interviewerVoice+"Scene 1_I_2_Final.mp3"
    i "Great! Why don't you introduce yourself to the audience?"

    #show dummyJ wonder #show callista normal

    voice callistaVoiceScene1+"Scene 1_HJ_2_Final.mp3"
    j "Hello! I’m Callista, a VTuber known as Hazu-Chan and a college student at BIT."

    voice interviewerVoice+"Scene 1_I_3_Final.mp3"
    i "That University is known for its hard tests. How do you balance work and study?"

    voice callistaVoiceScene1+"Scene 1_HJ_3_Final.mp3"
    j "I have made a fixed schedule for streaming and studying so that I’m not left behind in my study and can still stream."

    voice interviewerVoice+"Scene 1_I_4_Final.mp3"
    i "Do you have any tutor for your study?"

    voice callistaVoiceScene1+"Scene 1_HJ_4_Final.mp3"
    j "Currently not. I’m still able to study and find all of the references I need by myself."

    voice interviewerVoice+"Scene 1_I_5_Final.mp3"
    i "Wow, smart and talented. You’re one gifted person. So, may we know why you pursue a career as a VTuber?"

    #show dummyJ smile #show callista happy

    voice "<to 9.9>"+callistaVoiceScene1+"Scene 1_HJ_5_Final.mp3"
    j "I loved to watch many VTuber. I often watch their streams in my free time. I’m inspired to be like one of them and stream to an audience."
    
    voice "<from 10>"+callistaVoiceScene1+"Scene 1_HJ_5_Final.mp3"
    j "I wanted to create a loving audience and entertain them. I also love to play games and sometimes make music."

    voice interviewerVoice+"Scene 1_I_6_Final.mp3"
    i "Such a wonderful intention. May we know who your inspiration is?"

    #show dummyJ wonder #show callista normal

    voice callistaVoiceScene1+"Scene 1_HJ_6_Final.mp3"
    j "It’s actually another VTuber around my age. His VTuber name is Kazuo and I’ll love to stream with him some day."

    voice interviewerVoice+"Scene 1_I_7_Final.mp3"
    i "Interesting. I hope you will fulfil your dreams. So, moving on. Under the current situation, how does the pandemic affect your work and study?"

    #show dummyJ sad #show callista sad

    voice "<to 4>"+callistaVoiceScene1+"Scene 1_HJ_7_Final.mp3"
    j "The pandemic has impacted my life a lot."

    voice "<from 4.5 to 17>"+callistaVoiceScene1+"Scene 1_HJ_7_Final.mp3"
    j "I have a harder time studying than I normally do. At college, it’s hard for me to find a new friend. I didn’t have many chances of talking to any of my classmates outside of class."

    #show dummyJ smile #show callista happy

    voice "<from 18 to 27.5>"+callistaVoiceScene1+"Scene 1_HJ_7_Final.mp3"
    j "I’m glad I have a best friend, Lucky that’s always by my side. Also, he’s the one who made my VTuber model. You all should check him out."

    #show dummyJ wonder #show callista normal
    
    voice "<from 27.5 to 32.5>"+callistaVoiceScene1+"Scene 1_HJ_7_Final.mp3"
    j "Despite all of that, I’m glad of the chances that appear because of the pandemic."

    voice "<from 32.5>"+callistaVoiceScene1+"Scene 1_HJ_7_Final.mp3"
    j "Because I spent a lot more time inside, I started to think that I shouldn’t waste all of this free time, so I started to stream as a VTuber. Without it, I won’t be the VTuber that I am now."
    
    voice "<to 7.6>"+interviewerVoice+"Scene 1_I_8_Final.mp3"
    i "Such a lovely story we heard today. I think everyone should be inspired by Callista to not waste their time and use it to better ourselves."
    
    voice "<from 7.9>"+interviewerVoice+"Scene 1_I_8_Final.mp3"
    i "So that’s it for today's interview. Thank you, Callista, for coming here today. See you all next time on Nico Show!"

    stop music fadeout 0.2
    return