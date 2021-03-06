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

# variables

default Skor = 0
default Darren_Reveal = False
default choose_with = "X"

# declare background name

image bg 1:
    "Backgrounds/1-Couch.png"
    zoom 0.8
image bg 2:
    "Backgrounds/2-PC2.png"
    zoom 0.8
image bg 3:
    "Backgrounds/3-Kamar2.png"
    zoom 0.75
image bg 4:
    "Backgrounds/4-Taman.png"
image bg 5:
    "Backgrounds/5-Stage.png"
    zoom 0.8
image bg 6:
    "Backgrounds/6-Kelas.png"
    zoom 0.8
image bg 7:
    "Backgrounds/7-Kamar1.png"
    zoom 0.8
image bg 8:
    "Backgrounds/8-Amusement Park.png"
    zoom 0.8
image bg 9:
    "Backgrounds/9-Sea.png"
    zoom 0.8

# declare chara sprites
# sebenernya asal file gak usah asal var-nya huruf kecil semua

image callista blushing center:
    "Chara/callista/callista blushing.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista blushing left:
    "Chara/callista/callista blushing.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista blushing right:
    "Chara/callista/callista blushing.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista focused center:
    "Chara/callista/callista focused.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista focused left:
    "Chara/callista/callista focused.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista focused right:
    "Chara/callista/callista focused.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista happy center:
    "Chara/callista/callista happy.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista happy left:
    "Chara/callista/callista happy.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista happy right:
    "Chara/callista/callista happy.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista laugh center:
    "Chara/callista/callista laugh.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista laugh left:
    "Chara/callista/callista laugh.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista laugh right:
    "Chara/callista/callista laugh.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista mad center:
    "Chara/callista/callista mad.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista mad left:
    "Chara/callista/callista mad.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista mad right:
    "Chara/callista/callista mad.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista sad center:
    "Chara/callista/callista sad.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista sad left:
    "Chara/callista/callista sad.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista sad right:
    "Chara/callista/callista sad.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista thinking center:
    "Chara/callista/callista thinking.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista thinking left:
    "Chara/callista/callista thinking.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista thinking right:
    "Chara/callista/callista thinking.png"
    zoom 0.275
    anchor(0.0, 0.85)
image callista tired center:
    "Chara/callista/callista tired.png"
    zoom 0.275
    anchor(0.5, 0.85)
image callista tired left:
    "Chara/callista/callista tired.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.85)
image callista tired right:
    "Chara/callista/callista tired.png"
    zoom 0.275
    anchor(0.0, 0.85)

image hazu energetic center:
    "Chara/hazu chan/hazu energetic.png"
    zoom 0.275
    anchor(0.5, 0.75)
image hazu energetic left:
    "Chara/hazu chan/hazu energetic.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.75)
image hazu energetic right:
    "Chara/hazu chan/hazu energetic.png"
    zoom 0.275
    anchor(0.0, 0.75)
image hazu focused center:
    "Chara/hazu chan/hazu focused.png"
    zoom 0.275
    anchor(0.5, 0.75)
image hazu focused left:
    "Chara/hazu chan/hazu focused.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.75)
image hazu focused right:
    "Chara/hazu chan/hazu focused.png"
    zoom 0.275
    anchor(0.0, 0.75)
image hazu happy center:
    "Chara/hazu chan/hazu happy.png"
    zoom 0.275
    anchor(0.5, 0.75)
image hazu happy left:
    "Chara/hazu chan/hazu happy.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.75)
image hazu happy right:
    "Chara/hazu chan/hazu happy.png"
    zoom 0.275
    anchor(0.0, 0.75)
image hazu laugh center:
    "Chara/hazu chan/hazu laugh.png"
    zoom 0.275
    anchor(0.5, 0.75)
image hazu laugh left:
    "Chara/hazu chan/hazu laugh.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.75)
image hazu laugh right:
    "Chara/hazu chan/hazu laugh.png"
    zoom 0.275
    anchor(0.0, 0.75)
image hazu sad center:
    "Chara/hazu chan/hazu sad.png"
    zoom 0.275
    anchor(0.5, 0.75)
image hazu sad left:
    "Chara/hazu chan/hazu sad.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.75)
