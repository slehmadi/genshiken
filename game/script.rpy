# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("H")
define b = Character("B")
define v = Character("V")


# The game starts here.
﻿
label start:

    call variables

    scene 1

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
