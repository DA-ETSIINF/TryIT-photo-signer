TryIT-photo-signer
==================

Projecto creado (muy rápido) para firmar las fotos (con el logo y el hastag del evento) hechas durante el evento llamado [TryIT](www.congresotryit.com) en la [Escuela Técnica de Ingenieros Informáticos](www.etsiinf.upm.es).


## Requisitos
* Docker
* Docker compose

## Instalación
### Host
### Docker

## Configuración
Crear las siguientes carpertas dentro de esta misma carpeta:

### Fotos
* `/photos_imputs`: Aquí se dejaran las fotos que queremos firmar. Sólo son válidas las siguientes extensiones: `.png`, `.jpg`.
```bash
$ mkdir photos_imputs
```

* `/photos_signed`: Aquí se dejaran las fotos firmadas
```bash
$ mkdir photos_signed
```

### Diseño de la firma
* `/fonts`: Aquí se dejaran las tipologias de letras que se quieran usar para firmar las fotos.
* `/logos`: Aquí se dejaran los logos que se quieran usar para firmar las fotos.
#### TryIT2018
Hay una función, llamada `tryit_2018(...)`, en el fichero `tryit_photo_signer.py` que tiene la configuración para la firma del año 2018.


## Ejecución
### Host
TBD

### Docker
```bash
$ docker-compose up
```

### TODO:
- [ ] Fichero de configuración YAML
    - [ ] Carpeta donde cargar las fotos originales
    - [ ] Carpeta dede dejar las fotos firmadas
    - [ ] Evento
        - [ ] Nombre
        - [ ] Año
        - [ ] Hashtag
    - [ ] Configuración de las imagenes firmadas
        - [ ] Nombres
        - [ ] Tamaño (`maxwidth`)
        - [ ] Configuración de la firma
            - [ ] `ratio_elements`
            - [ ] Texto
                - [ ] Tipografía
                - [ ] Color
                - [ ] Fondo
                - [ ] Posición
            - [ ] Imagen (logo)
                - [ ] Tipografía
                - [ ] Posición

## Agradecimientos
* [Mike](https://www.blog.pythonlibrary.org/author/mld/) por la entrada *[How to Watermark Your Photos with Python](https://www.blog.pythonlibrary.org/2017/10/17/how-to-watermark-your-photos-with-python/)* 
    * Creado: 17 de Octubre de 2017
    * Visto: 1 de Mayo de 2018

## Licencia