let fontsize = 12

function listenerInit(){
    document.getElementById('increment').addEventListener('click', incrementLetter)
    document.getElementById('decrement').addEventListener('click', decrementLetter)
    document.getElementById('tituloexemplo').addEventListener('click', writeMesage)
    document.getElementById('layoutmore').addEventListener('click', moreLayout)
    document.getElementById('layoutless').addEventListener('click', lessLayout)
    document.getElementById('showMenu').addEventListener('click', showMenu)
    document.getElementById('hideMenu').addEventListener('click', hideMenu)
}

function hideMenu() {
    document.getElementById('cabecalho').style.display = 'none'
    document.getElementById('conteudo').style.width = '100%'
    document.getElementById('referencias').style.width = '100%'
    document.getElementById('showMenu').style.display = 'inline'
    document.getElementById('hideMenu').style.display = 'none'
}

function showMenu() {
    document.getElementById('cabecalho').style.display = 'flex'
    document.getElementById('conteudo').style.width = '80%'
    document.getElementById('referencias').style.width = '80%';
    document.getElementById('showMenu').style.display = 'none'
    document.getElementById('hideMenu').style.display = 'inline'

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

function decrementLetter() {
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