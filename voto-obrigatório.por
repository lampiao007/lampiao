programa
{
    funcao inicio()
    {
        // Entrada dos dados
        cadeia nome
        inteiro idade
        
        escreva("Digite seu nome: ")
        leia(nome)
        
        escreva("Digite sua idade: ")
        leia(idade)
        
        // Verifica��o da idade
        se (idade < 16)
        {
            escreva("Voto n�o permitido")
        }
        senao se (idade >= 16 e idade <= 17)
        {
            escreva("Voto opcional")
        }
        senao se (idade >= 18 e idade <= 64)
        {
            escreva("Voto obrigat�rio")
        }
        senao // idade >= 65
        {
            escreva("Voto opcional")
        }
    }
}
