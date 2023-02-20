define mujer = Character("Eileen")
define n = Character("Nelson")


label start:

    image fondoPrimero = im.Scale("fondo1.jpg", 1920, 1280)

    scene fondoPrimero

    "De pronto encontre...."
    "..."
    "dbkjfbbfurbfurfur"

    show personaje1 at reset 

    n "Hola soy el personajeuno"
    n "Adios"

    menu:
        "4":
            jump respuesta4
        "5":
            call respuesta5

    label respuesta4:
        "esta es una instruccion .. 4"
        return

    label respuesta5:
        "Esta es a instruccion .. 5"


    return

