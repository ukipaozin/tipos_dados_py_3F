

#https://dontpad.com/abner/pitondo/redondo
coloca dnv#revisão de variaveis e tipos de dados
#tipos básicos

#int: números inteiros (sem casas decimais)
idade = 17
print("Idade: ")
print(idade)
print("tipo de dado: ")
print(type(idade))

#float: ponto flutuante (com casas decimais)
altura = 1.90
print("Altura: ")
print(altura)
print("Tipo de dado")
print(type(altura))


#string: (ou str) texto puro
nome = "Turtle Man Tartauguescp"
print("nome :")
print(nome)
print("tipo de dado: ")
print(type(nome))

#bool: booleano (sim, nao, verdade, mentira, true, false)
estudante = True
print("estudante :")
print(estudante)
print("tipo de dado: ")
print(type(estudante))

#tipos de coleção
#lista coleção ordenada
frutas = ["maça", "banana", "uva", "pera"]
print("Frutas :")
print(frutas)
print("tipo de dado: ")
print(type(frutas))

#tupla, geralmente usada para guardar coordenadas
cianorte = (-23.6631, -52.6054)
print("cianorte :")
print(cianorte)
print("tipo de dado: ")
print(type(cianorte))
latitude = cianorte[0]
longitude = cianorte[1]
link_mapa = f"https://www.google.com/maps?q={latitude},{longitude}"
print("mapa: ")
print(link_mapa)

#set (conjunto de dados nao repetitivos)
numeros = {1,2,3,4,5}
print("numeros :")
print(numeros)
print("tipo de dado: ")
print(type(numeros))

#dic (dicionario)
pessoa = {"nome": "TurtleMan", "idade": 17}
print("nome :")
print(pessoa)
print("tipo de dado: ")
print(type(pessoa))

#none type, quando preciso que algo
#"seja realmente nulo"
valor = None
print("valor :")
print(valor)
print("tipo de dado: ")
print(type(valor))
