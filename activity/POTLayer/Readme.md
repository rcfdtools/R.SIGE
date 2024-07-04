# Inventario de información geo-espacial recopilada 
Keywords: `DEM` `AgreeDEM`

En esta actividad se presenta una tabla resumen de la información geo-espacial (vectorial, ráster) y tablas anexas al POT.

<div align="center"><img src="graph/Gravity_anomalies_on_Earth.png" alt="R.SIGE" width="50%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* 


## Requerimientos

* [:open_file_folder:POT_Layer.xlsx](PoblacionDANE.xlsx): libro para registro de capas y grillas recopiladas del POT.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ArcGIS Pro de ESRI
* [:toolbox:Herramienta](https://qgis.org/): QGIS
* Datos recopilados


## 1. Especificaciones para revisión

En el libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se registran los siguientes atributos:

| Columna       | Alcance de evaluación                                                                                                                                                                 |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipo          | Vector, Tabla, Ráster.                                                                                                                                                                |
| Nombre        | Nombre del elemento. Para archivos que no estén contenidos dentro de una GDB incluir la extensión primaria, p. ej.: .shp, .tif, .dbf, dwg.                                            |
| Alias         | Nombre corto utilizado en listas de elementos sobre mapas. En caso de que no disponga de nombre corto, incluir el Nombre sin extensión.                                               |
| Dataset       | Nombre de GDB / Nombre del grupo de capas. Para archivos que no estén contenidos dentro de una GDB indicar el nombre de la carpeta que contiene el elemento.                          |
| Descripción   | Evalúe la espacialidad de la capa y sus atributos para identificar que contiene y representa.                                                                                         |
| Geometría     | Punto 2D, Punto 3D, Línea 2D, Línea 3D, Polígono 2D, Polígono 3D, N/A o no aplica. Grillas ráster y tablas de datos no contienen geometría.                                           |
| Fuente datos  | Fuente de datos original de la capa.                                                                                                                                                  |
| Registros     | Total de entidades contenidas dentro de la tabla de atributos. Para grillas incluir en una fórmula el resultado obtenido de multiplicae el número de filas por el número de columnas. |
| CRS           | Sistema de proyección de coordenadas                                                                                                                                                  |
| Límite norte  | Extensión espacial al norte en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                            |
| Límite sur    | Extensión espacial al sur en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                              |
| Límite este   | Extensión espacial al este en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                             |
| Límite oeste  | Extensión espacial al oeste en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                            ||               |                                                                                                                                                  |
| Observaciones | Observaciones relacionadas con el contenido y su visualización.                                                                                                                       |


## 2. Descarga de información

Información geo-espacial del Plan de Ordenamiento Territorial Municipio de Zipaquirá, Acuerdo 012 de 2013 disponibles.

1. Ingrese a www.colombiaot.gov.co y de clic en la opción _Los POT del País_

<div align="center"><img src="graph/ColombiaOT_1.png" alt="R.SIGE" width="100%" border="0"/></div>

2. En el buscador de Colombia OT, realizar los siguientes filtros:

* Filtra por entidad territorial: Zipaquirá 
* Forma de representación: Cartografía
* Tipo: Dato

Luego, desde su navegador busque los resultados cuyo formato sea .zip y descargue estos archivos.

<div align="center"><img src="graph/ColombiaOT_2.png" alt="R.SIGE" width="100%" border="0"/></div>

<div align="center">

Listado de archivos obtenidos

| Archivo                                                                                                                                     | Formato   | Tamaño (KB) | 
|:--------------------------------------------------------------------------------------------------------------------------------------------|:----------|:------------|
| [:floppy_disk:Barrios.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Barrios.zip)                                                      | Shapefile | 19          |
| [:floppy_disk:Comunas.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Comunas.zip])                                                     | Shapefile | 7           |
| [:floppy_disk:Expansion_Urbana_Ajustada_Predios.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Expansion_Urbana_Ajustada_Predios.zip ) | Shapefile | 10          |
| [:floppy_disk:Hidrografia.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Hidrografia.zip)                                              | Shapefile | 263         |
| [:floppy_disk:ModeloOrdenamientoTerritorial.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/ModeloOrdenamientoTerritorial.zip)          | Shapefile | 1031        |
| [:floppy_disk:Orden_Vial.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Orden_Vial.zip)                                                | Shapefile | 184         |
| [:floppy_disk:Rio_Bogota.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Rio_Bogota.zip)                                                | Shapefile | 52          |
| [:floppy_disk:Vereda.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vereda.zip)                                                        | Shapefile | 535         |
| [:floppy_disk:Vias.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias.zip)                                                            | Shapefile | 3           |
| [:floppy_disk:Vias_Perimetro.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Perimetro.zip)                                        | Shapefile | 64          |
| [:floppy_disk:Vias_Perimetro_Urbano.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Perimetro_Urbano.zip)                          | Shapefile | 77          |
| [:floppy_disk:Vias_Rurales.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Rurales.zip)                                            | Shapefile | 184         |
| [:floppy_disk:Vias_Urbanas.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Urbanas.zip)                                            | Shapefile | 73          |
| [:floppy_disk:Zona_Urbana_Ajustada_Predios.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Zona_Urbana_Ajustada_Predios.zip)            | Shapefile | 29          |
| [:floppy_disk:25899.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/25899.zip)                                                          | GDB       | 57464       |

</div>

> Renombre los archivos comprimidos con los nombres indicados en la tabla anterior.

3. En su repositorio de proyecto y dentro de la carpeta `\file\data\POT\Anexo_Acuerdo_012_2013\shp\`, guarde y descomprima los archivos vectoriales en formato Shapefile.

<div align="center"><img src="graph/Data_POT_shp.png" alt="R.SIGE" width="100%" border="0"/></div>




## 2. Procedimiento en ArcGIS Pro

1. Descargue los 





## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P1** | Esta actividad no requiere del desarrollo de elementos en el avance P1 del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                     | 
| Avance **P1** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. |

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* 



## Referencias

* 


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../xxxx) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|---------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 