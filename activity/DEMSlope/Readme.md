# Mapa de pendientes de terreno
Keywords: `dem` `agreedem`

A partir del modelo de terreno ESA Copernicus, crear: mapa de relleno de sumideros FIL, mapa de pendientes en tasa porcentual, mapa de pendientes reclasificadas en 9 clases utilizando las especificaciones definidas en el dominio `Dom_PenSuelo` del modelo nacional para presentación de licencias ambientales del [ANLA](https://www.anla.gov.co/). Para cada zona geopolítica municipal y para cada polígono de categoría de suelo disponible en el MOT, calcule la pendiente mínima, media y máxima e identifique incompatibilidades (por ejemplo, zonas con pendientes altas definidas para desarrollos urbanos, de centros poblados, implantación de equipamientos).

<div align="center"><img src="graph/DEMSlope.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Rellenar sumideros en el modelo digital de elevación para ajuste de pendientes no existentes.
* Crear y reclasificar el mapa de pendientes.
* Estimar la pendiente característica municipal, en cada zona geopolítica municipal y para cada categoría del suelo en el MOT.
* Identificar incompatibilidades de pendientes altas en zonas con asentamientos humanos.


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:mortar_board:Actividad](../DEMContour/Readme.md): Modelo digital de elevación - DEM a partir de curvas de nivel.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Creación de mapa de pendientes clasificadas

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _DEMSlope_ y establezca el CRS 9377. Agregue al mapa el modelo digital de elevación Copernicus disponible en la ruta `\file\dem\Copernicus\Copernicus30m.tif` y las capas `Mpio25899_MOT2013`, `Mpio25899_DiviPol` y `MOT` desde la base de datos geográfica `\file\gdb\SIGE.gdb`, simbolice el DEM por sombreado de relieve o _Shaded Relief_ y ajuste la simbología de los polígonos utilizando diferentes colores de contorno y sin relleno.  

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Utilizando la herramienta de geo-procesamiento _Spatial Analysis Tools / Fill_, rellene los sumideros del modelo digital de elevación Copernicus, guarde como `\file\dem\Copernicus\Copernicus30m_Fill.tif` y simbolice a partir por sombreado de relieve.

<div align="center"><img src="graph/ArcGISPro_Fill1.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Utilizando la herramienta de geo-procesamiento _Spatial Analysis Tools / Slope_, cree en mapa de pendientes de terreno en tasa porcentual, guarde como `\file\dem\Copernicus\Copernicus30m_Fill_Slope.tif`. Podrá observar que automáticamente se crea una visualización clasificada con diferentes rangos que representan la pendiente.

<div align="center"><img src="graph/ArcGISPro_Slope1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Utilizando la herramienta de geo-procesamiento _Spatial Analysis Tools / Reclassify_, reclasifique el mapa de pendientes en las siguientes 9 clases definidas en el dominio `Dom_PenSuelo` del diccionario de datos del ANLA utilizado para la presentación de estudios ambientales en Colombia, guarde como `\file\dem\Copernicus\Copernicus30m_Fill_Slope_Reclass.tif` y ajuste la simbología a valores únicos utilizando la paleta _Brown Light to Dark_.

<div align="center">

| Código | Descripción                                      | Rango        |
|:------:|:-------------------------------------------------|:-------------|
|  6010  | A nivel                                          | 0-1% (a)     |
|  6020  | Ligeramente plana                                | 1-3% (a)     |
|  6030  | Ligeramente inclinada                            | 3-7% (b)     |
|  6040  | Moderadamente inclinada                          | 7-12% (c)    |
|  6050  | Fuertemente inclinada                            | 12-25% (d)   |
|  6060  | Ligeramente escarpada o ligeramente empinada     | 25-50% (e)   |
|  6070  | Moderadamente escarpada o moderadamente empinada | 50-75% (f)   |
|  6080  | Fuertemente escarpada o fuertemente empinada     | 75-100% (g)  |
|  6090  | Totalmente escarpada                             | >100% (g)    |

</div>

<div align="center"><img src="graph/ArcGISPro_Reclassify1.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Análisis general de pendiente municipal




## 3. Análisis de pendiente por división geopolítica municipal



## 4. Análisis de pendiente por categoría de suelo e identificación de incompatibilidades




## 5. Análisis usando software libre - QGIS

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
| Avance **P5** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P5** | :compass:Mapa digital impreso _P3-1: xxxx_<br>Incluir xxxxx. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                          | 
| Avance **P5** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

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

| [:arrow_backward: Anterior](../DEMSatellite/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|------------------------------------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 