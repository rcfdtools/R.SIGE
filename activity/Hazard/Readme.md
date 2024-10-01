# ArcGIS Pro - Análisis de amenazas naturales
Keywords: `hazard`

A partir de los conceptos aprendidos en este curso y de la investigación de geo-procesos complementarios, desarrollaremos un procedimiento que permite obtener el mapa de amenazas de Colombia, incluye: flujograma de procesos indicando el nombre de los geoprocesos a utilizar, ejecución paso a paso de los geoprocesos indicados con visualización de mapas y tablas de atributos. Utilizando el mapa de amenazas obtenido y mediante un recorte hasta la zona límite del Modelo de Ocupación Territorial - MOT de la zona de estudio, determinar el riesgo ponderado en función de las áreas de cada clase.                           

<div align="center"><img src="graph/AddedValue.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* 


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:notebook:Lectura](https://edu.gcfglobal.org/es/estadistica-basica/): Conocimientos básicos en estadística.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:open_file_folder:PoblacionDANE.xlsx](PoblacionDANE.xlsx): libro para registro y proyección de población DANE.


## 0. Capas requeridas y pesos

<div align="center">

| Mapa / Capa                                                                            | Descripción                                                           |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Colombia.shp                                                                           | Departamentos de Colombia - IGAC                                      |
| SusceptibilidadDeslizamientos2010.tif<br><sub>\file\data\IDEAM\Susceptibilidad\ </sub> | Mapa de susceptibilidad a deslizamientos - IDEAM - 2010               |
| SusceptibilidadInundacion500K2010.shp<br><sub>\file\data\IDEAM\Susceptibilidad\ </sub> | Mapa de susceptibilidad por inundación escala 1:500K - IDEAM - 2010   |
| AmenazaV.shp<br><sub>\file\data\SGC\AmenazaVolcanica\ </sub>                           | Mapa de amenazas volcánicas - SGC                                     |
| ZonaAmenazaNSR10a.shp<br><sub>\file\data\SGC\ </sub>                                   | Zonas amenaza Sísmica NSR-10 - SGC                                    |
| SuscMM_100kReclass.tif<br><sub>\file\data\SGC\SuscMM_2019web\ </sub>                   | Mapa de susceptibilidad por movimientos en masa - SGC                 |
| Tsunami.mpr                                                                            | Regiones con amenazas de tsunamí debidas a ondas inducidas por sismos |
| Rivers.mpr                                                                             | Regiones con actividad torrencial en ríos                             |
| Beach.mpr                                                                              | Regiones con erosión en playas y/o acumulación de sedimentos          |
| Topograp.mpr                                                                           | Regiones topográficas de Colombia                                     |
| Colombia.mpa                                                                           | Límites de departamentos de Colombia en formato vectorial             |

</div>

<div align="center">Mapa de susceptibilidad a deslizamientos - IDEAM - 2010<br>(SusceptibilidadDeslizamientos2010.tif)<br>

| Valor  | Nombre    |   R   |  G   |  B   | (W) Peso |
|:------:|:----------|:-----:|:----:|:----:|:--------:|
|   0    | Nula      |  225  | 225  | 225  |    0     |
|   1    | Muy Baja  |  56   | 168  |  0   |    0     |
|   2    | Baja      |  139  | 209  |  0   |    1     |
|   3    | Media     |  255  | 255  |  0   |    5     |
|   4    | Alta      |  255  | 128  |  0   |   7.5    |
|   5    | Muy Alta  |  255  |  0   |  0   |    10    |

</div>

<div align="center">Mapa de susceptibilidad por inundación escala 1:500K - IDEAM - 2010<br>(SusceptibilidadInundacion500K2010.shp)<br>

| Simbologia | Nombre     |  WInundat  |
|:----------:|:-----------|:----------:|
|     1      | Inundación |     5      |

</div>



## 1. Procedimiento general en ArcGIS Pro

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _PopulationGIS_ y establezca el CRS 9377. Agregue al mapa la capa del Modelo de Ocupación Territorial - MOT disponible en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\MOT.shp` y ajuste la simbología a valores únicos representando el campo de atributos `SUELO`.  

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues_MOT_Suelo.png" alt="R.SIGE" width="100%" border="0" /></div>

<div align="center"><img src="graph/ECEF.svg" alt="R.SIGE" width="50%" border="0" /><sub><br>Diagram of Earth Centered, Earth Fixed coordinates in relation to latitude and longitude.<br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:ECEF.svg">https://commons.wikimedia.org</a></sub><br><br></div>


En este momento ya dispone de la grilla de terreno reacondicionada requerida para el relleno de sumideros.



## 2. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso            | Procedimiento                                                           |
|:-------------------|:------------------------------------------------------------------------|
| Simbología         | Modificable desde las propiedades de la capa en la pestaña _Symbology_. |
| Rotulado           | Modificable desde las propiedades de la capa en la pestaña _Labels_.    |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)  
[:notebook:Herramientas comúnmente utilizadas en QGIS](../QGIS.md)


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre                           | Descripción                                                                                                                  | Geometría   | Registros | 
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
|                                  |                                                                                                                              | Polígono 2D | 14        | 
|                                  |                                                                                                                              | Polígono 2D | 14        | 
|                                  |                                                                                                                              | Polígono 2D | 14        | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.



## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P7** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P7** | :compass:Mapa digital impreso _P7-1: xxxx_<br>Incluir xxxxx. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                          | 
| Avance **P7** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* 


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../ILWISHazard/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|-------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------|-------------------------------|

[^1]: 