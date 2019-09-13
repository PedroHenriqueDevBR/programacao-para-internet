function selecionarPokemon(url) {
    const xhttp = new XMLHttpRequest()
    xhttp.open('Get', url)
    
    const show = document.getElementById('show')
    const nome = document.getElementById('nome-pokemon')
    const habilidades = document.getElementById('habilidades-pokemon')
    const img = document.getElementById('img-pokemon')

    nome.innerHTML = ''
    habilidades.innerHTML = ''
    img.innerHTML = ''
    show.classList.remove('esconde')

    xhttp.onreadystatechange = () => {
        if (xhttp.status === 200) {
            const dados = JSON.parse(xhttp.responseText)
            nome.innerHTML = dados.name
            img.innerHTML = `
            <img src="${dados.sprites.front_default}" class="img-fluid" style="width: 200px; id='img-pokemon-src">
            `

            for (habilidade of dados.abilities) {
                habilidades.innerHTML += `
                <li class="list-group-item">${habilidade.ability.name}</li>
                `
            }

        } else {
            console.log('erro')
        }
    }

    xhttp.send()
}

function mostrarPokemons(url) {
    const xhttp = new XMLHttpRequest()

    xhttp.open('Get', url)
    xhttp.onreadystatechange = () => {
        if (xhttp.status === 200){
            const dados = JSON.parse(xhttp.responseText)
            const root = document.getElementById('list-tab')
            root.innerHTML = ''

            for (const pokemon of dados.results) {
                root.innerHTML += `
                <a class="list-group-item list-group-item-action" id="list-home-list" data-toggle="list"
                            href="#description" role="tab" aria-controls="home" onclick="selecionarPokemon('${pokemon.url}')">${ pokemon.name }</a>
                `
            }

            root.innerHTML += `
            <a class="list-group-item list-group-item-action bg-info text-white" onclick=mostrarPokemons('${ dados.next }')>More</a>
            `

        } else {
            console.log('Erro ao obter dados')
        }
    }

    xhttp.send()

}

const url_inicial = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=10'
addEventListener('load', mostrarPokemons(url_inicial))