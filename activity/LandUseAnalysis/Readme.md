# Análisis geográfico del Modelo de Ocupación Territorial - MOT
Keywords: `land-use-analysis` `mot`

A partir de la capa MOT contenida en el anexo de formulación del POT, realice un análisis estadístico de áreas por clasificación del suelo (urbano, expansión urbana, rural) y categorías definidas en el Modelo de Ocupación Territorial - MOT con porcentaje de distribución respecto al total del área municipal.

<div align="center"><img src="graph/Gravity_anomalies_on_Earth.png" alt="R.SIGE" width="50%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* El mapa CG-01 de Clasificación general del territorio anexo al Plan de Ordenamiento, contiene los valores de áreas y porcentajes de distribución territorial calculadas a partir del CRS 3116. A partir de la capa del Modelo de Ocupación Territorial - MOT, generaremos los polígonos de clasificación y calcularemos las áreas y dis distribuciones porcentuales usando el CRS 9377.


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:open_file_folder:PoblacionDANE.xlsx](LandUseAnalysis.xlsx): libro para comparación de áreas.


## 1. Áreas y porcentajes por clasificación general del territorio

Mapa CG-01 Clasificación general del territorio.<br><sub>Tomado de: Plan de Ordenamiento Territorial Municipio de Zipaquirá, Acuerdo 012 de 2013.</sub><br><img src='../../file/data/POT/Anexo_Acuerdo_012_2013/CG-01.jpg' alt='R.SIGE' width='100%' border='0' /><br>

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _LandUseAnalysis_ y establezca el CRS 9377. En la parte superior de la ventana se encuentran los diferentes mapas y la plantilla de impresión creados en actividades anteriores, ciérrelos.

> Los mapas y plantillas de impresión son almacenados dentro de la estructura del proyecto de ArcGIS Pro, estos pueden ser abiertos directamente desde el arbol de catálogo o _Catalog Pane_.

Agregue al mapa la capa del Modelo de Ocupación Territorial - MOT disponible en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\MOT.shp` y ajuste la simbología a valores únicos representando el campo de atributos `SUELO`, rotule a partir de este mismo campo. Como puede observar, este mapa contiene 5 tipos diferentes de clasificación de suelo, de los cuales, Rural - Suburbano - Protección, pertenecen a la clase rural. 

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues_MOT_Suelo.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Utilizando la herramienta _Data Management Tools / Dissolve_, disuelva los polígonos del Modelo de Ocupación Territorial - MOT a partir del campo de atributos `SUELO`, defina en _Environments_ el sistema de proyección 9377 asignado al mapa. Guarde la capa o clase de entidad resultante en la ruta `\file\shp\MOT_ClasificacionSuelo.shp` y abra la tabla de atributos de la capa inicial y la capa disuelta. Podrá observar que de los 80 polígonos iniciales, hemos obtenido 5 zonas.

<div align="center"><img src="graph/ArcGISPro_MOT_ClasificacionSuelo_shp.png" alt="R.SIGE" width="100%" border="0" /></div>

3. En la tabla de atributos de la capa disuelta, cree los siguientes campos:

<div align="center">

| Campo      | Descripción                                           | Tipo    | Propiedad ArcGIS Pro        | 
|------------|-------------------------------------------------------|---------|-----------------------------| 
| APha3116   | Área planar en hectáreas a partir de CRS 3116         | Double  | Area                        |
| AGha3116   | Área geodésica en hectáreas a partir de CRS 3116      | Double  | Area (geodesic)             |
| APha9377   | Área planar en hectáreas a partir de CRS 9377         | Double  | Area                        |
| AGha9377   | Área geodésica en hectáreas a partir de CRS 9377      | Double  | Area (geodesic)             |
| APhaDP3116 | Distribución porcentual de áreas a partir de APha3116 | Double  | Area (geodesic)             |
| AGhaDP3116 | Distribución porcentual de áreas a partir de AGha3116 | Double  | Area (geodesic)             |
| APhaDP9377 | Distribución porcentual de áreas a partir de APha9377 | Double  | Area (geodesic)             |
| AGhaDP9377 | Distribución porcentual de áreas a partir de AGha9377 | Double  | Area (geodesic)             |

</div>

> CRS 3116: MAGNA Sirgas orígen Bogota.  
> CRS 9377: MAGNA Colombia orígen único nacional.

<div align="center"><img src="graph/ArcGISPro_AddField1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Desde la tabla de atributos, calcule las propiedades geométricas de los campos `APha3116`, `AGha3116`, `APha9377` y `AGha9377`. Como observa, los valores de las áreas planares y geográficas son diferentes en un mismo sistema y también entre los dos CRS calculados.

<div align="center"><img src="graph/ArcGISPro_MOT_ClasificacionSuelo_CalculateGeometry1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_MOT_ClasificacionSuelo_CalculateGeometry2.png" alt="R.SIGE" width="100%" border="0" /></div>

Ajuste los colores del mapa 

<div align="center">

| Categoría        | HEX color |
|------------------|-----------|
| Urbano           | #CDCDCD   |
| Expansión urbana | #D69DBE   |
| Suburbano        | #D6C29F   |
| Protección       | #74B273   |
| Rural            | #FFEABE   |

</div>

## 1.1. Análisis de diferencias

En la siguiente ilustración se pueden observar las diferencias de identificación por categoría del mapa oficial CG-01 con respecto a las asignaciones de categoría de suelo contenidas en la capa _MOT.shp_.

<div align="center"><img src="graph/ArcGISPro_MOT_ClasificacionSuelo_Diferencias1.png" alt="R.SIGE" width="100%" border="0" /></div>



## 2. Áreas y porcentajes en mapa del modelo ocupación territorial - MOT

Agregue al mapa la capa del Modelo de Ordenamiento Territorial - MOT disponible en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\MOT.shp` y ajuste la simbología a valores únicos representando el campo de atributos `SUELO`.  






## 3. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                                                                                         | Procedimiento                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                                                                                      | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                                                         |
| Rotulado                                                                                                        | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                                            |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `


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
| Avance **P1** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P1** | :compass:Mapa digital impreso _P1-1: xxxx_<br>(Incluir xxxxx. Embebidos dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                        | 
| Avance **P1** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

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

| [:arrow_backward: Anterior](../Layout/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|------------------------------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 