number_to_guess = 7

user_number = int(input("Advivina el numero entre el uno y el diez: "))

if number_to_guess == user_number:
    print("has ganado")
else:
    print("has perdido")