from funciones.funciones import *



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 2_Agregar Trainer
def agregarTrainer(baseDatos):
    print('--------------------------Registrar camper---------------------------')
    nombre = input('Escribe tu nombre completo :')
    cedula = getInt('Escribe tu cedula :')
    print('Escribe tu fecha de nacimiento :')
    dia = getInt('Dia: ')
    mes = getInt('Mes: ')
    año = getInt('Año: ')
    fechaNacimiento = (f'{dia}/{mes}/{año}')
    skills = input('Ingresa tus habilidades aqui: \n')
    hDisponibles = print('Escoge una opcion: \n1. 6am a 2pm\n2. 2pm a 10pm')
    hDisponibles = getInt('Elige una opcion: ')
    if hDisponibles == 1:
        hDisponibles = '6am-2pm'
    elif hDisponibles == 2:
        hDisponibles = '2pm-10pm'
    salon = 0
    

    newTrainer = {
        'nombre':nombre,
        'cedula':cedula,
        'fechaNacimiento':fechaNacimiento,
        'skills':skills,
        'hDisponible':hDisponibles,
        'salon': salon
    }
    baseDatos['trainer'].append(newTrainer)
    return baseDatos
def addTrainer():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = agregarTrainer(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS,baseDatos)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#CASE 3_Coordinacion

def cambiarCandidato(baseDatos):
    opcion = getInt('Ingrese una opción: ')
    
    match opcion:
        case 1:
            pass  # Aquí puedes agregar lógica para la opción 1 si lo necesitas
        case 2:
            print(menuCandidatosCoordinador)
            opcion = getInt('Ingrese una opción: ')
            match opcion:
                case 1:
                    ingresar = input('Ingrese cédula del candidato: ')
                    encontrado = False
                    for camper in baseDatos['camper']:
                        if ingresar == str(camper['cedula']):
                            camper['estado']['En proceso'] = False
                            camper['estado']['Inscrito'] = True
                            print("El Camper ha sido inscrito para el examen.")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Cédula no encontrada.")
                case 2:
                    ingresar = input('Ingrese cédula del candidato: ')
                    encontrado = False
                    for camper in baseDatos['camper']:
                        if ingresar == str(camper['cedula']):
                            notaPractica = getInt('Ingrese la nota de la práctica: ')
                            notaTeorica = getInt('Ingrese la nota teórica: ')
                            totalNota = (notaPractica + notaTeorica) / 2
                            if totalNota >= 60:
                                camper['estado']['Inscrito'] = False
                                camper['estado']['Aprobado'] = True
                                print("El Camper ha sido aprobado con éxito.")
                            else:
                                camper['estado']['Inscrito'] = False
                                camper['estado']['Denegado'] = True
                                print("El Camper no alcanzó la puntuación de aprobación.")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Cédula no encontrada.")
    return baseDatos

def changeCandidato():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = cambiarCandidato(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)

def verInfoDeRutas():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cont = 0
    for i in datos["rutas"].values():
        cont += 1
        print(f"{cont}. {i}")
    rut = getInt("Ingrese la ruta: ")
    rut = str(rut)
    for j in datos["rutas"]:
        if rut == j:
            print("---- Estudiantes ----")
            for h in datos["camper"]:
                if rut == h["ruta"]:
                    print("")
                    print(h["cedula"])
                    print(f"{h["nombre"]} {h["apellido"]}")
                    print("")
            print("---- Profesores ----")
            for z in datos["trainer"]:
                if rut == z["ruta"]:
                    print("")
                    print(z["cedula"])
                    print(f"{z["nombre"]}: {z["skills"]}")
                    print("")
            pressEnter()
            return
        
def verGrupos():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    for i in datos["grupos"]:
        print("")
        for j in datos["trainer"]:
            if j["cedula"] == i["trainer"]:
                nombre =  j["nombre"]
        jornada = datos["jornadas"].get(i["jornada"])
        ruta = datos["rutas"].get(i["ruta"])
        salon = datos["salones"].get(i["salon"])
        
        print(f"Grupo: {i["nombre"]} - Trainer: {nombre} - Jornada: {jornada}")
        print(f"Ruta: {ruta} - Salon: {salon} - Cantidad: {i["cantidad"]}")
    pressEnter()
    return


