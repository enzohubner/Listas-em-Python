lista = []
conf = "sim"
while conf == "sim":
    resp = input("Adicione algo: ")
    lista.append(resp)
    conf = input("Deseja continuar adicionando?")

print(lista)