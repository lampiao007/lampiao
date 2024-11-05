programa
{
    funcao inicio()
    {
        real peso, altura, imc
        
        // Solicita o peso do aluno
        escreva("Digite o peso do aluno (em kg): ")
        leia(peso)
        
        // Solicita a altura do aluno
        escreva("Digite a altura do aluno (em metros): ")
        leia(altura)
        
        // Calcula o IMC
        imc = peso / (altura * altura)
        
        // Exibe o resultado
        escreva("O IMC do aluno �: ", imc)
    }
}
