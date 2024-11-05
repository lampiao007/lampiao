programa {
  funcao inicio() 
  {
        real soma, sub, mult, div
        real n1, n2
        real op

        escreva ("informe a opera��o desejada: \n")
        escreva ("DIGITE: \n")
        escreva ("1 para SOMAR \n")
        escreva ("2 para SUBTRAIR \n")
        escreva ("3 para MULTIPLICAR \n")
        escreva ("4 para DIVIDIR \n")
        leia(op)

        limpa()

        escreva("Informe o primeiro valor: ")
        leia(n1)
        escreva("informe o segundo valor: ")
        leia(n2)

        se (op == 1){
          soma = n1+n2
          escreva("A soma �: ",soma)
        }
        senao se(op == 2){
          sub = n1-n2
          escreva("A diferen�a �: ",sub)
        }
        senao se(op == 3){
          mult = n1*n2
          escreva("A maultiplica��o �: ",mult)
        }
        senao se(op == 4){
          div = n1/n2
          escreva("A divis�o �: ",div)
        }
        senao{
          escreva("Opera��o Inv�lida!!!")
        }


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  }
}
