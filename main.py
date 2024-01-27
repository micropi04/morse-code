def on_received_number(receivedNumber):
    music.play(music.string_playable("C5 B - - - - - - ", 199),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("-")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("•")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_icon(IconNames.SMALL_DIAMOND)
    music.play(music.string_playable("C5 - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_number(-1)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)