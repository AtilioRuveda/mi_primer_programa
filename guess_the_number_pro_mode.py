numero_a_adivinar = 5

primer_intento = int(input("adivina un numero entre el 1 y el 15: "))

if numero_a_adivinar == primer_intento:
    print("has ganado!!")
else:
    segundo_intento = int(input("intentalo otra vez: "))

if numero_a_adivinar == segundo_intento:
    print("lo conseguiste en tu segundo intento")
else:
    tercer_intento = int(input("intenta de nuevo, la tercera es la vencida: "))

if numero_a_adivinar == tercer_intento:
    print("la tercera era la vencida!")
else:
    cuarto_intento = int(input("dos intentos mas..: "))

if numero_a_adivinar == cuarto_intento:
    print("por fin lo hiciste!")
else:
    quinto_intento = int(input("el ultimo intento!: "))

if numero_a_adivinar == quinto_intento:
    print("casi la perdes, pero muy bien!")
else:
    print("mejor suerte la proxima vez!")


