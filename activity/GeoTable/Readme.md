# Tablas geo-codificadas del POT
Keywords: `geo-table` `table-to-point` `point-to-line` `line-to-polygon`

A partir de las tablas geo-codificadas contenidas en el Acuerdo o Decreto que reglamenta el POT, cree una tabla integrada con diferentes atributos y secuencias, que permitan generar los nodos y polígonos de la zona urbana, zona de expansión urbana, centros poblados, áreas institucionales, recreativas, culturales, de servicios, distritos especiales, zonas de vivienda y otra áreas de interés especial. Utilizando imágenes satelitales y los polígonos de la cartografía del POT, evalué la espacialidad de los polígonos creados. 

<div align="center"><img src="graph/GeoTable.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* 


## Requerimientos

* [:mortar_board:Actividad](../POTStudyZone/Readme.md): Ordenamiento Territorial de la zona de estudio.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:open_file_folder:POTGeoTable.xlsx](POTGeoTable.xlsx): libro con tablas geo-codificadas del POT.


## 1. Creación de tabla geo-codificada

La geo-codificación, es el proceso de transformar una descripción de una ubicación (por ejemplo, un par de coordenadas, una dirección o un nombre de un lugar) en una ubicación de la superficie de la Tierra. Se puede geo-codificar introduciendo una descripción de una ubicación a la vez o proporcionando muchas de ellas al mismo tiempo en una tabla. Las ubicaciones que se obtienen se transforman en entidades geográficas con atributos, que se pueden utilizar para la representación cartográfica o él para análisis espacial. Con la geoc-odificación, puede buscar varios tipos de ubicaciones de manera rápida. Los tipos de ubicaciones que puede buscar incluyen: puntos de interés o nombres de un diccionario geográfico, como montañas, puentes y negocios; coordenadas basadas en latitud y longitud o en otros sistemas de referencia.[^1]

1. A partir de las tablas geo-codificadas contenidas en los Artículos 12, 13, 14, 15 y 134 del Acuerdo Municipal 012 de 2013, cree un libro de Microsoft Excel con el nombre [POTGeoTable.xlsx](POTGeoTable.xlsx) (guarde en la carpeta _\table_) que contenga una hoja con el nombre _POTGeoTable_ y que incluya las siguientes columnas de atributos:

<div align="center">

| Columna    | Descripción                                                                           |
|------------|---------------------------------------------------------------------------------------|
| Suelo      | Clasificación de suelo: Urbano, Rural, Expansión urbana, Suburbano.                   |
| ZonaID     | Numero consecutivo por cada zona identificada.                                        |
| ZonaNombre | Nombre de la zona.                                                                    |
| Punto      | Número de punto, 1 a n por zona.                                                      |
| CX         | Coordenada X en metros. Para el caso de estudio corresponde a valores en el CRS 3116. |
| CY         | Coordenada Y en metros. Para el caso de estudio corresponde a valores en el CRS 3116. |
| Norma      | Artículo del Acuerdo o Decreto Municipal.                                             |

</div>

2. Desde el Acuerdo Municipal, registre los valores en el libro de Excel.

> Es recomendable convertir el documento de Adobe Acrobat a un formato editable, para de poder copiar correctamente los elementos multilínea contenidos en las tablas.

Por ejemplo, para el artículo 12 correspondiente a la delimitación del suelo urbano:

<div align="center"><img src="graph/Acuerdo012_Art12.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Acuerdo012_Art12Table.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Excel_POTGeoTable1.png" alt="R.SIGE" width="100%" border="0" /></div>

Repita el mismo procedimiento para los demás artículos que incluyen tablas geo-codificadas. Una vez terminado, obtendrá para este Acuerdo, los registros de localización para 35 zonas diferentes.

<div align="center">Tabla resumen en suelo urbano y número de nodos<br><img src="graph/Excel_POTGeoTableUrbano.png" alt="R.SIGE" width="40%" border="0" /></div><br>

<div align="center">Tabla resumen en suelo de expansión urbana y número de nodos<br><img src="graph/Excel_POTGeoTableExpansionUrbana.png" alt="R.SIGE" width="60%" border="0" /></div><br>

<div align="center">Tabla resumen en suelo suburbano y número de nodos<br><img src="graph/Excel_POTGeoTableSuburbano.png" alt="R.SIGE" width="75%" border="0" /></div><br>

<div align="center">Tabla resumen en suelo rural y número de nodos<br><img src="graph/Excel_POTGeoTableRural.png" alt="R.SIGE" width="50%" border="0" /></div><br>

> Tenga en cuenta, que el suelo suburbano también hace parte de la zona rural.


## 2. Creación y re-proyección de polígonos

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _PopulationGIS_ y establezca el CRS 9377. Agregue al mapa la capa del Modelo de Ocupación Territorial - MOT disponible en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\MOT.shp` y ajuste la simbología a valores únicos representando el campo de atributos `SUELO`.  

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues_MOT_Suelo.png" alt="R.SIGE" width="100%" border="0" /></div>

<div align="center"><img src="graph/ECEF.svg" alt="R.SIGE" width="50%" border="0" /><sub><br>Diagram of Earth Centered, Earth Fixed coordinates in relation to latitude and longitude.<br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:ECEF.svg">https://commons.wikimedia.org</a></sub><br><br></div>


## 3. Verificación de límites utilizando imágenes satelitales





## 34. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                                                                                         | Procedimiento                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                                                                                      | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                                                         |
| Rotulado                                                                                                        | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                                            |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)


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
| Avance **P3** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P3** | :compass:Mapa digital impreso _P3-1: xxxx_<br>Incluir xxxxx.<br>Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                       | 
| Avance **P3** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.



## Referencias

* [¿Qué es la geocodificación?](https://desktop.arcgis.com/es/arcmap/latest/manage-data/geocoding/what-is-geocoding.htm)


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../Digitizing/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------|-------------------------------|

[^1]: https://desktop.arcgis.com/es/arcmap/latest/manage-data/geocoding/what-is-geocoding.htm