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
image bg 7:
    "Backgrounds/7-Kamar1"
image bg 8:
    "Backgrounds/8-Amusement Park.png"
image bg 9:
    "Backgrounds/9-Sea.png"

# declare chara sprites
# sebenernya asal file gak usah asal var-nya huruf kecil semua

image dummyJ smile:
    "Dummies/characters/dummyJ/dummyJ smile.png"
    zoom 0.67
image dummyJ wonder:
    "Dummies/characters/dummyJ/dummyJ wonder.png"
    zoom 0.67
image dummyJ sad:
    "Dummies/characters/dummyJ/dummyJ sad.png"
    zoom 0.67
image dummyJ upset:
    "Dummies/characters/dummyJ/dummyJ upset.png"
    zoom 0.67

image dummyH neutral:
    "Dummies/characters/dummyH/dummyH neutral.png"
image dummyH happy:
    "Dummies/characters/dummyH/dummyH happy.png"
image dummyH frightened:
    "Dummies/characters/dummyH/dummyH frightened.png"
image dummyH terrified:
    "Dummies/characters/dummyH/dummyH terrified.png"
image dummyH mad:
    "Dummies/characters/dummyH/dummyH mad.png"
image dummyH sad:
    "Dummies/characters/dummyH/dummyH sad.png"

image dummyV neutral:
    "Dummies/characters/dummyV/dummyV neutral.png"
    zoom 0.65
image dummyV happy:
    "Dummies/characters/dummyV/dummyV happy.png"
    zoom 0.65
image dummyV surprised:
    "Dummies/characters/dummyV/dummyV surprised.png"
    zoom 0.65
image dummyV angry:
    "Dummies/characters/dummyV/dummyV angry.png"
    zoom 0.65
image dummyV sad:
    "Dummies/characters/dummyV/dummyV sad.png"
    zoom 0.65

image dummyB neutral:
    "Dummies/characters/dummyB/Sprite Male Dark Hair Neu01.png"
    zoom 0.6
image dummyB smile:
    "Dummies/characters/dummyB/Sprite Male Dark Hair Smi02.png"
    zoom 0.6
image dummyB confused:
    "Dummies/characters/dummyB/Sprite Male Dark Hair Con01.png"
    zoom 0.6
image dummyB angry:
    "Dummies/characters/dummyB/Sprite Male Dark Hair Ang01.png"
    zoom 0.6
image dummyB sad:
    "Dummies/characters/dummyB/Sprite Male Dark Hair Sad01.png"
    zoom 0.6
image dummyB apologize:
    "Dummies/characters/dummyB/Sprite Male Dark Hair Apo01.png"
    zoom 0.6

image dummyC normal:
    "Dummies/characters/dummyC/taishiro outing normal.png"
    zoom 0.65
image dummyC happy:
    "Dummies/characters/dummyC/taishiro outing happy.png"
    zoom 0.65
image dummyC surprised:
    "Dummies/characters/dummyC/taishiro outing surprised.png"
    zoom 0.65
image dummyC angry:
    "Dummies/characters/dummyC/taishiro outing angry.png"
    zoom 0.65
image dummyC sad:
    "Dummies/characters/dummyC/taishiro outing sad.png"
    zoom 0.65

image callista normal:
    "Chara/irl_hazu.png"
    zoom 0.49

# The game starts here.
label start:
    #scene 1
    call scene_1

    scene Opening

    #scene 2-4
    call scene_2
    call scene_3
    call scene_4

    #scene 5
    call scene_5

    #scene 6
    call scene_6

    #scene 7
    call scene_7

    #scene 8-9 sudah di scene_7

    #scene 10
    call scene_10

    #scene 11
    call scene_11

    #scene 12
    call scene_12

    #scene 13-14 sudah di scene_12

    #scene 15-16
    call scene_15
    call scene_16

    if not Darren_Reveal:
        call scene_17A
    else:
        call scene_17B

    #scene 18
    call scene_18

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

