# Declaração
nome_completo = "Salumão Barbosa"

nome_completo_aspas = """Salumão 
Barbosa"""

nome_completo_quebra = "Salumao \
    Barbosa"

nome = "Salumão"
sobrenome = "Barbosa"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + nome, sobrenome)
print("Nome completo (4a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (5a forma): {nome} {sobrenome}")
print("Nome completo (6a forma): {} {}".format(nome, sobrenome))

print(nome_completo.count("a")) # 3 ocorrências da letra a
print(f"Retorna tamanho da string: {len(nome_completo)}")
print(nome_completo.find("a")) # Primeira posição é 0. Primeira ocorrência de a é na posição 1.