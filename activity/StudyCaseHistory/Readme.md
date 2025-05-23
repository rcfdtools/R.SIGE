# Reseña histórica y geográfica municipal del caso de estudio  
Keywords: `History` `StudyCase`

Zipaquirá es un municipio de Colombia ubicado en el departamento de Cundinamarca, en la provincia de Sabana Centro, de la que es capital. Es el segundo municipio más grande y poblado de la provincia. Es uno de los centros de explotación de sal más importantes del país, razón por la que también es conocida como la Capital Salinera de Colombia.

<div align="center"><img src="graph/StudyCaseHistory.png" alt="R.SIGE" width="50%" border="0" /><sub><br>Áreas homogéneas de tierra - Municipio de Zipaquirá (norte hacia arriba)<br>Tomado de: <a href="https://www.colombiaenmapas.gov.co">https://www.colombiaenmapas.gov.co</a></sub><br><br></div>

> Reseña histórica es una expresión que se utiliza para explicar o repasar los hechos del pasado reciente o lejano, de un asunto determinado.


## Objetivos

* Entender el contexto histórico y geográfico del municipio del caso de estudio
* Identificar información geo-espacial disponible en fuentes de datos públicas


## Requerimientos

* [:people_holding_hands:Grupo de trabajo](https://forms.office.com/r/kQMcvm3awd): integrantes y código asignado para desarrollo del proyecto.
* :label:Caso de estudio: revisado y aprobado para el grupo de trabajo.


## 1. Historía del municipio [^1]

De fundación prehispánica, sus pobladores se asentaban en el sector hoy conocido como "Pueblo viejo" a 200 metros aproximados de su actual emplazamiento. Fue erigida como villa el 18 de julio de 1600 por auto de poblamiento proferido por el oidor español Luis Henríquez. Fue sucesivamente capital de la Provincia de Cundinamarca (1851), de la Provincia de Zipaquirá (1852-1855), del Estado Soberano de Cundinamarca (1861-1864), del departamento de Quesada (1905-1908) y del departamento de Zipaquirá (1908-1910). Zipaquirá es reconocida a nivel internacional por su Catedral de Sal, la cual recibió el reconocimiento como primera de las "Siete maravillas de Colombia” el 4 de febrero de 2007, además de su casco urbano, el cual fue declarado patrimonio histórico y cultural de Colombia.


## 2. Localización geográfica y topografía [^1]  

La ciudad de Zipaquirá está situada en el Valle de El Abra, sobre la cordillera Oriental, en el altiplano Cundiboyacense. El casco urbano se encuentra a una altitud de 2652 m.s.n.m., lo que la convierte en la tercera ciudad con mayor altitud en Colombia con más de 100.000 habitantes de acuerdo a la lista de las grandes ciudades más altas del mundo. Zipaquirá posee una extensión aproximada de 197 km² así: 8 km² de la zona urbana y 189 km² de la zona rural. El territorio donde se asienta la ciudad fue en el pasado un gran campo lleno de vegetación; algunos sectores de la ciudad también están construidos sobre unos viejos fosos de agua-sal, en los que la sal vigua era procesada para su consumo. Su río principal más extenso es el río Bogotá, pasando por el borde oriental de Zipaquirá en límites con Tocancipá y Sopó que desde hace varias décadas presenta altos niveles de contaminación, finalizando en Girardot. La zona en donde está ubicada la ciudad corresponde a la placa tectónica sudamericana, por lo que presenta una importante actividad sísmica.

<div align="center">

Información [DANE](https://www.dane.gov.co/)

| Localización                 | Descripción                                                                                  |
|------------------------------|:---------------------------------------------------------------------------------------------|
| Departamento de Cundinamarca | Código DANE: 25                                                                              |
| Municipio de Zipaquirá       | Código DANE: 899                                                                             |
| Dirección territorial        | Gestor territorial: Municipio de Zipaquirá según Resolución IGAC 96 del 9 de Febrero de 2021 |
| Categoría                    | 1                                                                                            |

> Para conocer su gestor catastral territorial, en www.colombiaenmapas.gov.co buscar en la temática Catastro: _"Gestores Catastrales Colombia"_. Dentro del marco de la política de Catastro Multipropósito del Gobierno Nacional, el Instituto Geográfico Agustín Codazzi (IGAC) habilitó diferentes entidades, como gestores catastrales, con el objetivo de empoderar a los entes territoriales y que puedan mejorar la gestión de sus territorios.

La zona rural del municipio está compuesta por diecisiete (17) veredas

| Vereda              | Código DANE    |
|:--------------------|:---------------|
| Barandillas         | 2589900000015  |
| Barro Blanco        | 2589900000013  |
| Centro              | 2589900000002  |
| El Cedro            | 2589900000007  |
| El Empalizado       | 2589900000010  |
| El Tunal            | 2589900000005  |
| La Granja           | 2589900000006  |
| Pantano Redondo     | 2589900000008  |
| Páramo del Guerrero | 2589900000009  |
| Paso Ancho          | 2589900000004  |
| Portachuelo         | 2589900000003  |
| Río Frío            | 2589900000012  |
| San Isidro          | 2589900000011  |
| San Jorge           | 2589900000014  |

<img src="graph/25899Vereda.png" alt="R.SIGE" width="70%" border="0"/><br><sub>Veredas DANE (norte hacia arriba). Expresión de rotulado en QGIS: QGIS: "nombre" ||'\n'|| 'A: ' ||Round("Akm2", 2) || 'km²'<br>Elaborado por rcfdtools</sub>

En la zona rural se encuentran los siguientes centros poblados

| Centro poblado Rural - CPR | Vereda      |
|:---------------------------|:------------|
| Argélia                    | El Cedro    |
| Aposentos altos            | El Cedro    |
| Barandillas                | La Granja   |
| Bolívar 83                 | El Cedro    |
| Bosques de Silesia         | El Cedro    |
| El Rudal                   | Paso Ancho  |
| La Mariela                 | La Granja   |
| La Paz                     | Paso Ancho  |
| Malagón                    | La Granja   |
| Pasoancho                  | Paso Ancho  |
| Portachuelo                | Portachuelo |
| San Jorge                  | San Jorge   |
| San Miguel                 | La Granja   |
| Santa Isabel               | La Granja   |

<img src="graph/25899CentroPobladoRural.png" alt="R.SIGE" width="100%" border="0"/><br><sub>Centros poblados (norte hacia arriba)<br>En la ilustración se han excluido las veredas: Empalizado, Páramo de Guerrero, San Isidro, Pantano Redondo y Río Frío.<br>Elaborado por rcfdtools</sub>

</div>

> La Ley 388 de 1997 y el Decreto 1077 de 2015 se refieren a los centros poblados rurales, que forman parte de la definición de núcleos de población, caracterizados como asentamientos humanos agrupados en un conjunto de construcciones independientes y próximas, que comparten circulaciones e infraestructuras de servicios comunes. El artículo 2.2.2.2.3.2. del Decreto 1077 se refiere al ordenamiento de los centros poblados rurales y establece que el componente rural de los POT debe definir, entre otros aspectos, su delimitación, y los usos principales, compatibles, condicionados y prohibidos.
>
> Direcciones territoriales tomadas de www.colombiaenmapas.gov.co

## 3. Principales actividades económicas

Las principales actividades económicas del municipio son:

* Agropecuaria: ganadería, cultivos de flores, cultivos de papa
* Industrial: extracción, procesamiento y refinamiento de sal
* Turística: Catedral de Sal


## 4. Mapas de referencia

Información geo-espacial específica del municipio que puede ser consultada en línea a través de los siguientes portales, plataformas o servicios:

| Plataforma                                                | Información consultable                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Colombia en Mapas](https://www.colombiaenmapas.gov.co/)  | Áreas Homogéneas de Tierras - Municipio de Zipaquirá, Cundinamarca. Capacidad de Uso - Levantamiento detallado de Suelos en las áreas planas de los municipios de Cogua, El Rosal, Nemocón, Subachoque, Suesca, Zipacón y Zipaquirá del departamento de Cundinamarca a escala 1:10.000. En la cartografía básica a escala 1:500k, 1:100k y 1:25k se encuentran múltiples vectores sobre el municipio. |
| [Google Maps y Google Earth](https://www.google.com/maps) | Disponible: mapa satelital, mapa vial, mapa de terreno, mapa de tráfico, street view, puntos de interés, límite urbano                                                                                                                                                                                                                                                                                |
| [Microsoft Bing Maps](https://www.bing.com/maps)          | Disponible: mapa satelital, mapa vial combinado con terreno, puntos de interés                                                                                                                                                                                                                                                                                                                        |
| [Open Street Maps ](https://www.openstreetmap.org)        | Disponible: mapa vial, mapa de terreno                                                                                                                                                                                                                                                                                                                                                                |
| Sistema de información geográfica municipal               | No disponible o no encontrado                                                                                                                                                                                                                                                                                                                                                                         |


### 4.1. Colombia en Mapas

[Colombia en Mapas](https://www.colombiaenmapas.gov.co/inicio/) es la colección más completa de mapas de Colombia. Es una herramienta en constante evolución. Construido para que todos los colombianos puedan consumir los datos, productos y servicios geográficos. No estamos solos en esto. Colombia en Mapas es el vehículo que dispone y centraliza la información geográfica producida por el IGAC y por todas las entidades nacionales, regionales y locales que generan datos del territorio, con el fin de promover la toma de decisiones efectivas del gobierno, las industrias y el ciudadano.

<div align="center"><img src="graph/IGAC_ColombiaEnMapas.png" alt="R.SIGE" width="80%" border="0" /><sub><br>Zipaquirá en Colombia en Mapas del IGAC<br>Tomado de: <a href="https://www.colombiaenmapas.gov.co">https://www.colombiaenmapas.gov.co</a></sub><br><br></div>


**Áreas Homogéneas de Tierras. Municipio de Zipaquirá, Cundinamarca**

El mapa digital de Áreas Homogéneas de Tierras (AHT) con fines multipropósito a escala 1:25.000, representa características y cualidades similares de clima, relieve, material litológico o depósitos superficiales que dan origen a los suelos, lo cual permite delimitar espacios de la superficie terrestre en trece clases de AHT e identificarlas según sus principales limitaciones y caracterizarlas, a través de un índice numérico denominado valor potencial, que expresa la capacidad productiva de las tierras. Esta información geográfica se constituye en una de las más importantes aplicaciones de los levantamientos de suelos a diferentes escalas cartográficas, siendo el insumo base para calificar la capacidad productiva de las tierras rurales.

Este producto es generado por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi  - IGAC, para el municipio de Zipaquirá (Cundinamarca) a escala 1:25.000.

<div align="center"><img src="graph/IGAC_AHT.png" alt="R.SIGE" width="80%" border="0" /><sub><br>Áreas Homogéneas de Tierras. Municipio de Zipaquirá, Cundinamarca<br>Tomado de: <a href="https://www.colombiaenmapas.gov.co">https://www.colombiaenmapas.gov.co</a></sub><br><br></div>


**Capacidad de Uso. Levantamiento detallado de Suelos en las áreas planas de los municipios de Cogua, El Rosal, Nemocón, Subachoque, Suesca, Zipacón y Zipaquirá del departamento de Cundinamarca a escala 1:10.000**

Mapa temático que representa la clasificación por Capacidad de Uso de las Tierras de las áreas planas de los municipios de Cogua, el Rosal, Nemocón, Subachoque, Suesca, Zipacón y Zipaquirá, Departamento de Cundinamarca a escala 1:10.000, publicado en el año 2013. Suministra información importante acerca del recurso suelo, a través de la determinación de las potencialidades y limitaciones de uso de las tierras a partir del análisis de las características de los suelos. Se definen las unidades cartográficas de capacidad de uso de la tierra con sus respectivos componentes: Clase, Subclase, Grupo de manejo, Principales Limitantes y Prácticas de Manejo.

Este producto es generado por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi - IGAC, para el Departamento de Cundinamarca.

<div align="center"><img src="graph/IGAC_CUT.png" alt="R.SIGE" width="80%" border="0" /><sub><br>Capacidad de Uso. Levantamiento detallado de Suelos en las áreas planas de los municipios de Cogua, El Rosal, Nemocón, Subachoque, Suesca, Zipacón y Zipaquirá del departamento de Cundinamarca a escala 1:10.000<br>Tomado de: <a href="https://www.colombiaenmapas.gov.co">https://www.colombiaenmapas.gov.co</a></sub><br><br></div>


### 4.2. Mapas disponibles en Google Maps y Google Earth

<div align="center">
<img src="graph/GoogleMaps_Road.png" alt="R.SIGE" width="480" border="0" />
<img src="graph/GoogleMaps_Satellite.png" alt="R.SIGE" width="480" border="0" />
<img src="graph/GoogleMaps_Terrain.png" alt="R.SIGE" width="480" border="0" />
<img src="graph/GoogleMaps_Traffic.png" alt="R.SIGE" width="480" border="0" />
<img src="graph/GoogleEarth_Everything.png" alt="R.SIGE" width="480" border="0" />
</div>


### 4.3. Mapas disponibles en Microsoft Bing Maps

<div align="center">
<img src="graph/Bing_Road.png" alt="R.SIGE" width="480" border="0" />
<img src="graph/Bing_Satellite.png" alt="R.SIGE" width="480" border="0" />
</div>


### 4.4. Mapas disponible en OpenStreet

<div align="center">
<img src="graph/OpenStreetMap_Road.png" alt="R.SIGE" width="480" border="0" />
<img src="graph/OpenStreetMap_Road_Terrain.png" alt="R.SIGE" width="480" border="0" />
</div>


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P1** | Investigue y documente la reseña histórica municipal del caso de estudio asignado. Consulte y documente que información geográfica puede ser consultada o descargada desde las plataformas indicadas en esta actividad o desde plataformas que utilice frecuentemente en su trabajo profesional.                                                                                                                                                    | 
| Avance **P1** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. |

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* https://es.wikipedia.org/wiki/Zipaquir%C3%A1
* https://www.colombiaenmapas.gov.co/inicio/
* [Geovisor del municipio de Zipaquirá](https://www.arcgis.com/apps/webappviewer/index.html?id=122af7ada9f1415692af27e9239a6d49)


## Control de versiones

| Versión    | Descripción                                  | Autor                                      | Horas |
|------------|:---------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.20 | Versión inicial con alcance de la actividad  | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.25 | Reseña histórica del caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   4   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../CRS/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/5)  | [Siguiente :arrow_forward:](../Population/Readme.md) |
|-----------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------|

[^1]: Tomado o adaptado de https://es.wikipedia.org/wiki/Zipaquir%C3%A1