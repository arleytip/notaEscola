nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))

total= (nota1 + nota2) / 2
if total < 7:
    print("Reprovado")
elif total < 10:
    print("Aprovado")
else:
    print("Aprovado com Distinção")