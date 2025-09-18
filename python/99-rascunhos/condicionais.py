# if, elif e else

idade = 18

if idade >= 18:
    print("Maior de idade")

if idade == 18:
    print("Você tem 18 anos")

if idade <= 17:
    print("Você é menor de idade")

if idade != 10:
    print("Você não tem 10 anos")

idade += -1
if idade >= 18:
    print("Maior de idade")
elif idade == 17:
    print("Você vai fazer 18 anos")
else:
    print("VocÊ é menor de idade")

idade  = int(input("Informe sua idade: "))
mensagem = "Pode tirar CNH" if idade >= 18 else "Não pode tirar CHN ainda"

print(mensagem)