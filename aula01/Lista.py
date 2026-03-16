from No import No
class Lista:

    def __init__(self):
        self.inicio = None

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox

                while aux :
                    if nodo.dado < aux.dado:
                        nodo.prox = aux
                        ant.prox = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux == None:
                    ant.prox = nodo
        self.imprimir()




    def imprimir(self):
        print("\n----------------------")
        print("Lista Encadeada")

        if self.inicio is None:
            print("\nLista Vazia")
            return
        aux = self.inicio
        while aux :
            print(  aux.dado )
            aux = aux.prox
