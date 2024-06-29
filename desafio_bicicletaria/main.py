# class Bicicleta:
#     def __init__(self, cor, modelo, ano, valor):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.valor = valor


#     def buzinar(self):
#         print("Plim Plim")
    
    
#     def parar(self):
#         print("Parando...")
#         print("Bicleta parada")
    
    
#     def correr(self):
#         print("Vrummmmm")

    
#     def get_cor(self):
#         return self.cor


#     def __str__(self):
#         # return f"Bicicleta: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: R${self.valor}"
#         return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# b1 = Bicicleta("Preta", "caloi", 2024, 750)
# b1.buzinar()
# b1.parar()
# b1.correr()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)


# b2 = Bicicleta("Vermelha", "monark", 2024, 600)
# Bicicleta.buzinar(b2)
# b2.buzinar()
# print(b2.get_cor())
# print(b2.cor)
# print(b2)
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()