# Regulação de Leitos de UTI
> Este simulador é  capaz de criar, de forma aleatória, demandas e disponibilidade de leitos. O sistema gerencia  a alocação de leitos e, se necessário, a espera por leitos. Um mapa da situação do sistema é apresentado a cada instante, onde temos  ideia da situação do processo, ou seja, identificar se o sistema está sobrecarregado ou com sub-utilização.

# Apresentando a solução do problema: 👾

## Como a solução foi modularizada? 🚀
> Segue abaixo as classes e métodos utilizados.

###  cLeitos

>  Gera um leito aleatório com código, estado, Paciente (onde fica alocado o id do paciente), tipo (faixa etária que será vinculada).

#### Métodos:

- **tipo_leito()**: Retorna a faixa etária do paciente que pode ser vinculado.

- **dar_paciente()**: Envia o id do paciente.

- **dar_estado()** : Modifica a disponibilidade do leito (caso tenha um paciente vinculado, ele deixa de estar disponível).

### cPacientes

> Gera um paciente com id, estado, idade aleatórios. Além disso, possui funções de verificação e conversão para facilitar a comunicação entre as classes.

#### Métodos:

- **precisaUTI()**: Retorna se o paciente precisa ou não de leito.

- **defineVaga()**: Retorna a Faixa Etária do Paciente.

- **idadeEmAnos()**: Converte idade em meses para anos.

- **estado_paranumero(), padronizaEstado()**: Converte o estado do paciente de cores para um número e, transforma o estado, antes identificado por cores, em frases mais intuitivas, respectivamente.

### Gerenciador

> Criado usando a classe  cFila, tem como principal objetivo  relacionar os leitos e os pacientes.

#### Métodos:

- **inserir Ordenado()**: Insere um paciente em uma cFila ordenando-o pelo nível de urgência.

- **inserir_Leito()**: Insere o Leito classificando-o pela Faixa Etária que ele recebe e o realocando para a sua respectiva cFila.

- **vincular_Paciente()**: Vincula o paciente a um leito verificando sua faixa etária e o nível de urgência, se o nível de urgência for abaixo de 3, retira-o paciente da cFila.

- **Métodos auxiliares:** Métodos iniciados com "imprimir" e "len" (imprimem a fila e seu tamanho, respectivamente).

### PacienteMelhoraPiora

#### Métodos:

 -  **acompanhaPacientesNaFila():** Usa a função *determina_evento* para simular possíveis pacientes que melhoraram ou morreram. Em ambos os casos o paciente é retirado da fila de espera.

 - **determine_evento():** Com base nas faixas etárias dos pacientes, determina a probabilidade de melhora ou piora deles. Os critérios são meramente ilustrativos.

## Qual TAD foi utilizada ? 🛸

> A Fila  foi utilizada como  principal TAD. 

## Como foi feito o controle de leitos e dos pacientes ? 🏥

> O controle dos leitos foi feito com  três filas, uma para cada faixa etária abrangida e no decorrer das solitações, o leito é removido da lista e vinculado conforme o tipo (faixa etária) do paciente. 

> O controle do paciente foi realizado por meio de uma fila chamada "Fila_de_Espera", onde os pacientes são inseridos por ordem de prioridade. O paciente com maior risco de dano é priorizado e colocado à frente. Em seguida, busca-se um leito disponível e, caso seja encontrado, ocorre a vinculação: ambos (paciente e leito) são removidos de suas respectivas filas (sendo o leito mais recentemente inserido o primeiro a receber um paciente). Se a vinculação não ocorrer, há duas possíveis situações: o paciente retorna para a fila de espera caso esteja em estado de urgência, ou é removido da fila se sua condição for de baixa urgência.

## Como o controlador principal foi construído e quais as principais situações  abrangidas na solução ? ⛓️

> O controlador principal é nomeado "Gerenciador" nesta solução. Como citado anteriormente, ele relaciona os pacientes aos leitos, com auxilio das classes cLeitos e cPacientes. Sendo assim, ele atua como o núcleo do sistema.

## Situações abrangidas:

- **Alocação de Leitos:** Alocação de leitos de acordo com a quantidade de pacientes. Aqui também é abrangida a possibilidade de melhora ou piora do paciente enquanto ele está na fila de espera.

- **Superlotação - Primeiro Caso:** O sistema recebe uma grande quantidade de pacientes e, à medida que ocorre a superlotação, gera novos leitos e aloca a demanda extra de pacientes (Escalabilidade).

- **Superlotação - Segundo caso :** Exaustão do sistema.

### Simuladores:

 > Criamos 3 simuladores para testar as situações que nossa solução abrange.

- **SimulaAlocacaoLeitos:** Nesse teste é solicitado  ao usuário uma quantidade máxima de pacientes que o sistema pode suportar, em seguida simula-se  a evolução do paciente na fila de espera, geração de leitos, vinculação dos pacientes da fila aos leitos e exibição da situação final da fila de espera.
  
- **SimulaSuperLotacao1:** O sistema gera uma grande quantidade de paciente e uma quantidade limitada de leitos, em seguida ele recebe mais leitos para suprir a demanda extra até que a fila_espera esteja vazia.
  
- **SilumaSuperLotacao2:** Aqui o sistema é testado até sua exaustão por meio de um *loop* de geração infinita de pacientes, demanda maior que a quantidade de leitos, afim de superlotar o sistema. 

## Metodologia ágil adotada: 🧙
>  Inicialmente, cada desenvolvedor ficou responsável por duas funcionalidades do código. Realizamos reuniões semanais para alinhar o projeto e os alinhamentos pequenos eram feitos de acordo com a demanda no WhatsApp. Os simuladores foram desenvolvidos em conjunto.

### Atribuição dos Devs:
> Segue abaixo as classes e métodos responsáveis por cada DEV. 

#### Nicole Siva: 
- cPacientes
- PacienteMelhoraPiora
- Estrutura da justificativa/Formatação

#### Yuri Santos:
 - cLeitos
 - Gerenciador
 - SimulaSuperloTacao2

 ### Ambos:
 - cFila
 - SimulaAlocacaoLeitos
 - SimulaSuperLotacao1
 - Conteúdo da justificativa



## Devs: 🧑🏿‍💻👩🏿‍💻

- [Nicole Silva](https://github.com/Nicolesilvaa)
- [Yuri Santos](https://github.com/Snorlaxch)
