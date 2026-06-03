def gerarlista(var):
    i = 0 
    lista = []
    while i < len(var):
        lista.append(var[i])
        i += 1
    return lista

def vogcon(var):
    lista = []
    vog = ""
    con = ""
    i = 0 
    while i < len(var):
        if var[i] == "a" or var[i] == "e" or var[i] == "i" or var[i] == "o" or var[i] == "u":
            vog = vog + var[i]
        else:
            con = con + var[i]
        i += 1
    lista.append(vog)
    lista.append(con)
    return lista


"""3 leia um string e retorne uma lista de letras que se repetem continuamente ex: abbacaxi - - > [b]"""
def repete(var):
    lista = []
    i = 0
    while i < (len(var) - 1):
        if var[i] == var[i+1]:
            lista.append(var[i])
            i += 1
        else:
            i += 1
    return lista

"""4 leia uma string numerica e retorne um texto com pontuação separando o texto EX: 1234567 = 1.234.567"""
def numeros(var):
    newVar = ""
    var = inverter(var)
    i = 0
    while i < len(var):
        if i > 0 and i % 3 == 0:
            newVar += "."
        newVar += var[i]
        i += 1
    return inverter(newVar)

def inverter(texto):
    i = len(texto) - 1
    texto_invertido = ""
    while i >= 0:
        texto_invertido += texto[i]  
        i -= 1                       
    return texto_invertido

def tem():
    s
    
"""5 crie uma função "substitui(texto,original,troca)"
esta funcao le a string texto e troca todos as ocorrencias do caractere original e troca pelo caractere troca 
retorne o texto alterado"""

def substitui(texto,original,troca):
    i = 0
    while i < len(texto):

        return