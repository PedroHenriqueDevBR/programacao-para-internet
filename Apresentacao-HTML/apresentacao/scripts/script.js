let fontsize = 12

function listenerInit(){
    document.getElementById('increment').addEventListener('click', incrementLetter)
    document.getElementById('decrement').addEventListener('click', decrementLetter)
    document.getElementById('tituloexemplo').addEventListener('click', writeMesage)
    document.getElementById('layoutmore').addEventListener('click', moreLayout)
    document.getElementById('layoutless').addEventListener('click', lessLayout)
}

function moreLayout(){
    let elementos = document.getElementsByTagName('section')
    for (let i = 0; i < elementos.length; i++){
        elementos[i].style.width = '95%'
    }
}

function lessLayout() {
    let elementos = document.getElementsByTagName('section')
    for (let i = 0; i < elementos.length; i++) {
        elementos[i].style.width = '80%'
    }
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

function writeMesage() {
    let theElement = document.getElementById('tituloexemplo')
    theElement.innerHTML = ''
    let newMesage = 'Digo, mão no código'

    for (let i = 0; i < newMesage.length; i++) {
        setTimeout(() => {
            theElement.innerHTML += newMesage[i]
            // console.log(newMesage[i])
            // console.log('ads')
        }, 100 * i);
    }
}

addEventListener('load', listenerInit)