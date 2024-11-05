programa {
  funcao inicio() {
    
    cadeia nome
    inteiro idade

    escreva("Digite o seu nome: ")
    leia(nome)
    escreva("Informe a sua idade: ")
    leia(idade)

    se(idade>=18){
      escreva(nome, " voc� � maior de idade")
    } senao{
      escreva(nome, " voc� � menor de idade")
    }



  }
}
