document.addEventListener('DOMContentLoaded', function() {
    var titulo = document.getElementById('titulo');
    var listaNaoOrdenada = document.getElementById('lista-nao-ordenada');
    var linkProzeducacao = document.getElementById('link-prozeducacao');
    var listaOrdenada = document.getElementById('lista-ordenada');

    titulo.innerText = 'Projeto Prozeducacao';
    linkProzeducacao.innerText = 'Acesse o site Prozeducacao';

    var item1 = document.createElement('li');
    var item2 = document.createElement('li');
    var item3 = document.createElement('li');

    item1.innerText = 'Item 1';
    item2.innerText = 'Item 2';
    item3.innerText = 'Item 3';

    listaNaoOrdenada.appendChild(item1);
    listaNaoOrdenada.appendChild(item2);
    listaNaoOrdenada.appendChild(item3);

    var itemOrdenado1 = document.createElement('li');
    var itemOrdenado2 = document.createElement('li');
    var itemOrdenado3 = document.createElement('li');

    itemOrdenado1.innerHTML = '<a href="https://prozeducacao.com.br">Item 1</a>';
    itemOrdenado2.innerHTML = '<a href="https://prozeducacao.com.br">Item 2</a>';
    itemOrdenado3.innerHTML = '<a href="https://prozeducacao.com.br">Item 3</a>';

    listaOrdenada.appendChild(itemOrdenado1);
    listaOrdenada.appendChild(itemOrdenado2);
    listaOrdenada.appendChild(itemOrdenado3);
});