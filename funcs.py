# region HOMEMADE 
def inverter(texto):
    i = len(texto) - 1
    texto_invertido = ""
    while i >= 0:
        texto_invertido += texto[i]  
        i -= 1                       
    return texto_invertido


def tem(var,lista):
    i = 0
    while i < len(lista):
        if var == lista[i]:
            return True
        else:
            i += 1
               
#endregion 
# region exercicios
def gerarlista(var):
    i = 0 
    lista = []
    while i < len(var):
        lista.append(var[i])
        i += 1
    return lista
def vogcon(var):
    listo = ["a","e","i","o","u"]
    ba = []
    vog = ""
    con = ""
    i = 0 
    nada = 0
    while i < len(var):
        if tem(var[i],listo) == True:
            vog = vog + var[i]
        
        elif var[i] == " ":
            nada += 1
        else:
            con = con + var[i]
        i += 1
    ba.append(vog)
    ba.append(con)
    return ba


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

"""5 crie uma função "substitui(texto,original,troca)"
esta funcao le a string texto e troca todos as ocorrencias do caractere original e troca pelo caractere troca 
retorne o texto alterado"""

def substitui(texto,original,troca):
    i = 0
    novoTexto = ""
    while i < len(texto):
        if tem(texto[i],original) == True:
            novoTexto += troca
            
        else:
            novoTexto += texto[i]
        i += 1
    return novoTexto
def substitui2(texto, original, troca):
    i = 0
    novoTexto = ""
    tamanho = len(original)
    while i < len(texto):
        if texto[i : i + tamanho] == original:  
            novoTexto += troca  
            i += tamanho  
        else:
            novoTexto += texto[i]
            i += 1
    return novoTexto




# endregion


