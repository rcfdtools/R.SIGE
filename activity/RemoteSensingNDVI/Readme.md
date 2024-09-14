# Índices de vegetación: NDVI, SAVI, MSAVI, TSAVI, NBR
Keywords: `normalized-difference-vegetation-index` 

Utilizando las imágenes satelitales obtenidas en este módulo, crear con algebra de mapas o con Imagery / Indices, mapas de diferencias normalizadas de vegetación [NDVI](https://pro.arcgis.com/es/pro-app/latest/help/analysis/raster-functions/ndvi-function.htm). Recortar hasta el límite municipal obtenido con la envolvente del MOT, reclasificar las vegetaciones en 4 clases (definidas manualmente con cortes en 0.1, 0.23, 0.35 y 1 o hasta el valor máximo). A partir del número de celdas obtenidas en cada clase, calcule áreas y realice un análisis comparativo entre los datos obtenidos entre dos instantes de tiempo, explique las diferencias encontradas. Compare los mapas de vegetación obtenidos con el mapa de usos potenciales del suelo del IGAC evaluado en el módulo 4, explique si existe alguna correspondencia en sus límites internos. Cree mapas para índices complementarios. Uso y aplicabilidad de mapas de índices en estudios de ordenamiento territorial.

<div align="center"><img src="graph/RemoteSensingNDVI.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Obtener y evaluar coberturas de vegetación a partir del cálculo de índices.
* Evaluar y comparar coberturas con mapas de usos.


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Cálculo manual del índice NDVI

El método Índice diferencial de vegetación normalizado (NDVI, por sus siglas en inglés) es un índice normalizado que permite generar una imagen que muestra el verdor (la biomasa relativa). Este índice aprovecha el contraste de las características de dos bandas de un dataset ráster multiespectral: las absorciones de pigmento de clorofila en la banda roja y la alta reflectividad de los materiales de las plantas en la banda NIR.[^1]

La ecuación del NDVI documentada y predeterminada es la siguiente:

`NDVI = ((NIR - Red)/(NIR + Red))`

* NIR = valores de píxel de la banda infrarroja cercana
* Rojo = valores de píxel de la banda roja

Este índice coloca los valores entre -1,0 y 1,0. [^2]

Utilizando las imágenes satelitales obtenidas en la primera actividad de este módulo realizar el siguiente procedimiento.

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _RemoteSensingNDVI_ y establezca el CRS 9377. Agregue al mapa la capa del límite municipal obtenido Modelo de Ocupación Territorial - MOT disponible en la información recopilada del POT en la ruta `\file\gdb\SIGE.gdb\SIGE\Mpio25899_MOT2013` ajuste la simbología solo a contorno y agregue de Landsat 7 las bandas B4 y B3, para Landsat 9 agregue las bandas B5 y B4.

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Utilizando la herramienta de geo-procesamiento _Image Analyst Tools / Raster Calculator_, calcule los mapas de índices para Landsat 7 y Landsat 9, utilice las siguientes expresiones y nombres de archivo:

* `\file\grid\LE07_L2SP\L720030111NVDI.tif`: expresión de algebra de mapas `(B4 - B3) / (B4 + B3)`
* `\file\grid\LC09_L2SP\L920230219NVDI.tif`: expresión de algebra de mapas `(B5 - B4) / (B5 + B4)`

> En las expresiones, reemplace B3, B4, B5 por los nombres de las imágenes y bandas correspondientes.

Para Landsat 7 podrá observar que se han obtenido valores entre -0.495 y 0.595  
<div align="center"><img src="graph/ArcGISPro_RasterCalculator1.png" alt="R.SIGE" width="100%" border="0" /></div>

Para Landsat 9 podrá observar que se han obtenido valores entre -0.228 y 0.998
<div align="center"><img src="graph/ArcGISPro_RasterCalculator2.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Utilizando la herramienta de geo-procesamiento _Data Management Tools / Clip Raster_, recorte las grilla NDVI hasta el límite municipal del MOT, nombre como `\file\grid\LE07_L2SP\L720030111NVDIClip.tif` y `\file\grid\LC09_L2SP\L920230219NVDIClip.tif`.

<div align="center"><img src="graph/ArcGISPro_ClipRaster1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_ClipRaster2.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Utilizando la herramienta de geo-procesamiento _Spatial Analyst Tools / Reclassify_, reclasifique los mapas obtenidos en las siguientes clases, guarde como `\file\grid\LE07_L2SP\L720030111NVDIClipReclass.tif` y `\file\grid\LC09_L2SP\L920230219NVDIClipReclass.tif`, rotule y simbolice con los colores RGB indicados:

<div align="center">

| Corte | Label                                 | RGB         |
|-------|---------------------------------------|-------------|
| 0.10  | 1 - Sin Vegetación - Urbano o Desnudo | 255,255,190 |
| 0.23  | 2 - Bosque Mixto                      | 85,255,0    |
| 0.35  | 3 - Bosque Denso                      | 112,168,0   |
| 1.00  | 4 - Bosque Muy Denso                  | 38,115,0    |

</div>

<div align="center"><img src="graph/ArcGISPro_Reclassify1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Reclassify2.png" alt="R.SIGE" width="100%" border="0" /></div>

> Tenga en cuenta que los cuerpos de agua, zonas húmedas y zonas urbanas serán clasificadas en la clase 1 - Sin Vegetación - Urbano o Desnudo

5. En la tabla de atributos de las grillas de reclasificación, agregue un campo numérico doble para el cálculo del área en hectáreas a partir del número de celdas (Count * 30 * 30 /10000), nombre como `APha` y un campo de texto para el rótulo con el nombre `Label`.

<div align="center"><img src="graph/ArcGISPro_FieldCalculator1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_FieldCalculator2.png" alt="R.SIGE" width="100%" border="0" /></div>

6. Desde la tabla de contenido y para cada mapa, cree gráficas de barras y evalúe la distribución de las áreas obtenidas. Podrá observar que la clase 1 correspondiente a sin vegetación, urbano o desnudo a aumentado de 375.84 hectáreas a 463.23 hectáreas y que la distribución de bosques ha cambiado en el tiempo.

<div align="center"><img src="graph/ArcGISPro_Chart1.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Cálculo automático del índice NDVI

1. Utilizando la herramienta de geo-procesamiento _Data Management Tools / Composite Bands_, cree una composición de las bandas disponibles en Landsat 7, asegúrese de ingresar las bandas en el orden de secuencia B1 a B7. Guarde la composición como `\file\grid\LE07_L2SP\LE07_L2SP_Composite.TIF`. 

<div align="center"><img src="graph/ArcGISPro_CompositeBands1.png" alt="R.SIGE" width="100%" border="0" /></div>

En la simbología, ajuste el orden de secuencia a `Band_3`, `Band_2` y `Band_1` y en el menú superior active las opciones de visualización de rango dinámico _DRA_. 

<div align="center"><img src="graph/ArcGISPro_Symbology1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. En la tabla de contenido, seleccione la composición `LE07_L2SP_Composite.TIF` y en el menú _Imagery_ seleccione la opción _Tools / Indices_, automáticamente será calculado este índice y será agregada al mapa la capa `NDVI_LE07_L2SP_Composite.TIF`. 

<div align="center"><img src="graph/ArcGISPro_IndicesNDVI1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_IndicesNDVI2.png" alt="R.SIGE" width="100%" border="0" /></div>


## 3. Cálculo de otros índices [^1]

Como observo en las opciones de _Imagery / Tools / Indices_, ArcGIS Pro permite el cálculo automático de los siguientes índices complementarios:


### 3.1. Vegetación y suelos


#### 3.1.1. SAVI

El método Índice de vegetación ajustado al suelo (SAVI, por sus siglas en inglés) es un índice de vegetación que intenta minimizar las influencias del brillo del suelo utilizando un factor de corrección de brillo del suelo. Esto con frecuencia se utiliza en regiones áridas en donde la cubierta de vegetación es baja y genera valores entre -1,0 y 1,0.

`SAVI = ((NIR - Rojo) / (NIR + Rojo + L)) x (1 + L)`

* NIR = valores de píxel de la banda infrarroja cercana
* Rojo = valores de píxel de la banda roja cercana
* L = cantidad de cobertura de vegetación verde

Si usa una lista delimitada por espacios, identificará las bandas NIR y roja e introducirá el valor L en el siguiente orden: NIR Roja L. Por ejemplo, 4 3 0,5.

> Referencia: Huete, A. R., 1988, "A soil-adjusted vegetation index (SAVI)," Remote Sensing of Environment, Vol. 25, 295–309.


#### 3.1.2. MSAVI

El método Índice de vegetación ajustada de suelo modificado (MSAVI2) minimiza el efecto del terreno desnudo en el SAVI.

`MSAVI2 = (1/2)*(2(NIR+1)-sqrt((2*NIR+1)2-8(NIR-Rojo)))`

* NIR = valores de píxel de la banda infrarroja cercana
* Rojo = valores de píxel de la banda roja

> Referencia: Qi, J. et al., 1994, "A modified soil vegetation adjusted index," Remote Sensing of Environment, Vol. 48, n.º 2, 119–126.


#### 3.1.3. TSAVI

El método Índice de vegetación ajustado de suelo transformado (TSAVI, por sus siglas en inglés) es un índice de vegetación que minimiza las influencias de brillo del suelo al asumir que la línea del suelo tiene una intercepción y pendiente arbitraria.

`TSAVI = (s * (NIR - s * Rojo - a)) / (a * NIR + Rojo - a * s + X * (1 + s2))`

* NIR = valores de píxel de la banda infrarroja cercana
* Rojo = valores de píxel de la banda roja
* s = la pendiente de la línea del suelo
* a = la intercepción de la línea del suelo
* X = un factor de ajuste que se establece para minimizar el ruido del suelo

> Referencia: Baret, F. y G. Guyot, 1991, "Potentials and limits of vegetation indices for LAI and APAR assessment," Remote Sensing of Environment, Vol. 35, 161–173.


#### 3.1.4. PVI

El método Índice de vegetación perpendicular (PVI, por sus siglas en inglés) es similar a un índice diferencial de vegetación; sin embargo, es sensible a las variaciones atmosféricas. Al utilizar este método para comparar imágenes, solo se debe utilizar en imágenes que se han corregido atmosféricamente.

`PVI = (NIR - a*Rojo - b) / (sqrt(1 + a2))`

* NIR = valores de píxel de la banda infrarroja cercana
* Rojo = valores de píxel de la banda roja
* a = pendiente de la línea de suelo
* b = gradiente de la línea del suelo

Este índice coloca los valores entre -1,0 y 1,0.


#### 3.1.5. VARI

El Índice de resistencia atmosféricamente visible (VARI) está diseñado para resaltar la vegetación en la parte visible del espectro, a la vez que mitiga las diferencias en la iluminación y los efectos atmosféricos. Resulta idóneo para las imágenes RGB o en color; utiliza las tres bandas de color.

`VARI = (Green - Red) / (Green + Red - Blue)`

* Verde = valores de píxel de la banda verde
* Rojo = valores de píxel de la banda roja
* Azul = valores de píxel de la banda azul

> Referencia: Gitelson, A., et al. "Vegetation and Soil Lines in Visible Spectral Space: A Concept and Technique for Remote Estimation of Vegetation Fraction." International Journal of Remote Sensing 23 (2002): 2537−2562.


### 3.2. Agua





### 3.3. Geología


### 3.4. Paisaje







## 4. Análisis usando software libre - QGIS

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
| Avance **P6** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P6** | :compass:Mapa digital impreso _P6-1: xxxx_<br>Incluir xxxxx. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                          | 
| Avance **P6** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* https://pro.arcgis.com/es/pro-app/latest/help/data/imagery/indices-gallery.htm


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../xxxx) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|---------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: https://pro.arcgis.com/es/pro-app/latest/help/data/imagery/indices-gallery.htm
[^2]: https://pro.arcgis.com/es/pro-app/latest/help/analysis/raster-functions/ndvi-function.htm