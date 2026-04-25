# 💻 Disciplina: Programação Back-end
## CST em Tecnologia em Sistemas de Computação — UESPI Parnaíba

**Instituição:** Universidade Estadual do Piauí (UESPI)  
**Professor:** Eyder Rios  
**Desenvolvedor:** Willamy Josué  
**Tecnologias:** TypeScript, Node.js, Vitest  

---

## Descrição do Projeto

Este repositório é dedicado ao estudo e à implementação de **Testes Unitários** no ambiente de desenvolvimento Back-end. O foco principal é garantir a qualidade, a confiabilidade e a manutenção do código por meio da criação de especificações rigorosas para as regras de negócio.

### Conceitos Aplicados

- **Especificações (`.spec.ts`)**: definição do comportamento esperado do código.
- **Padrão AAA (Arrange, Act, Assert)**: organização lógica e estruturada de cada teste.
- **Suítes de Teste**: agrupamento de testes relacionados utilizando `describe`.
- **Feedback Loop Rápido**: uso do modo *watch* do Vitest para desenvolvimento contínuo e ágil.

---

## Guia de Instalação e Execução

Para reproduzir este ambiente e executar os testes em sua máquina local, siga as etapas abaixo.

### 1️⃣ Pré-requisitos

- Ter o Node.js instalado (versão 18 ou superior).
- Possuir o gerenciador de pacotes `npm` (instalado juntamente com o Node.js).

### 2️⃣ Clonagem do Repositório

```bash
# Clone o repositório
git clone [https://github.com/JosueSerejo/tsc-2026.1.git]
```

### 3️⃣ Acesso ao Diretório do Projeto

```bash
cd "PROGRAMAÇÃO BACK-END/testes_unitarios"
```

### 4️⃣ Instalação das Dependências

```bash
npm install
```

### 5️⃣ Execução dos Testes

```bash
npm test
```

---

## 🔍 Estrutura de Testes

- Organização em arquivos com extensão `.spec.ts`;
- Separação clara das etapas de preparação, execução e validação;
- Cobertura de cenários positivos e negativos;
- Verificação de regras de negócio;
- Testes de tratamento de exceções e casos extremos.

---

## 📚 Objetivos de Aprendizagem

- Compreender os fundamentos dos testes unitários;
- Aplicar o framework **Vitest** em projetos desenvolvidos com TypeScript;
- Garantir maior confiabilidade e qualidade ao código;
- Desenvolver software com foco em manutenção, escalabilidade e robustez.

---

## 🛠️ Tecnologias Utilizadas

- **TypeScript**
- **Node.js**
- **Vitest**

---

## 📂 Estrutura do Projeto

```text
testes_unitarios/
├── src/
│   ├── funcoes.ts
├── tests/
│   ├── funcoes.spec.ts
├── package.json
├── tsconfig.json
└── README.md
```

---

## ▶️ Fluxo de Desenvolvimento com Testes

1. Escrever a especificação do comportamento esperado.
2. Executar os testes para observar a falha inicial.
3. Implementar a funcionalidade.
4. Executar novamente os testes.
5. Refatorar o código mantendo todos os testes aprovados.

---

## ✨ Benefícios dos Testes Unitários

- Redução de erros em produção;
- Maior segurança durante refatorações;
- Documentação viva do comportamento do sistema;
- Facilita a manutenção e evolução do código;
- Aumenta a confiança no desenvolvimento.
