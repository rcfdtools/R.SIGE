# Georreferenciación
Keywords: `CRS` `SRS` `EPSG-4326` `WGS84`

La georreferenciación es el uso de coordenadas de mapa para asignar una ubicación espacial a entidades cartográficas. Todos los elementos de una capa de mapa tienen una ubicación geográfica y una extensión específicas que permiten situarlos en la superficie de la Tierra o cerca de ella. La capacidad de localizar de manera precisa las entidades geográficas es fundamental tanto en la representación cartográfica como en SIG. Tomado de [ArcGIS Resources](https://resources.arcgis.com/es/help/getting-started/articles/026n0000000s000000.htm).

<div align="center"><img src="graph/ECEF.svg" alt="R.SIGE" width="50%" border="0" /><sub><br>Diagram of Earth Centered, Earth Fixed coordinates in relation to latitude and longitude.<br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:ECEF.svg">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* 


## Requerimientos

* Lectura - [Georreferenciación y sistemas de coordenadas](https://resources.arcgis.com/es/help/getting-started/articles/026n0000000s000000.htm)
* Lectura - [¿Qué son las proyecciones cartográficas?](https://resources.arcgis.com/es/help/main/10.1/index.html#//003r00000001000000)
* Lectura - [Forma de la tierra](https://es.wikipedia.org/wiki/Forma_de_la_Tierra)


## ¿Qué es la georrefenciación y qué es un sistema de proyección de coordenadas?[^1]

La forma teórica que convencionalmente se utiliza para definir la Tierra es el Geoide qué se define teóricamente a partir del nivel medio de los mares. Debido a su forma irregular y para la definición de una forma geométrica que pueda ser resuelta matemáticamente de forma simple se utilizan los conceptos de esfera y elipsoide

La georreferenciación es el proceso utilizado para determinar la posición de un objeto o un conjunto de datos mediante un sistema de coordenadas referidas a la superficie terrestre. Los sistemas de coordenadas son un conjunto de parámetros que permiten definir inequívocamente la posición de cualquier punto en un espacio geométrico respecto a un punto denominado origen.

<div align="center"><img src="graph/Topografia-geoide-y-elipsoide.jpg" alt="R.SIGE" width="30%" border="0" /><sub><br>Relaciones geométricas entre la superficie topográfica de la Tierra, 
el geoide y el elipsoide, necesarias para una cartografía de precisión 
<br>Tomado de: <a href="http://www.albireotopografia.es/topografia-basica-iii-la-forma-de-la-tierra/">www.albireotopografia.es</a></sub><br><br></div>


## Sistemas de referencia y proyección cartográfica en Colombia

Las coordenadas determinadas para el desarrollo de proyectos que requieran datos espaciales deben estar ligadas al **Marco Geocéntrico Nacional de Referencias – MAGNA**, razón por lo cual es necesario regirse por las **“Técnicas de georreferenciación para levantamientos topográficos ligados a MAGNA”** expedidos por el Instituto Geográfico Agustín Codazzi – IGAC.


### Sistema de referencia horizontal datum MAGNA-SIRGAS, EPSG:4686

Mediante resolución No. 068 de 2005 se adoptó como único datum oficial de Colombia el Marco Geocéntrico Nacional de Referencia MAGNA (Según resolución MAGNA-SIRGAS), cuyos parámetros son:

| Parámetro                                                                                                                                          | Valor                                            |
|:---------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------|
| Código [EPSG](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset)                                                                       | 4686                                             |
| Primer meridiano                                                                                                                                   | Greenwich 0,000000000000000000 Grados decimales  |
| [Datum geodésico](https://es.wikipedia.org/wiki/Sistema_de_referencia_geod%C3%A9sico)                                                              | MAGNA_SIRGAS                                     |
| [Elipsoide](https://es.wikipedia.org/wiki/Elipsoide)                                                                                               | GRS 1980                                         |
| Semieje mayor (a), metros                                                                                                                          | 6378137                                          |
| Semieje menor (b), metros                                                                                                                          | 6356752.314                                      |
| Aplanamiento inverso o recíproco (1/f), f = (a - b) / a                                                                                            | 298.2572201                                      |
| [ITRF](https://en.wikipedia.org/wiki/International_Terrestrial_Reference_System_and_Frame) - International Terrestrial Reference System and Frame  | 1994, Época 1995.4                               |

> Los valores del semieje mayor y semieje menor corresponden a los parámetros del elipsoide.

<div align="center"><img src="graph/EPSG4686.png" alt="R.SIGE" width="70%" border="0" /><sub><br>Visualización de sistema de proyección usando QGIS
<br>Tomado de: <a href="https://qgis.org/">https://qgis.org/</a></sub><br><br></div>


## Referencias

* https://resources.arcgis.com/es/help/getting-started/articles/026n0000000s000000.htm
* http://www.albireotopografia.es/topografia-basica-iii-la-forma-de-la-tierra/topografia-geoide-y-elipsoide/


## Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2024.06.25 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../xxxx) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|---------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: https://geoportal.igac.gov.co