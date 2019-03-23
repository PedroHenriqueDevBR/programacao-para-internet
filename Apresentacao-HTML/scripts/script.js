var fontsize = 12

function listenerInit(){
    document.getElementById('increment').addEventListener('click', incrementLetter)
    document.getElementById('decrement').addEventListener('click', decrementLetter)
}

function incrementLetter() {
    fontsize++
    elements = document.getElementsByTagName('section')
    for (element of elements) {
        element.style.fontSize = fontsize + 'pt'
        document.getElementById('config').style.fontSize = '12pt'
    }
}

function decrementLetter(params) {
    fontsize--
    elements = document.getElementsByTagName('section')
    for (element of elements) {
        element.style.fontSize = fontsize + 'pt'
        document.getElementById('config').style.fontSize = '12pt'
    }
}

addEventListener('load', listenerInit)