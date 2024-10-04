# ArcGIS Pro - Análisis de amenazas naturales
Keywords: `hazard` `landslide` `seismic` `volcanic` `tsunami` `mass-move` `erosion`

A partir de los conceptos aprendidos en este curso, desarrollaremos un procedimiento que permita generar el mapa de amenazas de Colombia. Utilizando el mapa de amenazas obtenido y mediante un recorte hasta la zona límite del Modelo de Ocupación Territorial - MOT de la zona de estudio, determinar el riesgo ponderado en función de las áreas de cada clase.                           

<div align="center"><img src="graph/Hazard.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Identificar y descargar mapas de amenazas naturales.
* Para las clases contenidas en cada, asignar pesos en función del tipo de amenaza.
* Mediante unión geográfica, combinar y obtener sub-polígonos calculando el valor total de la amenaza.
* Reclasificar los valores obtenidos en diferentes categorías.
* Obtener el riesgo ponderado dentro del límite geográfico del área de estudio.


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Capas requeridas y pesos

Para la creación del mapa general de amenazas naturales de Colombia, utilizaremos los mapas listados en la siguiente tabla, los cuales han sido obtenidos, ajustados o generados a partir de diferentes fuentes de información pública.

> Tenga en cuenta que los pesos establecidos, pueden no corresponder a los valores de referencia utilizados por las entidades gubernamentales que gestionan los riesgos naturales en Colombia, y que estos valores han sido definidos solamente para ejemplificar esta actividad académica. 

<div align="center">

| Mapa / Capa                                                                  | Descripción                                                                                   |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| SusceptibilidadDeslizamientos2010.shp<br><sub>\file\data\IDEAM\ </sub>       | Mapa de susceptibilidad a deslizamientos escala 1:500K - IDEAM - 2010                         |
| SusceptibilidadInundacion.shp<br><sub>\file\data\IDEAM\ </sub>               | Mapa de susceptibilidad por inundación debidas a lluvias - IDEAM                              |
| AmenazaVolcanicaZonasMax.shp<br><sub>\file\data\SGC\AmenazaVolcanica\ </sub> | Mapa de amenazas volcánicas - SGC                                                             |
| ZonaAmenazaNSR10.shp<br><sub>\file\data\SGC\ </sub>                          | Zonas amenaza Sísmica NSR-10 - SGC                                                            |
| SuscMM_500kReclass.shp<br><sub>\file\data\SGC\ </sub>                        | Mapa de susceptibilidad por movimientos en masa debidos eventos sísmicos - SGC                |
| TsunamiCota3menos.shp<br><sub>\file\data\rcfdtools\ </sub>                   | Zonas con amenazas de inundación por tsunamí debidas a ondas inducidas por sismos - rcfdtools |
| Erosion1988.shp<br><sub>\file\data\IDEAM\ </sub>                             | Zonas erosionables IDEAM - 1988                                                               |

</div>


### 1.1. Mapa de susceptibilidad a deslizamientos - IDEAM - 2010

