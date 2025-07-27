<div align="center" id="topo">

<img src="https://media.giphy.com/media/iIqmM5tTjmpOB9mpbn/giphy.gif" width="200px" alt="Gif animado"/>

# <code><strong> Interpolação Polinomial pelo Método de Newton</strong></code>

<em>Trabalho de Análise Numérica para implementar a interpolação polinomial pelo método de Newton.</em>

[![Python Usage](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge&logo=python)]()
[![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)]()
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Visite%20meu%20perfil-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rian-carlos-valcanaia-b2b487168/)

</div>

## Índice

- [📌 Objetivos](#-objetivos)
- [📥 Entradas do sistema](#-entradas-do-sistema)
- [🧱 Estruturas de Dados](#-estruturas-de-dados)
- [🧰 Funcionalidades](#-funcionalidades)
- [📊 Exemplo de Execução](#-exemplo-de-execução)
- [📂 Como executar](#-como-executar)
- [👨‍🏫 Envolvidos](#-envolvidos)
- [📅 Curso](#-curso)
- [📄 Código-fonte](#-código-fonte)

## 📌 Objetivos
* Implementar o método de Interpolação Polinomial de Newton em Python.
* Construir e exibir a tabela de diferenças divididas a partir de um conjunto de dados.
* Gerar um gráfico de dispersão com os pontos discretos e a curva do polinômio interpolador.
* Estimar o valor de `f(1.23)` utilizando o polinômio com o menor grau que satisfaça um erro estimado.
* Justificar a escolha do grau do polinômio com base na estimativa de erro.

[⬆ Voltar ao topo](#topo)

## 📥 Entradas do sistema
* Todos os dados de entrada são pré-definidos diretamente no código-fonte:
* **Pontos conhecidos**: Uma lista de tuplas `(x, y)` para a interpolação.
* **Valor a estimar**: O ponto `x` (`1.23`) para o qual o valor de `f(x)` será estimado.
* **Erro máximo**: A tolerância de erro (`10^-3`) usada para determinar o grau ideal do polinômio.

[⬆ Voltar ao topo](#topo)

## 🧱 Estruturas de Dados
* **Pontos**: Os dados de entrada são armazenados em uma `list` de `tuples` no formato `[(x0, y0), (x1, y1), ...]`.
* **Tabela de Diferenças Divididas**: Uma matriz triangular (implementada como uma lista de listas) é usada para armazenar e calcular as diferenças divididas de Newton.
* **Polinômio Simbólico**: A biblioteca `SymPy` é usada para construir e manipular a expressão do polinômio de forma simbólica antes de convertê-la em uma função numérica.

[⬆ Voltar ao topo](#topo)

## 🧰 Funcionalidades

### 🔹 Funções Principais
* `diferencas_divididas()`: Calcula a tabela de diferenças divididas a partir dos pontos fornecidos.
* `polinomio_newton()`: Constrói a expressão simbólica do polinômio interpolador de Newton para um determinado grau.
* `estimativa_erro()`: Calcula o erro estimado para polinômios de graus crescentes e retorna o menor grau que satisfaz a tolerância de erro definida.
* `plot_dispersao()`: Gera e exibe um gráfico com os pontos originais, a curva do polinômio interpolador e o ponto estimado.

### 🔸 Funções Secundárias
* `selecionar_pontos_proximos()`: Seleciona os `grau + 1` pontos mais próximos do valor a ser interpolado para minimizar o erro.
* `printaDD()`: Formata e imprime a tabela de diferenças divididas no console.

[⬆ Voltar ao topo](#topo)

## 📊 Exemplo de Execução
1. O script é executado sem a necessidade de entradas do usuário.
2. A tabela de diferenças divididas para todos os pontos é calculada e exibida no console.
3. A função de estimativa de erro é chamada para determinar o melhor grau para o polinômio, buscando um erro menor que `10^-3`.
4. O polinômio de Newton com o grau ótimo é construído e sua expressão simbólica é impressa.
5. O valor de `f(1.23)` é calculado usando o polinômio e o resultado é exibido.
6. Por fim, um gráfico é gerado, mostrando os pontos originais, a curva do polinômio e o ponto recém-estimado destacado.

[⬆ Voltar ao topo](#topo)

## 📂 Como executar
Primeiro, instale as dependências necessárias:
```bash
pip install sympy matplotlib numpy
```
Em seguida, execute o script Python:
```bash
python3 trabalho.py
```

[⬆ Voltar ao topo](#topo)

## 👨‍🏫 Envolvidos
* **Professor**: Jarbas Ferrari
* **Estudantes**:
  - [Lucas Mamacedo](https://github.com/lucasomac0)
  * [Rian Valcanaia](https://github.com/RianValcanaia)

[⬆ Voltar ao topo](#topo)

## 📅 Curso

* **Universidade**: Universidade do Estado de Santa Catarina (UDESC)
* **Disciplina**: Análise Numérica
* **Semestre**: 4º

[⬆ Voltar ao topo](#topo)

## 📄 Código-fonte

🔗 [https://github.com/RianValcanaia/ANN_TC3_Interpolacao_Polinomial_Metodo_de_Newton](https://github.com/RianValcanaia/ANN_TC3_Interpolacao_Polinomial_Metodo_de_Newton)

[⬆ Voltar ao topo](#topo)
