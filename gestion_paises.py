# Trabajo Practico Integrador - Programacion 1
# Gestion de Datos de Paises en Python: filtros, ordenamientos y estadisticas
#
# Estructura principal:
# - Una lista de diccionarios.
# - Cada pais se guarda como:
#   {"nombre": str, "poblacion": int, "superficie": int, "continente": str}
#
# El programa lee los datos desde un archivo CSV, permite operar con ellos
# desde un menu en consola y guarda cambios cuando se agregan o actualizan paises.

import csv


def normalizar_texto(texto):
    """
    Normaliza un texto para comparar nombres o continentes.
    strip() elimina espacios al inicio y final.
    lower() convierte todo a minusculas.
    """
    return texto.strip().lower()


def validar_campo_no_vacio(valor, nombre_campo):
    """
    Valida que un campo de texto no este vacio.
    Si esta vacio, lanza ValueError con un mensaje claro.
    """
    if valor.strip() == "":
        raise ValueError(f"El campo {nombre_campo} no puede estar vacio.")


def pedir_entero(mensaje, minimo=None):
    """
    Pide un numero entero por teclado.
    Si el usuario ingresa un dato no numerico, se lanza ValueError.
    Si se indica un minimo, tambien valida que el numero sea mayor o igual a ese minimo.
    """
    try:
        numero = int(input(mensaje))
    except ValueError:
        raise ValueError("Debe ingresar un numero entero valido.")

    if minimo is not None and numero < minimo:
        raise ValueError(f"El numero debe ser mayor o igual a {minimo}.")

    return numero


def buscar_indice_pais(paises, nombre):
    """
    Busca un pais por nombre exacto, ignorando mayusculas/minusculas y espacios.
    Retorna el indice si lo encuentra.
    Retorna -1 si no lo encuentra.
    """
    nombre_buscado = normalizar_texto(nombre)

    for indice in range(len(paises)):
        if normalizar_texto(paises[indice]["nombre"]) == nombre_buscado:
            return indice

    return -1


def cargar_paises_csv(ruta_csv):
    """
    Lee los paises desde un archivo CSV.
    Controla errores de formato:
    - Columnas obligatorias.
    - Campos vacios.
    - Poblacion y superficie numericas.
    - Valores negativos.
    - Paises duplicados.

    Si una fila es invalida, se informa el error y se sigue con las demas.
    """
    paises = []

    try:
        with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            columnas_requeridas = ["nombre", "poblacion", "superficie", "continente"]

            if lector.fieldnames is None:
                raise ValueError("El archivo CSV esta vacio o no tiene encabezados.")

            for columna in columnas_requeridas:
                if columna not in lector.fieldnames:
                    raise ValueError(f"Falta la columna obligatoria: {columna}")

            numero_fila = 1

            for fila in lector:
                numero_fila += 1

                try:
                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()

                    validar_campo_no_vacio(nombre, "nombre")
                    validar_campo_no_vacio(continente, "continente")

                    if buscar_indice_pais(paises, nombre) != -1:
                        raise ValueError("Pais duplicado en el CSV.")

                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])

                    if poblacion < 0:
                        raise ValueError("La poblacion no puede ser negativa.")

                    if superficie <= 0:
                        raise ValueError("La superficie debe ser mayor que cero.")

                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    }

                    paises.append(pais)

                except ValueError as error:
                    print(f"Error en fila {numero_fila}: {error}. La fila fue omitida.")

    except FileNotFoundError:
        print("No se encontro el archivo CSV. Se iniciara con una lista vacia.")
    except ValueError as error:
        print("Error al leer el CSV:", error)

    return paises


def guardar_paises_csv(ruta_csv, paises):
    """
    Guarda la lista de paises en el archivo CSV.
    Esto permite conservar los cambios hechos al agregar o actualizar datos.
    """
    with open(ruta_csv, mode="w", encoding="utf-8", newline="") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


def mostrar_paises(paises):
    """1
    Muestra una lista de paises en pantalla.
    Se usa para mostrar resultados de busquedas, filtros y ordenamientos.
    """
    if len(paises) == 0:
        print("No hay paises para mostrar.")
        return

    print("\nListado de paises:")
    print("-" * 75)
    print(f"{'Nombre':<25} {'Poblacion':>15} {'Superficie':>15} {'Continente':<15}")
    print("-" * 75)

    for pais in paises:
        print(
            f"{pais['nombre']:<25} "
            f"{pais['poblacion']:>15} "
            f"{pais['superficie']:>15} "
            f"{pais['continente']:<15}"
        )


