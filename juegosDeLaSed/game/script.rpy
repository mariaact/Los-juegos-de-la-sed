define n = Character("Napoleon")
define ca = Character("Capitan America")
define jc = Character("Jackie Chan")
define s = Character("Shakira")
define e = Character("Elon Musk")
define t = Character("Thor")
define sirv = Character("Sirviente")
define yo = Character("Yo")


label start:

    image fondoPrimero = im.Scale("planeta.jpg", 1920, 1100)


    scene fondoPrimero

    "Tras años de guerras entre todos los continentes..."

    "El mundo no volvió a ser como antes..."
    "La población humana pasó de los 8 billones a 100 millones. La escasez de alimentos y productos generó todavía más violencia y un crecimiento de la anarquía en los grupos más débiles."
    "Debido a esta situación de caos general, los lideres mundiales decidieron crear una especie de Juegos del hambre denominado, Los Juegos de la Sed... "
    "Donde cada continente sería representado por un capitán, el cual se enfrentará contra el resto de los capitanes por conseguir..."
    "La última cerveza, un premio que simbolizaría la hegemonía del continente que la poseyese. Cada capitán recibió una carta de los lideres supremos..."

    scene fondoPrimero

    show napoleon at left with dissolve:
        yalign 0.0
        linear 2.0 xpos 700 ypos 500 
    show chris at right with dissolve:
        xalign 0.0
        linear 2.0 xpos 1000 ypos 700
        

    sirv "Señor le ha llegado una carta del primer ministro... "
    n "Gracias Roustam! "
    n "*leyendo*"
    n "Usted ha sido invitado..."
    hide napoleon

    show capitan at topright
    ca "a representar a su continente en... "
    hide capitan

    show personaje2 at reset
    jc "los Juegos de la Sed..."
    hide personaje2

    show shakira at reset
    s "una competición en la que…"
    hide shakira

    show elon at reset
    e "peleareis contra otros capitanes en la Arena Gelida en la Antártida, por..."
    hide elon
    
    show chris at reset
    t "salvar a vuestro continente del caos y la destrucción."
    show napoleon at topright
    n "Suena passionnant"
    yo "¿Cómo? ¡¿Por qué yo?!"

    image fondoSegundo = im.Scale("fondo2.jpg", 1920, 1100)
    scene fondoSegundo

    "Unos meses más tarde"
    "Bienvenidos capitanes, a los Juegos de la Sed, donde cada uno de vosotros representará a su respectivo continente. "
    "Napoleón (Europa), Jackie Chan (Asia), Shakira (Sur América), Charlie (Almendra), Thor (Oceanía) y el Capitán América (América del Norte). En estos Juegos tendréis que pelearos hasta que solo quede uno."

    image fondoTercero = im.Scale("fondo3.png", 1920, 1100)
    scene fondoTercero

    yo "De acuerdo, ahora tengo que escoger si voy hacia la cueva helada o seguir los sospechosos sonidos de las tundras. "

    label startPoint:
        menu: 
            "Cueva Helada":
                "Tras atravesar la cueva helada, llegas a un final cerrado."
                "Decides volver al principio"
                jump startPoint
            "Tundra":
                call respuesta1

        show chris at truecenter
        menu:
            "enfrentarse":
                jump respuesta4
            "persuadirlo":
                jump respuesta5

    label respuesta4:
        "Thor te golpea con el martillo y mueres."
        return

    label respuesta5:
        "¡Has logrado convencer a Thor de formar un equipo!"
        "Tras atravesar la tundra te encuentras a tan solo 10 km de llegar al centro de la Arena y se te plantea una nueva decisión.  "
        "Thor te insiste en descansar y hacer un campamento. "
        menu:
            "Sí":
                "Al montar un campamento y prender un fuego, revelais vuestra posición ..."
                "De repente aparece..."
                jump respuesta6
                
            "No":
                jump descanso
        return  
        
    label respuesta1:
        scene fondoTercero
        "Te encuentras con Thor (Quién esta armado con un martillo) "
        "Se te plantea una nueva decisión"
        return
    
    label respuesta2:


    label descanso:
        "El campamento está vacío, pero encuentras un cuchillo. Decidís apagar el fuego y descansar. "
        scene fondoSegundo
        "*El día final*"
        "Llegáis Chris y tu a la zona final y ahí veis como Napoleón mata a Jackie Chan"
        "Decides que es hora de matar a Napoleón y lo conseguís gracias al cuchillo que recogiste en el campamento. Sin embargo, Chris muere también."
        # poner un fin AQUI

    label respuesta6:
        "Los capitanes Capitán América y Shakira, que al parecer se han aliado también, asaltan vuestro campamento y os toca enfrentaros. "
        scene fondoPrimero
        show shakira at left with dissolve:
            yalign 0.0
            linear 2.0 xpos 700 ypos 500 
        show personaje1 at right with dissolve:
            xalign 0.0
            linear 2.0 xpos 1000 ypos 700 
        pause 5.0
        hide shakira
        hide personaje1
        show bang at truecenter with dissolve:
            linear 15.0

        "Has ganado!"  

        scene fondoSegundo
        show napoleon at left with dissolve:
            xalign 0.0
            linear 2.0 xpos 0 xpos 500
        pause 1.0
        show capitan at right
        pause 2.0

        menu:
            "enfrentarse":
                jump perder
                
            "persuadirlo":
                jump ganar
        return
    
    label perder:
        scene fondoTercero
        "GAME OVER"
        return
    
    label ganar:
        scene fondoTercero
        "Has ganado!!"
   


    return

