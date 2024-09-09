## Coletar Informações do Pet

# Descrição

Este script em Python coleta e exibe informações básicas sobre um pet, como nome, idade e peso. Ele garante que os valores inseridos para a idade e o peso sejam válidos (inteiros e números flutuantes, respectivamente) e que não sejam negativos.

# Funcionalidade

Nome do Pet: Solicita ao usuário que insira o nome do pet.
Idade do Pet: Solicita ao usuário que insira a idade do pet em anos. O valor deve ser um número inteiro e positivo.
Peso do Pet: Solicita ao usuário que insira o peso do pet em quilogramas. O valor deve ser um número flutuante e positivo.

# Validações

Idade: O programa verifica se a idade é um número inteiro e maior ou igual a zero.
Peso: O programa verifica se o peso é um número flutuante e maior ou igual a zero.
Uso
Execute o script e siga as instruções na tela para inserir as informações do seu pet. O script exibirá as informações coletadas de forma formatada ao final.

# Uso

Execute o script e siga as instruções na tela para inserir as informações do seu pet. O script exibirá as informações coletadas de forma formatada ao final.

# Exemplo de Execução

Por favor, insira as informações sobre seu pet.

```
Nome do pet: Rex
Idade do pet (em anos): 5
Peso do pet (em kg): 12.3

Informações do pet:
Nome: Rex
Idade: 5 anos
Peso: 12.3 kg 

```

# Requisitos

Python 3.x

# Como Executar

Para executar o script, basta rodar o comando abaixo em um terminal:

``` 
python nome_do_arquivo.py

```
Substitua nome_do_arquivo.py pelo nome do arquivo em que você salvou o script.
Por exemplo de acordo com esse código seria python info_pet.py

## Testes Unitários

# Descrição

Este projeto inclui um conjunto de testes unitários, escritos utilizando a biblioteca unittest, que verificam o comportamento da função coletar_informacoes_pet. Estes testes garantem que a função lida corretamente com diferentes tipos de entradas do usuário e que as validações de idade e peso são aplicadas conforme esperado.

# Como Executar os Testes

# Para rodar os testes, utilize o seguinte comando no terminal:

```
pytest -s tests/

```

Isso executará todos os testes definidos na classe TestInfoPet e exibirá um relatório dos resultados no terminal.

## Contribuição

Para Contribuir com esse projeto.

[Contribution guidelines for this project](contribuição/CONTRIBUTING.md)

