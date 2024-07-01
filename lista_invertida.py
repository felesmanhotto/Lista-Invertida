class ListaInvertida:
    def __init__(self):
        self.dados = {}         # Armazena todos os registros usando os IDs unicos como chave
        self.categoria_indice = {}
        self.marca_indice = {}
        self.preco_indice = {}          # Índices invertidos de cada campo

    
    def carrega_dados(self, dados_iniciais):
        for registro in dados_iniciais:
            self.add_registro(registro)     # Carrega uma lista de dicionarios (dados_iniciais)

        
    def add_registro(self, registro):
        id_registro = registro['id']            # Extrai o valor 'id' do registro a adicionar, então o usa como chave para adicionar
        self.dados[id_registro] = registro      # o registro inteiro em self.dados

        # Atualiza indice invertido categoria
        categoria = registro['categoria']
        if categoria not in self.categoria_indice:          # Verifica se a categoria já existe no indice invertido e a cria se não
            self.categoria_indice[categoria] = []
        self.categoria_indice[categoria].append(id_registro)          # Adiciona o id do registro na lista do indice invertido correspondente

        # Atualiza indice invertido marca
        marca = registro['marca']
        if marca not in self.marca_indice:
            self.marca_indice[marca] = []
        self.marca_indice[marca].append(id_registro)

        # Atualiza indice invertido preço
        preco = registro['preco']
        if preco not in self.preco_indice:
            self.preco_indice[preco] = []
        self.preco_indice[preco].append(id_registro)


    def remove_registro(self, id):
        if id in self.data:
            registro = self.data.pop(id)

        categoria_registro = registro['categoria']
        self.categoria_indice[categoria_registro].remove(id)        # Remove id do indice invertido
        if not self.categoria_indice[categoria_registro]:
            del self.categoria_indice[categoria_registro]           # Caso a categoria fique vazia, remove ela do indice invertido

        marca_registro = registro['marca']
        self.marca_indice[marca_registro].remove(id)        
        if not self.marca_indice[marca_registro]:
            del self.marca_indice[marca_registro]

        preco_registro = registro['preco']
        self.preco_indice[preco_registro].remove(id)        
        if not self.preco_indice[preco_registro]:
            del self.preco_indice[preco_registro] 

    
    def busca_simples(self, campo, valor):
        if campo == 'categoria':
            return self.categoria_indice.get(valor, [])     # Verifica qual é o campo, e entao retorna os IDs dentro da chave com o valor
        elif campo == 'marca':                              # correspondente. Ou seja, a lista (dentro do dicionario de indices invertidos)
            return self.marca_indice.get(valor, [])         # cuja chave é o valor passado como parametro.
        elif campo == 'preco':
            return self.preco_indice.get(valor, [])
        return []
    
    
    def busca_composta(self, campo1, valor1, campo2, valor2):
        primeira_busca = self.busca_simples(campo1, valor1)
        
        if campo2 == 'categoria':
            busca_filtrada = [id for id in primeira_busca if id in self.categoria_indice.get(valor2, [])]
        elif campo2 == 'marca':                                                                               
            busca_filtrada = [id for id in primeira_busca if id in self.marca_indice.get(valor2, [])]
        elif campo2 == 'preco':
            busca_filtrada = [id for id in primeira_busca if id in self.preco_indice.get(valor2, [])]
        else:
            busca_filtrada = []
                                    # Após uma busca simples, busca quais IDs encaixam no segundo valor passado apenas entre os que ja 
        return busca_filtrada       # encaixavam no primeiro.

    def exibe_dados(self):
        for registro in self.dados.values():
            print(registro)                         # Exibe registros em self.dados
