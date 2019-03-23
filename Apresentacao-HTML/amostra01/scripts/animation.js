function listeners() {
    document.getElementById('alertar').addEventListener('click', alerta)
}

function alerta() {
    alert('Funcionou, estranho!')
}

addEventListener('load', listeners)