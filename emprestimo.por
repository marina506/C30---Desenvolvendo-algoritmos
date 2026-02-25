programa{
 funcao inicio() {
real valor, salario, prestacaoMensal, limite
inteiro anosPagamento, meses

escreva("Digite o valor da casa:")
leia(valor)

escreva("Digite seu salário:")
leia(salario)

escreva("Digite em quantos anos você vai pagar:")
leia(anosPagamento)

meses = anosPagamento * 12
prestacaoMensal = valor / meses
limite = salario * 0.30

se(prestacaoMensal<=limite){
    escreva("Empréstimo aprovado!")
}
senao{
    escreva("Empréstimo negado!")
}
 }
}