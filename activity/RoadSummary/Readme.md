# Análisis estadístico de la red vial
Keywords: `road-summary` `summarize`

A partir de las capas orden vial y red vial urbana, contenidas en los anexos de formulación del POT, realice un análisis estadístico de longitud de vías por orden vial y longitud de vías urbanas por tipo.

<div align="center"><img src="graph/AddedValue.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* 


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:notebook:Lectura](https://edu.gcfglobal.org/es/estadistica-basica/): Conocimientos básicos en estadística.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Procedimiento general

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _RoadSummary_ y establezca el CRS 9377. Agregue al mapa desde la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\` las capas VIAS_PERIMETRO_URBANO.shp, ORDEN_VIAL.shp y MOT.shp, ajuste los colores para diferenciar las vías urbanas de las rurales y en el MOT, filtre la zona urbana y de expansión. 

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Verifique las vías en el contorno de la zona urbana, podrá observar que varios de los tramos rurales se extienden dentro de esta zona y que en la mayoría de los casos, en la red vial urbana, ya se encuentran digitalizados. Para integrar estas dos capas en una única capa de análisis, primero crearemos una copia de las capas para editar su contenido.

Desde la tabla de contenido y utilizando la herramienta _Data / Export Features_, exporte en la carpeta `\file\data\shp\`, las capas viales como _Vial_Urbano.shp_ y _Vial_Rural.shp_, asigne desde Environments el CRS 9377. En las vías rurales, conserve únicamente los atributos `Layer`, _ORDEN_VIAL_ y `VIAS_`. En la capa Vial_Urbano, elimine los campos `OBJECTID_1`, `SHAPE_Leng` y `LONGI`.  

<div align="center"><img src="graph/ArcGISPro_ExportFeatures1.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Para las dos capas, cree los siguientes campos en la tabla de atributos:

| Campo      | Descripción                      | Tipo       | Propiedad ArcGIS Pro | 
|------------|----------------------------------|------------|----------------------| 
| ZonaNombre | Rural, Urbano                    | Text (100) | N/A                  |
| NombreVia  | Nombre de la vía                 | Text (100) | N/A                  |
| LGkm       | Longitud geodésica en kilómetros | Double     | Area (geodesic)      |

<div align="center"><img src="graph/ArcGISPro_AddField1.png" alt="R.SIGE" width="100%" border="0" /></div>





## 2. Análisis usando software libre - QGIS

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
| Avance **P1** | :compass:Mapa digital impreso _P1-1: xxxx_<br>Incluir xxxxx.<br>Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                      | 
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

| [:arrow_backward: Anterior](../xxxx) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|---------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 