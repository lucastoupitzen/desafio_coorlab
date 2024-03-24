# Resultado - Desafio CoorLab

## Introdução

Nesse projeto foi desenvolvida uma plataforma full-stack que simula a busca de um usuário
interessado em transportes para sua viagem, com o sistema sendo responsável por mostrar as
informações da passagem mais barata e também da mais rápida para o destino escolhido pelo 
usuário de forma limpa e amigável para uma melhor experiência na plataforma.

## Backend

### Arquitetura

Para a criação do backend da aplicação proposta pelo desafio, foi utilizado o conceito
de arquitetura limpa para organização das funcionalidades, prezando pela manutenção, independência
entre os componentes e modularização do código. Conceitos de orientação a objetos foram
utilizados, buscando ao máximo seguir os princípios SOLID e usando injeção de dependência 
para garantir que a implementação de uma funcionalidade não afetasse as outras.

Para garantir a independência da aplicação de qualquer framework, o código foi estruturado
de maneira a delimitar a influência do framework aos adaptadores de requisição http. Para além disso,
todas as implementações, casos de uso e repositórios de acesso ao banco de dados independem 
de qualquer que seja a escolha do desenvolvedor para seu servidor web.


### Bibliotecas utilizadas

#### Flask

Visando uma construção de um servidor web simples que fosse leve e de fácil implementação,
foi escolhido o framework Flask para a construção do servidor do projeto e para estabelecer as rotas
de acesso da API, utilizando métodos internos como o blueprint para otimizar esse processo.

#### flask-cors

A biblioteca flask-cors foi adicionada ao projeto para permitir o melhor funcionamento
do compartilhamento de recurso entre origens (CORS), tornando a API acessível para as
requisições do frontend.

### Casos de uso e estrutura do projeto

Foram construídos dois casos de uso dentro do domínio do projeto

1- Busca pela passagem mais barata
2- Busca pela passagem mais confortável (mais rápida)

Cada um desses casos de uso possuem suas implementações independentes e acessíveis dentro
da pasta ```composers```. 

A pasta ```domain``` contém o domínio do projeto, com a estrutura de dados de uma passagem
e os casos de uso. Utilizar essa estrutura de dados possibilita que, seja qual for a solução
de banco de dados que seja escolhida, as implementações dos casos de uso utilizem a mesma
estrutura para definir o que é uma passagem e seus parâmetros, sem prejuízos em caso de troca
do banco de dados utilizado.

A pasta ```infra``` é responsácel pelo acesso ao banco de dados (no caso o arquivo data.json) 
e pelos métodos CRUD que podem ser construídos. Para o escopo dessa aplicação, apenas um método
de READ foi necessário, buscando todas as passagens disponíveis para um determinado destino.

A pasta ```data```contém a execução dos casos de uso, utilizando o repositório de métodos de acesso
ao banco de dados para fazer a filtragem dos dados requisitados.

Por fim, a pasta ```presentation```contém os controllers, responsáveis por fazer a ponte entre a requisi-
ção http e os casos de uso.

Dentro da pasta server, a pasta ```adapters``` possui os adaptadores responsáveis pela integração 
do framework utilizado com as requisições http esperadas pelo sistema.

## Frontend

### Arquitetura

Como requisitado no projeto, foi utilizado o Vue3 para a execução do frontend da aplicação, 
com a organização single file component para compor os elementos da tela. A organização dos 
componentes foi feita de modo que os componentes que são atômicos, ou seja, não são compostos
por outros componentes, fiquem na pasta ```atomic_components```. Já os componentes compostos
ficam dentro da pasta ```components```.

### Bibliotecas

#### Bootstrap

Para otimizar a estilização do código, foi utilizado o bootstrap via CDN.

#### Axios

A biblioteca axios foi utilizada para realizar as requisições http pela parte
do frontend. Os pontos de acesso da API requisitados pelo frontend são:

1) http://localhost:3000/transport/cheaper?city=${destino}
2) http://localhost:3000/transport/confort?city=${destino}

### Gerenciamento de estado

O gerenciamento de estado da aplicação foi realizado utilizando o vuex, o que permitiu 
reservar variáveis de controle para os alertas e demonstração dos resultados da requisição.
A configuração foi realizada no arquivo ```index.js```dentro da pasta ```store```, no frontend.



