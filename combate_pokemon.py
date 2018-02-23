pokemon_elegido = input("¿Contra que pokemon queres luchar? (squiertle / charmander / bulbasaur):")

vida_pikachu = 100

if pokemon_elegido == "squiertle":
    vida_enemigo = 90
    nombre_pokemon = "squiertle"
    ataque_pokemon = 15
elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 20
elif pokemon_elegido == "bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "bulbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido =input("¿Que ataque queres usar? (Impactrueno / relampago):")


    if ataque_elegido == "Impactrueno":
        print("Le sacaste 10 de vida al enemigo")
        vida_enemigo -= 10
    elif ataque_elegido == "relampago":
        print("Le sacaste 20 de vida al enemigo")
        vida_enemigo -= 20

        print("La vida de {} ahora es {}".format (nombre_pokemon, vida_enemigo))

        print("{} te ha sacado {}".format(nombre_pokemon, ataque_pokemon))
        vida_pikachu -= ataque_pokemon

        print("La vida de pikachu ahora es {}".format(vida_pikachu))


if vida_pikachu <= 0:
    print("Has perdido!!")
elif vida_enemigo <= 0:
    print("Has ganado!!")