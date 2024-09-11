# Delimitación de cuencas hidrográficas locales
Keywords: `basin` `basin-limit`

A partir del modelo digital de elevación ESA Copernicus, cree el mapa de relleno de sumideros FIL. Reacondicione el modelo de terreno FIL como RawDEM, utilizando la red hidrográfica del POT (completar drenajes y abrir bucles). A partir del RawDEM, cree el mapa de direcciones de flujo FDR. Con la grilla FDR, cree el mapa de acumulación de flujo FAC. Con la grilla FAC, defina los drenajes con áreas de aportación de 1 km² creando un mapa binarizado. Cree una capa de puntos y a partir de la red de drenaje y del modelo digital de elevación, identifique al menos 3 puntos de control para delimitación de cuencas principales. A partir de los 3 puntos de control y utilizando el mapa FDR, delimite las 3 cuencas hidrográficas, convierta a vectores y analice las áreas obtenidas.

<div align="center"><img src="graph/AddedValue.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Generar el mapa de direcciones y acumulaciones de flujo.
* Delimitar cuencas hidrográficas a partir de puntos de estudio 


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:mortar_board:Actividad](../DEMSatellite/Readme.md): Modelo digital de elevación - DEM a partir de sensores remotos satelitales.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:toolbox:Herramienta](https://www.hec.usace.army.mil/software/hec-hms/): HEC-HMS 4.12 o superior.


## 1. Edición de red de drenaje en ArcGIS Pro

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _BasinLimit_ y establezca el CRS 9377. Agregue al mapa el modelo digital de elevación Copernicus desde `\file\dem\Copernicus\Copernicus30m.tif`, el límite del modelo de ocupación territorial `\file\gdb\SIGE\Mpio25899_MOT2013` la red de drenaje utilizada en la formulación del POT disponible en `\file\gdb\SIGE.gdb\POT2013Formulacion\HIDROGRAFIA1` y el eje del tramo ajustado del Río Frío evaluado en la actividad anterior que se encuentra en [\file\gdb\SIGE.gdb\SIGE\LineaPerfil]().  

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Modifique y complete la red de drenaje incluyendo el tramo principal del Río Frío y elimine zonas con bucles. Para ello cree una copia de la capa _HIDROGRAFIA1_ guarde como `\file\gdb\SIGE.gdb\SIGE\Mpio25899_Drenaje` y utilice el editor de ArcGIS Pro. Digitalice al menos 1 kilómetro adicional aguas abajo del Río Frío.

<div align="center"><img src="graph/ArcGISPro_Edit1.png" alt="R.SIGE" width="100%" border="0" /></div>

Ejemplo ajuste de bucles  
<div align="center"><img src="graph/ArcGISPro_Edit2.png" alt="R.SIGE" width="100%" border="0" /></div>

Ajuste y extensión zona baja Río Frío  
<div align="center"><img src="graph/ArcGISPro_Edit3.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Delimitación de cuencas en HEC-HMS


1. En HEC-HMS, cree un proyecto nuevo en blanco definiendo _Metric_ en el sistema de unidades por defecto, guardar como _HECHMS_ en la carpeta D:\R.LTWB\.

<div align="center"><img src="graph/HECHMS_CreateNewProject.png" alt="R.SIGE" width="100%" border="0" /></div>

Automáticamente, obtendrá una carpeta con la estructura de directorios y archivos requeridos por este modelo, que para la versión 4.9 contendrá:

<div align="center"><img src="graph/HECHMS_CreateNewProjectStructure.png" alt="R.SIGE" width="100%" border="0" /></div>

Dentro de la carpeta de proyecto cree un nuevo folder con el nombre _projectionfile_ y copie dentro cualquier archivo de proyección de los archivos de forma shapefile generados en la carpeta `\file\shp` que cotenga los parámetros del CRS 9377 , por ejemplo, el archivo .prj de la capa _Predio.shp_. 

2. En el menú _Components – Create Component – Basin Model_, cree 1 modelo de cuenca y nómbrelo como _RioFrio_.

> Evite utilizar caracteres especiales diferentes a los utilizados en el idioma inglés, tales como eñes y tildes.

<div align="center"><img src="graph/HECHMS_CreateBasinModel.png" alt="R.SIGE" width="100%" border="0" /></div>

3. En la tabla de contenido localizada a la izquierda, seleccione _HECHMS – Basin Models – RioFrio_, luego en el menú _GIS – Coordinate System_ seleccione el sistema de proyección de coordenadas _MAGNA_OrigenNacional.prj_ localizado en el directorio _D:\R.LTWB\\.ProjectionFile_. Repita este procedimiento para los demás modelos de cuenca.

<div align="center"><img src="graph/HECHMS_CoordinateSystem.png" alt="R.SIGE" width="100%" border="0" /></div>

4. En el menú _Components – Create Component – Terrain Data_, cree los terrenos a partir de los modelos digitales de elevación - DEM recortados anteriormente hasta el límite de la zona de estudio localizados en las carpetas _D:\R.LTWB\\.dem\ASTER_, _D:\R.LTWB\\.dem\SRTM_ y _D:\R.LTWB\\.dem\ALOS_, seleccionando unidades verticales en metros, nombrar como _TerrainASTER_, _TerrainSRTM_ y _TerrainALOS_.

![R.LTWB](Screenshot/HECHMS4.9TerrainData1.png)

![R.LTWB](Screenshot/HECHMS4.9TerrainData2.png)

Automáticamente, los archivos _ASTGTMV003MosaicArcGISProZE.tif_, _SRTMV003MosaicArcGISProZE.tif_ y _APFBSRT1MosaicArcGISProZE.tif_ serán copiados con los nombres _TerrainASTER.elevation.tif_, _TerrainSRTM.elevation.tif_ y _TerrainALOS.elevation.tif_ en la carpeta _D:\R.LTWB\HECHMS\terrain_ y también en la carpeta _D:\R.LTWB\HECHMS\gis_ dentro de subcarpetas independientes.

![R.LTWB](Screenshot/HECHMS4.9TerrainData3.png)

![R.LTWB](Screenshot/HECHMS4.9TerrainData3a.png)

5. En la tabla de contenido, seleccione _HECHMS – Basin Models – BasinASTER_ y en la parte inferior asocie el terreno creado al modelo de cuencas. Repita este procedimiento para los modelos de elevación SRTM y ALOS.

> Este proceso puede tardar algunos segundos debido a la extensión del DEM y a su resolución.

![R.LTWB](Screenshot/HECHMS4.9TerrainData4.png)

6. En la tabla de contenido, seleccione _HECHMS – Basin Models – BasinASTER_ y en el menú _GIS_, seleccione la opción _Terrain Reconditioning_. El primer paso (Step 1) permite crear paredes perimetrales de confinamiento utilizando el borde de una cuenca previamente digitalizada, dar clic en _Next >_. 

> Para el caso de estudio no ejecutaremos la generación de paredes perimetrales a partir de la zona de estudio correspondiente a la zona hidrográfica 28 - Cesar, debido a que realizaremos el cálculo de los caudales medios de largo plazo sobre todo el modelo digital de elevación. 

![R.LTWB](Screenshot/HECHMS4.9TerrainReconditioningStep1.png)

El segundo paso (Step 2) permite modificar el terreno incrustando los drenajes, para ello seleccione la red de drenaje en formato Shapefile denominada _DrenajeSencilloIGAC100kZEMerge.shp_ localizada en _D:\R.LTWB\\.shp_, defina el número de celdas aferentes o _Smooth drop cell buffer_ (p. ej. 5), la profundidad de suavizado lateral o _Smooth drop height_ (p. ej. 10) y la profundidad de incrustación en el cauce o _Sharp drop height_ (p. ej. 1000 para garantizar que en el relleno de sumideros se mantenga la localización de las celdas correspondientes a los drenajes marcados), de clic en _Next >_. 

![R.LTWB](Screenshot/HECHMS4.9TerrainReconditioningStep2.png)

> Espere hasta que el proceso se complete, para la grilla de terreno _ASTGTMV003MosaicArcGISProZE.tif_ y la red _DrenajeSencilloIGAC100kZEMerge.shp_ este proceso en HEC-HMS requiere de aproximadamente 10 horas.

![R.LTWB](Screenshot/HECHMS4.9TerrainReconditioningStep3.png)

> Al igual que en la asociación y visualización en pantalla, este proceso puede tardar varios minutos debido a la extensión del DEM y a su resolución.

A través del monitor de procesos o _Processes_ del administrador de tareas o _Task Manager_ de su sistema operativo, verifique que se esté ejecutando el proceso _OpenJDK Platform binary_ de HEC-HMS. Este proceso requiere de mínimo 8GB de memoria RAM para modelos de terrenos como los utilizados en el caso de estudio.

![R.LTWB](Screenshot/Windows11TaskManagerProcesses.png)

Reacondicionamiento completado.
![R.LTWB](Screenshot/HECHMS4.9TerrainReconditioningStep4.png)

Grilla obtenida localizada en _D:\R.LTWB\HECHMS\gis\BasinASTER_
![R.LTWB](Screenshot/HECHMS4.9TerrainReconditioningStep5.png)

Opcional: repita el procedimiento anterior en HEC-HMS para los modelos de cuenca _BasinSRTM_ y _BasinALOS_. Los modelos de terreno serán almacenados en los directorios _\HECHMS\gis\BasinASTER_, _\HECHMS\gis\BasinSRTM_ y _\HECHMS\gis\BasinALOS_. 

> Debido a que los algoritmos y motor de cálculo del componente GIS de HEC-HMS requieren de varias horas para completar los procesos de reacondicionamiento en modelos digitales de elevación de gran tamaño, se recomienda realizar este procedimiento en _ArcGIS for Desktop_ a través de la herramienta _HEC-GeoHMS_ o desde _Arc Hydro Tools_ para ArcGIS.



1. Utilizando la herramienta de geo-procesamiento _Arc Hydro Tools Pro / DEM Reconditioning_, incruste en el modelo digital de elevación con relleno de sumideros la red de drenaje convertida a raster, guarde como `\file\dem\Copernicus\Copernicus30m_Fill_AgreeDEM.tif` 

<div align="center"><img src="graph/ArcGISPro_DEMReconditioning1.png" alt="R.SIGE" width="100%" border="0" /></div>



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

| [:arrow_backward: Anterior](../DEMProfile/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|----------------------------------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 