def agregar_pais(paises, ruta_csv):
    """
    Agrega un pais nuevo con todos sus datos.
    No permite campos vacios ni nombres duplicados.
    """
    try:
        nombre = input("Ingrese el nombre del pais: ").strip()
        validar_campo_no_vacio(nombre, "nombre")

        if buscar_indice_pais(paises, nombre) != -1:
            raise ValueError("El pais ya existe en el dataset.")

        poblacion = pedir_entero("Ingrese la poblacion: ", minimo=0)
        superficie = pedir_entero("Ingrese la superficie en km2: ", minimo=1)

        continente = input("Ingrese el continente: ").strip()
        validar_campo_no_vacio(continente, "continente")

        pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        paises.append(pais)
        guardar_paises_csv(ruta_csv, paises)

        print("Pais agregado correctamente.")

    except ValueError as error:
        print("Error:", error)
        print("No se agrego el pais.")


def actualizar_pais(paises, ruta_csv):
    """
    Actualiza poblacion y superficie de un pais existente.
    Si no encuentra el pais, informa el problema sin romper el programa.
    """
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    nombre = input("Ingrese el nombre del pais a actualizar: ").strip()
    indice = buscar_indice_pais(paises, nombre)

    if indice == -1:
        print("No se encontro un pais con ese nombre.")
        return

    try:
        nueva_poblacion = pedir_entero("Ingrese la nueva poblacion: ", minimo=0)
        nueva_superficie = pedir_entero("Ingrese la nueva superficie en km2: ", minimo=1)

        paises[indice]["poblacion"] = nueva_poblacion
        paises[indice]["superficie"] = nueva_superficie

        guardar_paises_csv(ruta_csv, paises)

        print("Datos actualizados correctamente.")

    except ValueError as error:
        print("Error:", error)
        print("No se actualizaron los datos.")


def buscar_pais(paises):
    """
    Busca paises por nombre.
    Permite coincidencia exacta o parcial.
    Por ejemplo, buscar 'arg' puede encontrar 'Argentina'.
    """
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip()

    if termino == "":
        print("La busqueda no puede estar vacia.")
        return

    resultados = []
    termino_normalizado = normalizar_texto(termino)

    for pais in paises:
        if termino_normalizado in normalizar_texto(pais["nombre"]):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises que coincidan con la busqueda.")
    else:
        mostrar_paises(resultados)


def filtrar_por_continente(paises):
    """
    Filtra paises segun el continente ingresado por el usuario.
    """
    continente = input("Ingrese el continente a filtrar: ").strip()

    if continente == "":
        print("El continente no puede estar vacio.")
        return

    resultados = []

    for pais in paises:
        if normalizar_texto(pais["continente"]) == normalizar_texto(continente):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises para ese continente.")
    else:
        mostrar_paises(resultados)


def filtrar_por_rango(paises, campo):
    """
    Filtra paises por rango de poblacion o superficie.
    El parametro campo puede ser 'poblacion' o 'superficie'.
    """
    try:
        minimo = pedir_entero(f"Ingrese el valor minimo de {campo}: ", minimo=0)
        maximo = pedir_entero(f"Ingrese el valor maximo de {campo}: ", minimo=0)

        if minimo > maximo:
            raise ValueError("El minimo no puede ser mayor que el maximo.")

        resultados = []

        for pais in paises:
            if minimo <= pais[campo] <= maximo:
                resultados.append(pais)

        if len(resultados) == 0:
            print("No se encontraron paises dentro del rango indicado.")
        else:
            mostrar_paises(resultados)

    except ValueError as error:
        print("Error:", error)


def menu_filtrar(paises):
    """
    Menu secundario para elegir el tipo de filtro:
    continente, rango de poblacion o rango de superficie.
    """
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    print("\nFiltros disponibles:")
    print("1. Filtrar por continente")
    print("2. Filtrar por rango de poblacion")
    print("3. Filtrar por rango de superficie")

    try:
        opcion = pedir_entero("Seleccione una opcion de filtro: ")

        if opcion == 1:
            filtrar_por_continente(paises)
        elif opcion == 2:
            filtrar_por_rango(paises, "poblacion")
        elif opcion == 3:
            filtrar_por_rango(paises, "superficie")
        else:
            print("Opcion de filtro invalida.")

    except ValueError as error:
        print("Error:", error)


