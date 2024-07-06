Implementação de lista invertida

Cleverson Borges dos Passos
Felipe Esmanhotto da Silva

Contexto:
Uma loja online quer gerenciar informações de seus produtos de forma eficiente. Eles precisam realizar buscas frequentes com base em diversos critérios, como categoria do produto, marca e preço dos produtos. Além disso, é necessário combinar esses critérios para obter resultados mais específicos.

Solução:
Implementar um sistema de indexação complementar usando lista invertida para permitir buscas eficientes.

Motivação:
A lista invertida é uma estrutura de dados eficiente para buscas rápidas em grandes volumes de dados. Ela permite a indexação de múltiplos campos, o que facilita buscas simples e compostas.

Implementação:
Usaremos a seguinte estrutura:
Classe ListaInvertida
Achamos que ficaria mais fácil concentrar todos os dicionários contendo os dados e índices invertidos em uma só classe, usando seus atributos. Dessa forma as funções da lista são métodos de uma mesma classe e tem acesso a todos os dados.
Atributos
self.dados:
Descrição: Armazena os registros de dados com identificadores únicos (IDs) como chaves.
self.categoria_indice:
Descrição: Índice invertido para o campo 'categoria'. Armazena listas de todos os IDs que correspondem à cada categoria, usando esta como chave.
self.marca_indice:
Descrição: Índice invertido para o campo 'marca'. Armazena listas de todos os IDs que correspondem à cada marca, usando esta como chave.
self.preco_indice:
Descrição: Índice invertido para o campo ‘preco’. Armazena listas de todos os IDs que correspondem a cada preço, usando este como chave.
Decidimos armazenar os dados e os índices invertidos em dicionários para acessá-los facilmente através de chaves.
Função main
Essa função cria toda a interface com menus. O loop principal permite ao usuário selecionar operações como carga de dados, inclusão, remoção, busca simples, busca composta e exibição de todos os dados.
Decidimos por essa interface como meio de interação com o usuário pois é simples e atende às necessidades (dar acesso aos métodos da classe ListaInvertida ao usuário.
Como esse não é o foco desta tarefa não nos estendemos muito no tratamento das entradas do usuário, ao invés disso especificamos o tipo de entrada que deve ser passada. O programa, portanto, pode ser facilmente quebrado por um usuário ignorante ou mal intencionado.
Modularização:
Para facilitar a manutenção e a legibilidade do código, separamos as responsabilidades de manipulação de dados e busca e de interface com o usuário.
Manipulação de Dados: Carregamento, adição, remoção e exibição de registros são responsabilidades da classe ListaInvertida.
Busca: Métodos de busca simples e composta são centralizados na classe ListaInvertida.
Interface com o Usuário: O loop principal e as opções de menu são gerenciados na função main, que interage com a instância da classe ListaInvertida.
Conclusão
A solução apresentada combina a eficiência das listas invertidas com a simplicidade de uma interface de menu de texto, resultando em um sistema que é ao mesmo tempo poderoso e fácil de usar. A modularização clara e a centralização das operações de dados em uma única classe garantem que o sistema seja escalável e fácil de manter.




