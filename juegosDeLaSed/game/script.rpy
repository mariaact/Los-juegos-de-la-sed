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

    image napoleonImg = img.Scale("shakira.png", 850, 850)
    image chrisImg = img.Scale("shakira.png", 850, 850)

    show napoleonImg at left with dissolve:
        yalign 0.0
        linear 2.0 xpos 100 ypos 30
    show chrisImg at right with dissolve:
        xalign 0.0
        linear 2.0 xpos 1000 ypos 870
        

    
    sirv "Señor le ha llegado una carta del primer ministro... "
    n "Gracias Roustam! "
    n "*leyendo*"
    n "Usted ha sido invitado..."
    hide napoleonImg

    image capitanImg = img.Scale("shakira.png", 850, 850)

    show capitanImg at topright
    ca "a representar a su continente en... "
    hide capitanImg

    show personaje2 at reset
    jc "los Juegos de la Sed..."
    hide personaje2

    image shakiraImg = img.Scale("shakira.png", 850, 850)

    show shakiraImg at reset
    s "una competición en la que…"
    hide shakiraImg

    image elonImg = img.Scale("shakira.png", 850, 850)
    show elonImg at reset
    e "peleareis contra otros capitanes en la Arena Gelida en la Antártida, por..."
    hide elonImg
    
    show chrisImg at reset
    t "salvar a vuestro continente del caos y la destrucción."
    show napoleonImg at topright
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

        show chrisImg at truecenter
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
                jump descanso
                
            "No":
                "Continuáis andando por un camino estrecho, y por vuestros pasos ruidosos revelais vuestra posición ..."
                "De repente aparece..."
                jump respuesta6
        return  
        
    label respuesta1:
        scene fondoTercero
        "Te encuentras con Thor (Quién esta armado con un martillo) "
        "Se te plantea una nueva decisión"
        return

    label descanso:
        "El campamento está vacío, pero encuentras un cuchillo. Decidís apagar el fuego y descansar. "
        scene fondoSegundo
        "*El día final*"
        show napoleon at reset
        # move napoleon?
        "Llegáis Chris y tu a la zona final y ahí veis como Napoleón mata a Jackie Chan"
        "De repente aparecen los capitanes Capitán América y Shakira, que al parecer se han aliado también, asaltan vuestro campamento y os toca enfrentaros. "
        
        show shakiraImg at left with dissolve:
            yalign 0.0
            linear 2.0 xpos 100 ypos 30
        show personaje1 at right with dissolve:
            xalign 0.0
            linear 2.0 xpos 1000 ypos 870
        pause 2.0
        hide shakiraImg
        hide personaje1
        play music "pelea.wmv.mp3"

        show bang at truecenter with dissolve:
            linear 15.0
        pause 2.0
        stop music
        "Napoleón se enfrenta a el Capitán America y le termina matando."
        "Decides que es hora de matar a Napoleón y lo conseguís gracias al cuchillo que recogiste en el campamento. Sin embargo, Thor muere también."
        "Finalmente Thor se suicida, debido a que el pensaba que los Juegos eran un truco del gobierno y que realmente la cerveza nunca existió... ahora nunca lo sabrá" 
        # poner un fin AQUI
        scene fondoTercero
        # sonidos de victoria
        "¡Te conviertes en el ganador de la última cerveza y todo tu continente lo festeja! "
        "Cuando traéis la última cerveza a tu gente, os dais cuenta de que la cerveza está en un estado lamentable..."
        "Os plateáis si estos juegos eran realmente un plan de los gobiernos para hacer desconectar a la población mundial... Fin  "
        return

    label respuesta6:
        show napoleonImg at reset
        n "Aquí termina vuestra búsqueda"
        scene fondoSegundo
        "GAME OVER"
        return  

        scene fondoSegundo
        show napoleon at left with dissolve:
            xalign 0.0
            linear 2.0 xpos 1000 ypos 870
        pause 1.0
        show capitanImg at right
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