def ordenar_paises(paises):
    """
    Ordena los paises por nombre, poblacion o superficie.
    Permite elegir orden ascendente o descendente.
    """
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    print("\nCampos para ordenar:")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")

    try:
        opcion_campo = pedir_entero("Seleccione el campo: ")

        if opcion_campo == 1:
            campo = "nombre"
        elif opcion_campo == 2:
            campo = "poblacion"
        elif opcion_campo == 3:
            campo = "superficie"
        else:
            raise ValueError("Opcion de campo invalida.")

        print("\nOrden:")
        print("1. Ascendente")
        print("2. Descendente")

        opcion_orden = pedir_entero("Seleccione el orden: ")

        if opcion_orden == 1:
            descendente = False
        elif opcion_orden == 2:
            descendente = True
        else:
            raise ValueError("Opcion de orden invalida.")

        if campo == "nombre":
            paises_ordenados = sorted(
                paises,
                key=lambda pais: normalizar_texto(pais[campo]),
                reverse=descendente
            )
        else:
            paises_ordenados = sorted(
                paises,
                key=lambda pais: pais[campo],
                reverse=descendente
            )

        mostrar_paises(paises_ordenados)

    except ValueError as error:
        print("Error:", error)


def calcular_cantidad_por_continente(paises):
    """
    Calcula cuantos paises hay por continente.
    Retorna un diccionario donde:
    - clave: continente
    - valor: cantidad de paises
    """
    cantidad_por_continente = {}

    for pais in paises:
        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    return cantidad_por_continente


def mostrar_estadisticas(paises):
    """
    Muestra indicadores basicos:
    - Pais con mayor poblacion.
    - Pais con menor poblacion.
    - Promedio de poblacion.
    - Promedio de superficie.
    - Cantidad de paises por continente.
    """
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

    suma_poblacion = 0
    suma_superficie = 0

    for pais in paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    cantidad_por_continente = calcular_cantidad_por_continente(paises)

    print("\nEstadisticas del dataset")
    print("-" * 40)
    print(f"Pais con mayor poblacion: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']})")
    print(f"Pais con menor poblacion: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']})")
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km2")

    print("\nCantidad de paises por continente:")

    for continente, cantidad in cantidad_por_continente.items():
        print(f"- {continente}: {cantidad}")


def mostrar_menu():
    """
    Muestra el menu principal del sistema.
    """
    print("\n==============================================")
    print(" GESTION DE DATOS DE PAISES")
    print("==============================================")
    print("1. Mostrar todos los paises")
    print("2. Agregar un pais")
    print("3. Actualizar poblacion y superficie")
    print("4. Buscar pais por nombre")
    print("5. Filtrar paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("8. Guardar cambios")
    print("9. Salir")


def main():
    """
    Funcion principal.
    Carga el CSV, mantiene el menu activo y llama a las funciones correspondientes.
    """
    ruta_csv = "paises.csv"
    paises = cargar_paises_csv(ruta_csv)

    opcion = 0

    while opcion != 9:
        mostrar_menu()

        try:
            opcion = pedir_entero("Seleccione una opcion: ")

            if opcion == 1:
                mostrar_paises(paises)
            elif opcion == 2:
                agregar_pais(paises, ruta_csv)
            elif opcion == 3:
                actualizar_pais(paises, ruta_csv)
            elif opcion == 4:
                buscar_pais(paises)
            elif opcion == 5:
                menu_filtrar(paises)
            elif opcion == 6:
                ordenar_paises(paises)
            elif opcion == 7:
                mostrar_estadisticas(paises)
            elif opcion == 8:
                guardar_paises_csv(ruta_csv, paises)
                print("Cambios guardados correctamente.")
            elif opcion == 9:
                guardar_paises_csv(ruta_csv, paises)
                print("Programa finalizado. Cambios guardados.")
            else:
                print("Opcion invalida. Debe ingresar un numero entre 1 y 9.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
