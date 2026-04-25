### **Disciplina**: Teste e Qualidade de Software
### **Docente**: Prof. Francisco Rocha
### **Discente**: Willamy Josué Santos Serejo

---

# Testes:

#### Teste 1: Calcula a média e a mediana de notas da turma
**Entrada:** [7.5, 8.0, 6.0, 9.0, 5.5]
**Saídas:** 7.2 (média) e  7.5 (mediana)

#### Teste 2: Indica qual a maior e a menor nota da turma
**Entrada:** [8.9, 9.0, 4.2, 6.5,7.8]
**Saídas:** 9.0 (maior nota) e 4. (menor nota)

#### Teste 3: Retorna quantos alunos foram aprovados e reprovados
**Entrada:**  [8.9, 9.0, 4.2, 5.5,7.2]
**Saídas:** 3 (aprovados) e 2 (reprovados)

#### Teste 4: Retorna os níveis de classificação da turma de acordo com a sua média
**Entradas:**  [8.0, 9.3, 7.8] , [5.5, 4.7, 8.2] e [3.5, 4.7, 2.3]
**Saídas:** A, B e C respectivamente

#### Teste 5: Retorna um erro de elemento não numérico
**Entrada:** [7.5, '8.0', 6.0]
**Saída:** "Elemento '8.0' não é numérico"

#### Teste 6: Retorna um erro de lista vazia
**Entrada:** []
**Saída:** "A lista de notas não pode estar vazia"

#### Teste 7: Retorna um erro de valor fora do intervalo (Valor negativo)
**Entrada:** [5.2, -7.3, 9.0]
**Saída:** Nota -7.3 fora do intervalo permitido (0 a 10)

### Teste 8: Retorna um erro de valor fora do intervalo (valor acima de 10)
**Entrada:** [7.5, 10.6, 6.0]
**Saída:** Nota 10.6 fora do intervalo permitido (0 a 10)