image hazu sad right:
    "Chara/hazu chan/hazu sad.png"
    zoom 0.275
    anchor(0.0, 0.75)
image hazu surprised center:
    "Chara/hazu chan/hazu surprised.png"
    zoom 0.275
    anchor(0.5, 0.75)
image hazu surprised left:
    "Chara/hazu chan/hazu surprised.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.75)
image hazu surprised right:
    "Chara/hazu chan/hazu surprised.png"
    zoom 0.275
    anchor(0.0, 0.75)

image kazuo confused center:
    "Chara/kazuo/kazuo confused.png"
    zoom 0.275
    anchor(0.5, 0.9)
image kazuo confused left:
    "Chara/kazuo/kazuo confused.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image kazuo confused right:
    "Chara/kazuo/kazuo confused.png"
    zoom 0.275
    anchor(0.0, 0.9)
image kazuo focused center:
    "Chara/kazuo/kazuo focused.png"
    zoom 0.275
    anchor(0.5, 0.9)
image kazuo focused left:
    "Chara/kazuo/kazuo focused.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image kazuo focused right:
    "Chara/kazuo/kazuo focused.png"
    zoom 0.275
    anchor(0.0, 0.9)
image kazuo surprised center:
    "Chara/kazuo/kazuo surprised.png"
    zoom 0.275
    anchor(0.5, 0.9)
image kazuo surprised left:
    "Chara/kazuo/kazuo surprised.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image kazuo surprised right:
    "Chara/kazuo/kazuo surprised.png"
    zoom 0.275
    anchor(0.0, 0.9)

image darren normal center:
    "Chara/darren/DARREN idle.png"
    zoom 0.275
    anchor(0.5, 0.83)
image darren normal left:
    "Chara/darren/DARREN idle.png"
    zoom 0.275
    xzoom -1 
    anchor(1.0, 0.83)
image darren normal right:
    "Chara/darren/DARREN idle.png"
    zoom 0.275
    anchor(0.0, 0.83)
image darren confused center:
    "Chara/darren/DARREN confused.png"
    zoom 0.275
    anchor(0.5, 0.83)
image darren confused left:
    "Chara/darren/DARREN confused.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.83)
image darren confused right:
    "Chara/darren/DARREN confused.png"
    zoom 0.275
    anchor(0.0, 0.83)
image darren serious center:
    "Chara/darren/DARREN serious.png"
    zoom 0.275
    anchor(0.5, 0.83)
image darren serious left:
    "Chara/darren/DARREN serious.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.83)
image darren serious right:
    "Chara/darren/DARREN serious.png"
    zoom 0.275
    anchor(0.0, 0.83)
image darren surprised center:
    "Chara/darren/DARREN surprised.png"
    zoom 0.275
    anchor(0.5, 0.83)
image darren surprised left:
    "Chara/darren/DARREN surprised.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.83)
image darren surprised right:
    "Chara/darren/DARREN surprised.png"
    zoom 0.275
    anchor(0.0, 0.83)

image bisma normal center:
    "Chara/bisma/BISMA6.png"
    zoom 0.275
    anchor(0.5, 0.9)
image bisma normal left:
    "Chara/bisma/BISMA6.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image bisma normal right:
    "Chara/bisma/BISMA6.png"
    zoom 0.275
    anchor(0.0, 0.9)
image bisma happy center:
    "Chara/bisma/BISMA1.png"
    zoom 0.275
    anchor(0.5, 0.9)
image bisma happy left:
    "Chara/bisma/BISMA1.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image bisma happy right:
    "Chara/bisma/BISMA1.png"
    zoom 0.275
    anchor(0.0, 0.9)
image bisma energetic center:
    "Chara/bisma/BISMA3.png"
    zoom 0.275
    anchor(0.5, 0.9)
image bisma energetic left:
    "Chara/bisma/BISMA3.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image bisma energetic right:
    "Chara/bisma/BISMA3.png"
    zoom 0.275
    anchor(0.0, 0.9)
image bisma thinking center:
    "Chara/bisma/BISMA2.png"
    zoom 0.275
    anchor(0.5, 0.9)
image bisma thinking left:
    "Chara/bisma/BISMA2.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image bisma thinking right:
    "Chara/bisma/BISMA2.png"
    zoom 0.275
    anchor(0.0, 0.9)
