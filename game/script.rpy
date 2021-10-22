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
default Skor = 0

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

# The game starts here.
label start:
    call variables

    #scene 1
    call scene_1

    scene Opening

    #scene 2-4
    call scene_2
    call scene_3
    call scene_4

    scene 5
    call scene_5

    scene 6
    call scene_6

    scene 7
    call scene_7

    scene 10
    call scene_10

    scene 11
    call scene_11

    scene 12
    call scene_12

    scene 15-16

    if Skor > 0:
        call Seventeen_A
    else:
        call Seventeen_B

    scene 18
    menu:
        "ke amusement park bareng B":
            $ Skor += 30
        "ke amusement park bareng V":
            $ Skor -= 30

    if Skor > 29:
        jump END1
    elif Skor < -29:
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