Este mapa del Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM de Colombia, contiene información geográfica que corresponde a la información indicativa tipo raster de la susceptibilidad del terreno a los movimientos en masa, generado a partir de información primaria de geomorfología, geología, suelos y cobertura de la tierra, a escala 1:500.000 (obtenido a partir de mapa por servicio de https://www.colombiaenmapas.gov.co).

<div align="center">Pesos (SusceptibilidadDeslizamientos2010.shp)<br>

| LandSlid     |   LandSRGB    | WLandSlid<br><sub>(peso)</sub> |
|:-------------|:-------------:|:------------------------------:|
| 0 - Nula     | (225,225,225) |               0                |
| 1 - Muy Baja |  (56,168,0)   |               0                |
| 2 - Baja     |  (139,209,0)  |               1                |
| 3 - Media    |  (255,255,0)  |               5                |
| 4 - Alta     |  (255,128,0)  |              7.5               |
| 5 - Muy Alta |   (255,0,0)   |               10               |

</div><br>

> El mapa original de susceptibilidad a deslizamientos - IDEAM ha sido convertido a polígonos multiparte.

<div align="center"><img src="graph/ArcGISPro_WLandSlid.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.2. Mapa de susceptibilidad por inundación debida a lluvia - IDEAM

Este mapa del Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM de Colombia, contiene información geográfica que corresponde a las zonas susceptibles a inundación, a escala 1:500.000 (obtenido a partir de mapa por servicio de https://www.colombiaenmapas.gov.co) combinada con las zonas inundadas por eventos extremos generados por el fenómeno de la Niña en los años 1988, 2000, 2011, 2012.

<div align="center">Pesos (SusceptibilidadInundacion.shp)<br>

| Inundat        | WInundat<br><sub>(peso)</sub> |
|:---------------|:-----------------------------:|
| 1 - Inundación |               5               |

</div><br>

<div align="center"><img src="graph/ArcGISPro_WInundat_Merge.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_WInundat.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.3. Mapa de amenazas volcánicas - SGC

Este mapa del Servicio Geológico Colombiano - SGC, contiene la zonificación de áreas vulnerables que pueden resultar afectadas en caso de la posible erupción de un volcán, y sirve de herramienta fundamental para la planificación en prevención de desastres, en ordenamiento territorial y en planes de inversión. Elaborado el 01-01-2017 (obtenido a partir de servicio rest de https://www.colombiaenmapas.gov.co).

<div align="center">Pesos (AmenazaVolcanicaZonasMax.shp)<br>

| Volcanic |  VolcanRGB   | WVolcanic<br><sub>(peso)</sub> |
|:---------|:------------:|:------------------------------:|
| Baja     | (255,255,0)  |               1                |
| Media    | (255,128,0)  |               5                |
| Alta     |  (255,0,0)   |               10               |

</div><br>

Utilizando la herramienta _Analysis Tools / Union_ se han unido los polígonos de cada volcán o nevado contenido en _AmenazaVolcanicaZonas.shp_ y se ha definido como valor final del peso en cada fracción, el mayor peso encontrado (para ejecutar este procedimiento, primero se deben crear capas independientes para cada nevado o volcán). 

<div align="center"><img src="graph/ArcGISPro_WVolcanic_Union.png" alt="R.SIGE" width="100%" border="0" /></div>

Script en Python para obtención de mayor peso   
```
def WVolcMax(WVolList):
    return max(WVolList)
```

Llamado de función a través de una lista de campos   
```
WVolcMax((!WVolcanic!,!WVolcanic_!,!WVolcanic1!,!WVolcani_1!,!WVolcani_2!,!WVolcani_3!,!WVolcani_4!,!WVolcani_5!,!WVolcani_6!,!WVolcani_7!,!WVolcani_8!,!WVolcani_9!,!WVolcan_10!,!WVolcan_11!))
```

> Los valores de los campos de atributos incluídos en la lista de entrada corresponden a los nombres asignados por la herramienta _Analysys Tools / Union_ a partir de las diferentes combinaciones de las intersecciones encontradas.

<div align="center"><img src="graph/ArcGISPro_WVolcanic_Python.png" alt="R.SIGE" width="100%" border="0" /></div>

<div align="center">Mapa de pesos WVolcanic<br><img src="graph/ArcGISPro_WVolcanicMax.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.4. Zonas amenaza Sísmica NSR-10 - SGC

Zonificación y parámetros para el diseño sismo resistente según el Reglamento NSR-10. La NSR-10 es el Reglamento Colombiano de Construcción Sismo Resistente, que regula las condiciones con las que deben contar las construcciones con el fin de que la respuesta estructural a un sismo sea favorable y pretende evitar que los movimientos sísmicos ocasionen derrumbes o daños a las edificaciones e igualmente preservar la integridad física y los bienes de las personas (obtenido a partir de servicio rest de https://srvags.sgc.gov.co).

<div align="center">Pesos (ZonaAmenazaNSR10.shp)<br>

| SeismicID |  Seismic   | SeismicRGB  | WSeismic<br><sub>(peso)</sub>  |
|:---------:|:----------:|:-----------:|:------------------------------:|
|     3     |    Baja    | (56,168,0)  |               0                |
|     2     | Intermedia | (255,255,0) |               5                |
|     1     |    Alta    |  (255,0,0)  |               10               |

</div><br>

<div align="center"><img src="graph/ArcGISPro_WSeismic.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.5. Mapa de susceptibilidad por movimientos en masa debidos eventos sísmicos - SGC

Este mapa creado por el Servicio Geológico Colombiano - SGC, contiene la zonificación de zonas susceptibles a movivientos en masa debidas a la ocurrencia de eventos sísmicos (obtenido a partir de servicio rest de https://srvags.sgc.gov.co).

<div align="center">Pesos (SuscMM_500kReclass.shp)<br>

| MassMove     |   MassMRGB   | WMassMove<br><sub>(peso)</sub> |
|:-------------|:------------:|:------------------------------:|
| 1 - Muy Baja |  (56,168,0)  |               0                |
| 2 - Baja     | (139,209,0)  |               1                |
| 3 - Media    | (255,255,0)  |               5                |
| 4 - Alta     | (255,128,0)  |              7.5               |
| 5 - Muy Alta |  (255,0,0)   |               10               |

</div><br>

> Para simplificar el análisis presentado en esta actividad, el mapa original de susceptibilidad por movimientos en masa debidos eventos sísmicos - SGC a escala 1:100K ha sido reescalado por vecinos naturales a celdas de 250 metros y convertido a polígonos multiparte.

<div align="center"><img src="graph/ArcGISPro_WMassMove.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.6. Zonas con amenazas de inundación por tsunamí debidas a olas inducidas por sismos - rcfdtools

A partir del modelo digital de elevación SRTM de la NASA con cobertura sobre Colombia (\file\data\NASA\SRTM\sa_con_3s.tif) se han creado los polígonos de zonas costeras amenazadas por Tsunamis con elevaciones inferiores o iguales a 3 metros, correspondientes a amenazas de nivel 3. En la delimitación de la zona de afectación, se han mantenido los corredores de los cauces principales cuya cota no supera el valor límite establecido; lo anterior debido a que los efectos de la onda cinemática y la condición de control en la descarga al pacífico, puede generar sobre elevaciones en los cauces e inundaciones. 

<div align="center">Pesos (TsunamiCota3menos.shp)<br>

| TsunamiAmp | Tsunami   | WTsunamRGB  | WTsunami<br><sub>(peso)</sub> |
|:----------:|:----------|:-----------:|:-----------------------------:|
|    0.3     | Baja      | (139,209,0) |               0               |
|     1      | Media     | (255,255,0) |               1               |
|     3      | Alta      | (255,128,0) |               5               |
|     5      | Extrema   |  (255,0,0)  |              7.5              |
|     10     | Severa    |  (168,0,0)  |              10               |

</div><br>

<div align="center"><img src="graph/ArcGISPro_WTsunami.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.7. Zonas erosionables IDEAM - 1988

El mapa de Erosión y degradaciÓn de las Tierras Colombianas (IGAC, 1988) a escala 3.400.000 fue elaborado por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi y publicado en 1988, en el Atlas de Suelos y Bosques de Colombia. Se presentan estadísticas de áreas afectadas y porcentajes sobre cada una de las cinco regiones naturales continentales de Colombia. En la memoria se hace alusión a la degradación de las tierras según la FAO (1980) y a la erosión de los suelos. En la leyenda del mapa, se utilizan seis clases, con base en parámetros selectivos y evidencias de campo.
Este producto es generado por la Subdirección de Agrología del Instituto Geográfico Agustín Codazzi - IGAC, para el territorio nacional, el cual fue publicado en la obra Suelos y Tierras de Colombia 2016. Elaborado el 09-12-2022 a escala 1:3.400.000 (obtenido a partir de servicio rest de https://www.colombiaenmapas.gov.co).

<div align="center">Pesos (Erosion1988.shp)<br>

| Erosion                 |   LandSRGB    | WErosion<br><sub>(peso)</sub> |
|:------------------------|:-------------:|:-----------------------------:|
| 0 - Sin Erosión         | (225,225,225) |               0               |
| 1 - Erosion muy ligera  |  (56,168,0)   |               0               |
| 2 - Erosion ligera      |  (139,209,0)  |               1               |
| 3 - Erosion moderada    |  (255,255,0)  |              2.5              |
| 4 - Erosion severa      |  (255,128,0)  |               5               |
| 5 - Erosion muy severa  |   (255,0,0)   |              10               |

</div><br>

<div align="center"><img src="graph/ArcGISPro_WErosion.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Análisis de amenazas

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _Hazard_ y establezca el CRS 9377. Agregue al mapa las diferentes capas indicadas en el numeral 1, ajuste la simbología a los valores RGB establecidos y establezca transparencias en 50%.

<div align="center"><img src="graph/ArcGISPro_AddLayer.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Utilizando la herramienta de geoprocesamiento _Analysis Tools / Union_, cree la unión e intersección espacial de las 7 capas de amenazas evaluadas, nombre como _\file\shp\Hazard.shp_. Podrá observar que hemos obtenido 425869 sub polígonos.

<div align="center"><img src="graph/ArcGISPro_Union1.png" alt="R.SIGE" width="100%" border="0" /></div>

3. En la capa resultante, agregue un campo numérico doble con el nombre `Hazard` y utilizando la siguiente expresión realice la suma de los diferentes pesos establecidos por variable. Simbolice por colores graduados en 6 clases por cortes naturales a partir del campo `Hazard` y obtenga una estadística visual del conjunto de datos.

`Hazard = !WLandSlid! + !WInundat! + !WVolcanic! + !WMassMove! + !WTsunami! + !WErosion!`

<div align="center"><img src="graph/ArcGISPro_FieldCalculator1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. En un campo de texto nuevo nombrado como `HazardCls` y utilizando el calculador de campo y un script en Python, reclasifique los valores obtenidos en las siguientes 6 clases a partir de los valores de corte o _Boundary_ indicados. Simbolice a partir de la marcación de clases.

<div align="center">

| Boundary  | HazardCls                 | Color RGB     | 
|:---------:|---------------------------|---------------|
|     5     | 1 - Very low hazard       | (62,128,79)   | 
|    10     | 2 - Low hazard            | (142,252,61)  | 
|    15     | 3 - Moderately low hazard | (254,254,65)  | 
|    20     | 4 - Moderate hazard       | (237,164,102) | 
|    25     | 5 - High hazard           | (246,135,36)  | 
|    100    | 6 - Very high hazard      | (255,0,0)   | 

</div>

Script en Python:  
```
hazardLevel = [[5, '1 - Very low hazard'],
                   [10, '2 - Low hazard'],
                   [15, '3 - Moderately low hazard'],
                   [20, '4 - Moderate hazard'],
                   [25, '5 - High hazard'],
                   [100, '6 - Very high hazard']]

def hazardcls(elevation):
  for i in hazardLevel:
    if elevation <= i[0]:
      return i[1]
```

Llamado de función:  
`hazardcls(!Hazard!)`

<div align="center"><img src="graph/ArcGISPro_FieldCalculator2.png" alt="R.SIGE" width="100%" border="0" /></div>

5. En un campo de atributos numérico doble nombrado como `APkm2`, calcule el área planar en km² de cada fracción. A través de un resúmen estadístico o _Summarize_, obtenga el total de áreas por clase de amenaza de Colombia. Cree un gráfico de análisis.  

<div align="center"><img src="graph/ArcGISPro_Summarize1.png" alt="R.SIGE" width="100%" border="0" /></div>

Imágenes complementarias  
<div align="center"><img src="graph/ArcGISPro_Hazard1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Hazard2.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Hazard3.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Hazard4.png" alt="R.SIGE" width="100%" border="0" /></div>


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

* [Tsunami Coastal Assessment Tool (TsuCAT)](https://sift.pmel.noaa.gov/ComMIT/TsuCAT/software/)
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