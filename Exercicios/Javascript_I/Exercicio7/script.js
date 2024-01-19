const produto = document.createElement('div');
produto.id = 'produto';

const nomeProduto = document.createElement('h2');
nomeProduto.textContent = 'Cachorro Quente  ';

const descricaoProduto = document.createElement('p');
descricaoProduto.textContent = 'Cachorro Quente feito com salsicha artesanal';

const precoProduto = document.createElement('p');
precoProduto.textContent = 'Preço: R$ 99,99';

const imagemProduto = document.createElement('img');
imagemProduto.src = './cachorro-quente.jpg';
imagemProduto.alt = 'Imagem do Produto';

produto.appendChild(nomeProduto);
produto.appendChild(descricaoProduto);
produto.appendChild(precoProduto);
produto.appendChild(imagemProduto);

document.body.appendChild(produto);
