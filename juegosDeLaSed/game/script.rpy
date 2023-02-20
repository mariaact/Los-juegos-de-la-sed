define n = Character("Napoleon")
define ca = Character("Capitan America")
define jc = Character("Jackie Chan")
define s = Character("Shakira")
define e = Character("Elon Musk")
define t = Character("Thor")


label start:

    image fondoPrimero = im.Scale("planeta.jpg", 1920, 1100)


    scene fondoPrimero

    "Tras años de guerras entre todos los continentes..."

    "El mundo no volvió a ser como antes..."
    "La población humana pasó de los 8 billones a 100 millones. La escasez de alimentos y productos generó todavía más violencia y un crecimiento de la anarquía en los grupos más débiles. Debido a esta situación de caos general, los lideres mundiales decidieron crear una especie de Juegos del hambre denominado, Los Juegos de la Sed, donde cada continente sería representado por un capitán, el cual se enfrentará contra el resto de los capitanes por conseguir..."
    "La última cerveza, un premio que simbolizaría la hegemonía del continente que la poseyese. Cada capitán recibió una carta de los lideres supremos..."

    
    scene fondoPrimero

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