def createGrupo(baseDatos):
    grupo = {}
    print("Ingresa el nombre: ")
    grupo["nombre"] = getDosDigitos()
    contT = 0
    salir = False
    while not salir:
        contT = 0
        for i in baseDatos["trainer"]:
            contT += 1
            print(f"{contT}. {i['nombre']} - cedula: {i['cedula']}")
        trainer = input("Ingresa la cedula del trainer: ")
        contT = 0
        for j in baseDatos["trainer"]:
            if j["cedula"] == trainer:
                grupo["trainer"] = j["cedula"]
                salir = True
        if not salir:
            print("Cedula de trainer invalida, ingresa un trainer existente")
    # --------------------------------------------------------------------
    salir = False
    while not salir: 
        contJ = 0
        for m in baseDatos["jornadas"].values():
            contJ += 1
            print(f"{contJ}. {m}")
        jor = getInt("Ingresa la jornada: ")
        jor = str(jor)  
        if jor in baseDatos["jornadas"]:
            grupo["jornada"] = jor
            salir = True 
        else:
            print("Valor no válido. Intenta nuevamente.")
        # -------------------------------------------------------------------
    salir = False
    while not salir:
        contJ = 0
        for n in baseDatos["rutas"].values():
            contJ += 1
            print(f"{contJ}. {n}")
        ru = str(getInt("Ingresa la ruta: "))
        rut = baseDatos["rutas"].get(ru)
        if rut is not None:
            grupo["ruta"] = ru
            salir = True
        else:
            print("Valor no válido")
    # ------------------------------------------------------------------
    salir = False
    while not salir:
        contJ = 0
        for o in baseDatos["salones"].values():
            contJ += 1
            print(f"{contJ}. {o}")
        sal = str(getInt("Ingresa el salon: "))
        salo = baseDatos["salones"].get(sal)
        if salo is not None:
            grupo["salon"] = sal
            salir = True
        else:
            print("Valor no válido")

    # -----------------------------------
    grupo["cantidad"] = 0
    baseDatos['grupos'].append(grupo)
    return baseDatos

def crearGrupo():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = createGrupo(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)

def editGroup(baseDatos):
    salirse = False
    while not salirse:
        verGrupos()
        grupo = input("Ingresa el nombre del geupo a editar: ").upper()
        for z in baseDatos["grupos"]:
            if z["nombre"] == grupo:
                contT = 0
                salir = False

                while not salir:
                    contT = 0
                    for i in baseDatos["trainer"]:
                        contT += 1
                        print(f"{contT}. {i['nombre']} - cedula: {i['cedula']}")
                    trainer = input("Ingresa la cedula del trainer: ")
                    contT = 0
                    for j in baseDatos["trainer"]:
                        if j["cedula"] == trainer:
                            z["trainer"] = j["cedula"]
                            salir = True
                    if not salir:
                        print("Cedula de trainer invalida, ingresa un trainer existente")
                        # -------------------------------------------------------------------
                salir = False
                while not salir:
                    contJ = 0
                    for n in baseDatos["rutas"].values():
                        contJ += 1
                        print(f"{contJ}. {n}")
                    ru = str(getInt("Ingresa la ruta: "))
                    rut = baseDatos["rutas"].get(ru)
                    if rut is not None:
                        z["ruta"] = ru
                        salir = True
                        return baseDatos
                    else:
                        print("Valor no válido")
def editarGrupo():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = editGroup(baseDatos)
    guardarArchivo(RUTA_BASE_DATOS, baseDatos)


def administrarGrupos():
    while True:
        print (menuAdministrarGrupos)
        opcion = getInt("Ingrese la opcion: ")
        match opcion:
            case 1: verGrupos()
            case 2: crearGrupo()
            case 3: editarGrupo()
            case 4: 
                pressEnter()
                return
            case _: print("Opcion no valida")
def administrarCampers ():
    while True:
        print(menuCamperCoordinador)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1:
                print(menuCampersCoordinador)
                opc1_1 = getInt('Ingrese una opción: ')
                match opc1_1:
                    case 1: verInfoDeRutas()
                    case 2: print("Grupo asignado")
                    case 3: 
                        print("Menu anterior")
                        break
                    case _:
                        print("Opcion no valida")
            case 2: changeCandidato() 
            case 3:
                pressEnter()
                return 
            case _: print("opcion invalida")

def administrarTrainers ():
    while True:
        print(menuCoordinadorTrainer)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1: print("addTrainer()")
            case 2: print("viewTrainers()")
            case 3: print("asigneRuta()")
            case 4: print("asigneSalon()")
            case 5: print("asigneEstudiantes()")
            case 6: print("asigneHorario()")
            case 7: 
                pressEnter()
                return
            case _: print("opcion invalida")


def reportes ():
    while True:
        print(menuCoordinadorTrainer)
        opc1 = getInt('Ingrese una opción: ')
        match opc1:
            case 1: print("addTrainer()")
            case 2: print("viewTrainers()")
            case 3: print("asigneRuta()")
            case 4: print("asigneSalon()")
            case 5: print("asigneEstudiantes()")
            case 6: print("asigneHorario()")
            case 7: 
                pressEnter()
                return
            case _: print("opcion invalida")
def coordinacion():
    while True:
        print(menuCoordinador)
        opcion = getInt('Ingrese una opción: ')
        match opcion:
            case 1: administrarCampers()
            case 2: administrarTrainers()
            case 3: reportes()
            case 4: administrarGrupos()
            case 5:
                print('Has cerrado tu sesión. ¡Adiós!')
                input('Presiona cualquier tecla para salir...')
                break
            case _:
                print('¡¡¡Opción inválida!!!')
