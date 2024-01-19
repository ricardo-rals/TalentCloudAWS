// Acesse o site OneCompiler (link em anexo) e crie uma função que recebe dois números como parâmetros e imprime quatro frases no terminal (a partir de template strings) demonstrando as quatro operações básicas aplicadas a ambos números. Exemplo:

// 4 + 5 = 9
// 4 - 5 = -1
// 4 x 5 = 20
// 4 / 5 = 0.8 

function operacoesBasicas(num1, num2) {
    console.log(`${num1} + ${num2} = ${num1 + num2}`);
    console.log(`${num1} - ${num2} = ${num1 - num2}`);
    console.log(`${num1} x ${num2} = ${num1 * num2}`);
    console.log(`${num1} / ${num2} = ${num1 / num2}`);
}

operacoesBasicas(4, 5);