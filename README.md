# Trabajo Practico Integrador - Programacion 1

## Gestion de Datos de Paises en Python

Este proyecto desarrolla una aplicacion de consola en Python para gestionar informacion de paises usando listas, diccionarios, funciones, condicionales, bucles, lectura de archivos CSV, filtros, ordenamientos y estadisticas basicas.

## Integrantes

- Tomas Lopez Turconi
- Marcos Borquez

## Archivos del proyecto

- `gestion_paises.py`: codigo fuente principal del sistema.
- `paises.csv`: dataset base con datos de paises.
- `Informe_TPI_Gestion_Paises.pdf`: documentacion academica y tecnica del proyecto.
- `README.md`: descripcion general del proyecto e instrucciones de uso.

## Estructura de datos utilizada

El sistema trabaja con una lista de diccionarios. Cada pais se almacena con la siguiente estructura:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

## Funcionalidades

El menu del sistema permite:

1. Mostrar todos los paises cargados.
2. Agregar un pais nuevo.
3. Actualizar poblacion y superficie de un pais.
4. Buscar un pais por nombre, con coincidencia parcial o exacta.
5. Filtrar paises por continente, rango de poblacion o rango de superficie.
6. Ordenar paises por nombre, poblacion o superficie, en forma ascendente o descendente.
7. Mostrar estadisticas basicas.
8. Guardar cambios en el archivo CSV.
9. Salir del programa.

## Instrucciones de uso

1. Descargar o clonar el repositorio.
2. Verificar que `gestion_paises.py` y `paises.csv` esten en la misma carpeta.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python gestion_paises.py
```

o, segun la instalacion:

```bash
python3 gestion_paises.py
```

## Ejemplos de uso

### Buscar pais

Entrada:

```text
Seleccione una opcion: 4
Ingrese el nombre o parte del nombre a buscar: arg
```

Salida esperada:

```text
Argentina  45376763  2780400  America
```

### Filtrar por continente

Entrada:

```text
Seleccione una opcion: 5
Seleccione una opcion de filtro: 1
Ingrese el continente a filtrar: Asia
```

Salida esperada:

```text
Japon
China
India
```

### Estadisticas

Entrada:

```text
Seleccione una opcion: 7
```

Salida esperada:

```text
Pais con mayor poblacion: China
Pais con menor poblacion: Nueva Zelanda
Promedio de poblacion
Promedio de superficie
Cantidad de paises por continente
```

## Validaciones incluidas

- Control de campos vacios.
- Control de datos numericos invalidos.
- Control de formato del archivo CSV.
- Evita paises duplicados.
- Evita poblacion negativa.
- Evita superficie menor o igual a cero.
- Informa busquedas sin resultados.
- Maneja opciones invalidas del menu.

## Link del video demostrativo

Completar con el enlace publico de Drive o YouTube:

`PENDIENTE - pegar aqui el link del video`

## Link del repositorio

Completar con el enlace al repositorio de GitHub:

[GitHub](https://github.com/TomasLopezTur/UTN-TUPaD-TP_integrador-Programacion_I-TomasLopezTurconi_MarcosBorquez)

## Documentacion PDF

El informe academico se incluye en la raiz del proyecto con el nombre:

[Informe del TP Integrador](https://github.com/TomasLopezTur/UTN-TUPaD-TP_integrador-Programacion_I-TomasLopezTurconi_MarcosBorquez/blob/master/Informe_TPI_Gestion_Paises.pdf)