image bisma sad center:
    "Chara/bisma/BISMA4.png"
    zoom 0.275
    anchor(0.5, 0.9)
image bisma sad left:
    "Chara/bisma/BISMA4.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image bisma sad right:
    "Chara/bisma/BISMA4.png"
    zoom 0.275
    anchor(0.0, 0.9)
image bisma smirk center:
    "Chara/bisma/BISMA5.png"
    zoom 0.275
    anchor(0.5, 0.9)
image bisma smirk left:
    "Chara/bisma/BISMA5.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image bisma smirk right:
    "Chara/bisma/BISMA5.png"
    zoom 0.275
    anchor(0.0, 0.9)

image lucky normal center:
    "Chara/lucky/1LUCKY.png"
    zoom 0.275
    anchor(0.5, 0.9)
image lucky normal left:
    "Chara/lucky/1LUCKY.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image lucky normal right:
    "Chara/lucky/1LUCKY.png"
    zoom 0.275
    anchor(0.0, 0.9)
image lucky happy center:
    "Chara/lucky/2LUCKY.png"
    zoom 0.275
    anchor(0.5, 0.9)
image lucky happy left:
    "Chara/lucky/2LUCKY.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image lucky happy right:
    "Chara/lucky/2LUCKY.png"
    zoom 0.275
    anchor(0.0, 0.9)
image lucky surprised center:
    "Chara/lucky/3LUCKY.png"
    zoom 0.275
    anchor(0.5, 0.9)
image lucky surprised left:
    "Chara/lucky/3LUCKY.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image lucky surprised right:
    "Chara/lucky/3LUCKY.png"
    zoom 0.275
    anchor(0.0, 0.9)
image lucky sad center:
    "Chara/lucky/4LUCKY.png"
    zoom 0.275
    anchor(0.5, 0.9)
image lucky sad left:
    "Chara/lucky/4LUCKY.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image lucky sad right:
    "Chara/lucky/4LUCKY.png"
    zoom 0.275
    anchor(0.0, 0.9)
image lucky angry center:
    "Chara/lucky/5LUCKY.png"
    zoom 0.275
    anchor(0.5, 0.9)
image lucky angry left:
    "Chara/lucky/5LUCKY.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image lucky angry right:
    "Chara/lucky/5LUCKY.png"
    zoom 0.275
    anchor(0.0, 0.9)
image lucky worried center:
    "Chara/lucky/6LUCKY.png"
    zoom 0.275
    anchor(0.5, 0.9)
image lucky worried left:
    "Chara/lucky/6LUCKY.png"
    zoom 0.275
    xzoom -1
    anchor(1.0, 0.9)
image lucky worried right:
    "Chara/lucky/6LUCKY.png"
    zoom 0.275
    anchor(0.0, 0.9)

# The game starts here.
label start:
    #scene 1
    call scene_1 from _call_scene_1

    scene Opening

    #scene 2-4
    call scene_2 from _call_scene_2
    call scene_3 from _call_scene_3
    call scene_4 from _call_scene_4

    #scene 5
    call scene_5 from _call_scene_5

    #scene 6
    call scene_6 from _call_scene_6

    #scene 7
    call scene_7 from _call_scene_7

    #scene 8-9 sudah di scene_7

    #scene 10
    call scene_10 from _call_scene_10

    #scene 11
    call scene_11 from _call_scene_11

    #scene 12
    call scene_12 from _call_scene_12

    #scene 13-14 sudah di scene_12

    #scene 15-16
    call scene_15 from _call_scene_15
    call scene_16 from _call_scene_16

    if not Darren_Reveal:
        call scene_17A from _call_scene_17A
    else:
        call scene_17B from _call_scene_17B

    #scene 18
    call scene_18 from _call_scene_18

    if Skor > 29:
        if choose_with == "B":
            jump scene_END1_B
        else: #choose_with == "V"
            jump scene_END1_V
    elif Skor < -29:
        if choose_with == "B":
            jump scene_END2_B
        else: #choose_with == "V"
            jump scene_END2_V
    else:
        if choose_with == "B":
            jump scene_END3_B
        else: #choose_with == "V"
            jump scene_END3_V

