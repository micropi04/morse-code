radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    music.play(music.stringPlayable("C5 B - - - - - - ", 199), music.PlaybackMode.UntilDone)
    basic.showString("-")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("•")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showIcon(IconNames.SmallDiamond)
    music.play(music.stringPlayable("C5 - - - - - - - ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(-1)
})
radio.setGroup(1)
