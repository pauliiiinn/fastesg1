nome_completo = str(input("Digite seu nome: "))
partes_nome = nome_completo.split()

primeiro_nome = partes_nome[0]
nome_inv = primeiro_nome[::-1]

sobrenome = partes_nome[-1]
sobrenome_inv = sobrenome[::-1]


nomes_do_meio = partes_nome[1]
meio_inv = nomes_do_meio[::-1]



print("-----------------")
print("Primeiro nome:", primeiro_nome)
print("Nome invertido:", nome_inv)
print("Posição: ", partes_nome.index(primeiro_nome) + 1)
print("-----------------")

print("Nomes do meio:", nomes_do_meio)
print("Nome do meio invertido:", meio_inv)
print("Posição: ", partes_nome.index(nomes_do_meio) + 1)
print("-----------------")

print("Sobrenome:", sobrenome)
print("Sobrenome invertido:", sobrenome_inv)
print("Posição: ", partes_nome.index(sobrenome) + 1)
print("-----------------")

