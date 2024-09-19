print("m- Matutino, v- Vespertino ou n- Noturno")
turno=input("Digite o seu turno: ").upper()

if turno=="M":
    print("Bom dia")
elif turno=="V":
        print("Boa Tarde")
elif turno=="N":
        print("Boa noite")
else:
    print("Valor Inválido")