class ListaInvertida:
    def __init__(self):
        self.dados = {}         # Armazena todos os registros usando os IDs unicos como chave
        self.categoria_indice = {}
        self.marca_indice = {}
        self.preco_indice = {}          # Índices invertidos de cada campo

    
    def carrega_dados(self, dados_iniciais):
        for registro in dados_iniciais:
            self.add_registro(registro)     # Carrega uma lista de dicionarios (dados_iniciais, cada registro é um dicionario)

        
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
        if id in self.dados:
            registro = self.dados.pop(id)

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

            return registro
        else:
            return None
    
    
    def busca_simples(self, campo, valor):
        if campo.lower() == 'categoria':
            return self.categoria_indice.get(valor, [])     # Verifica qual é o campo, e entao retorna os IDs dentro da chave com o valor
        elif campo.lower() == 'marca':                              # correspondente. Ou seja, a lista (dentro do dicionario de indices invertidos)
            return self.marca_indice.get(valor, [])         # cuja chave é o valor passado como parametro.
        elif campo.lower() == 'preco':
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
        for registro in self.dados.values():                            # Exibe registros em self.dados
            print(f"\nID: {registro['id']}")
            print(f"Nome do produto: {registro['nome']}")
            print(f"Categoria: {registro['categoria']}")
            print(f"Marca: {registro['marca']}")
            print(f"Preço: R${registro['preco']}")

    def get_id(self):
        for registro in self.dados.values():
            print(f"ID {registro['id']}")

    def get_categoria(self):
        sem_repeticao = []
        vistos = set()
        for registro in self.dados.values():
            if registro['categoria'] not in vistos:
                sem_repeticao.append(registro['categoria'])
                vistos.add(registro['categoria'])
        print(f"{sem_repeticao}")

    def get_marca(self):
        sem_repeticao = []
        vistos = set()
        for registro in self.dados.values():
            if registro['marca'] not in vistos:
                sem_repeticao.append(registro['marca'])
                vistos.add(registro['marca'])
        print(f"{sem_repeticao}")

    def get_preco(self):
        sem_repeticao = []
        vistos = set()
        for registro in self.dados.values():
            if registro['preco'] not in vistos:
                sem_repeticao.append(registro['preco'])
                vistos.add(registro['preco'])
        print(f"{sem_repeticao}")

    def verifica_entrada(self, min, num, max):
        while not (min <= num <= max):
            print("Valor inválido!")
            num = int(input(f"Tente novamente um valor entre {min} e {max}: "))

        return num


def main():

    lista = ListaInvertida()

    dados_iniciais = [
        {'id': 1, 'nome': 'smartphone', 'categoria': 'eletronicos', 'marca': 'samsung', 'preco': 999},
        {'id': 2, 'nome': 'notebook', 'categoria': 'eletronicos', 'marca': 'dell', 'preco': 1500},
        {'id': 3, 'nome': 'geladeira', 'categoria': 'eletrodomesticos', 'marca': 'electrolux', 'preco': 2000},
        {'id': 4, 'nome': 'televisão', 'categoria': 'eletronicos', 'marca': 'samsung', 'preco': 1200},
    ]

    lista.carrega_dados(dados_iniciais)          #carrega os dados iniciais

    while True:
        print()
        print("=" * 24)
        print("          MENU          ")
        print("=" * 24)
        print("1 - ADICIONAR ELEMENTO")
        print("2 - REMOVER ELEMENTO")
        print("3 - BUSCA SIMPLES")
        print("4 - BUSCA COMPOSTA")
        print("5 - EXIBIR DADOS")
        print("6 - SAIR")

        entrada = int(input("\nEscolha uma opção: "))
        entrada = lista.verifica_entrada(1, entrada, 6)


        if entrada == 1:
            print("\nDigite os dados do elemento a adicionar.")

            while True:
                id = int(input("\nID (número inteiro): "))
                if id in lista.dados:
                    print("Erro: ID já existe. Tente novamente.")
                else:
                    break
            
            nome = input("\nNome: ")
            categoria = input("\nCategoria: ")
            marca = input("\nMarca: ")
            preco = int(input("\nPreço (número inteiro): "))

            lista.add_registro({'id': id, 'nome': nome, 'categoria': categoria, 'marca': marca, 'preco': preco})
            print("\nElemento adicionado com sucesso!")


        elif entrada == 2:
            print("Possiveis IDs:")
            print()
            lista.get_id()
            id = int(input("\nDigite o ID do elemento a remover: "))

            removido = lista.remove_registro(id)
            if not removido:
                print("\nElemento não encontrado.")
            else:
                print("\nElemento removido com sucesso!")

 
        elif entrada == 3:
            campo = input("\ninforme por qual informação deseja fazer a busca(categoria, marca ou preco): ")
            if campo == 'categoria':
                print("\nPosséveis caregorias:")
                lista.get_categoria()
            if campo == 'marca':
                print("\nPossíveis marcas:")
                lista.get_marca()
            if campo == 'preco':
                print("\nPossíveis preços:")
                lista.get_preco()
            valor = input("\nValor para busca: ")
            if campo == 'preco':
                valor = int(valor)

            resultados = lista.busca_simples(campo, valor)

            if not resultados:
                print("\nNenhum elemento corresponde à busca.")
                continue

            print("\nElementos encontrados: ")
            for id in resultados:
                print(lista.dados[id])


        elif entrada == 4:
            campo1 = input("Primeiro campo para busca (categoria, marca ou preco): ")
            if campo1 == 'categoria':
                print("\nPosséveis caregorias:")
                lista.get_categoria()
            if campo1 == 'marca':
                print("\nPossíveis marcas:")
                lista.get_marca()
            if campo1 == 'preco':
                print("\nPossíveis preços:")
                lista.get_preco()

            valor1 = input("\nPrimeiro valor para busca: ")

            if campo1 == 'preco':
                valor1 = int(valor1)

            campo2 = input("Segundo campo para busca (categoria, marca ou preco): ")
            if campo2 == 'categoria':
                print("\nPosséveis caregorias:")
                lista.get_categoria()
            if campo2 == 'marca':
                print("\nPossíveis marcas:")
                lista.get_marca()
            if campo2 == 'preco':
                print("\nPossíveis preços:")
                lista.get_preco()

            valor2 = input("\nSegundo valor para busca: ")
            if campo2 == 'preco':
                valor2 = int(valor2)

            resultados = lista.busca_composta(campo1, valor1, campo2, valor2)
            
            if not resultados:
                print("\nNenhum elemnto corresponde à busca.")
                continue
            
            print("\nElementos encontrados: ")
            for id in resultados:
                print(lista.dados[id])


        elif entrada == 5:
            if lista.dados:
                print()
                lista.exibe_dados()
            else:
                print("A lista está vazia.")

        elif entrada == 6:
            print("\nPrograma Finalizado!")
            exit(0)


if __name__ == "__main__":
    main()