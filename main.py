def on_received_number(receivedNumber):
    if receivedNumber >= 10:
        basic.show_string("Perdí!!")
    else:
        if numPulsacion < receivedNumber:
            basic.show_icon(IconNames.SAD)
        elif numPulsacion > receivedNumber:
            basic.show_icon(IconNames.HAPPY)
        else:
            basic.show_icon(IconNames.ASLEEP)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global numPulsacion
    numPulsacion += 1
    radio.send_number(numPulsacion)
    if numPulsacion == 10:
        basic.show_string("Ganaste!!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global numPulsacion
    numPulsacion = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

numPulsacion = 0
numPulsacion = 0