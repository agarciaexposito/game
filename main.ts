radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber >= 10) {
        basic.showString("Perdí!!")
    } else {
        if (numPulsacion < receivedNumber) {
            basic.showIcon(IconNames.Sad)
        } else if (numPulsacion > receivedNumber) {
            basic.showIcon(IconNames.Happy)
        } else {
            basic.showIcon(IconNames.Asleep)
        }
    }
})
input.onButtonPressed(Button.A, function () {
    numPulsacion += 1
    radio.sendNumber(numPulsacion)
    if (numPulsacion == 10) {
        basic.showString("Ganaste!!")
    }
})
input.onButtonPressed(Button.AB, function () {
    numPulsacion = 0
})
let numPulsacion = 0
numPulsacion = 0
