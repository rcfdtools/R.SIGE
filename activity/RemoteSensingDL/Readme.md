# Descarga de imágenes satelitales y composición de bandas
Keywords: `landsat` `remote-sensing` `composite-band` `clip-raster`

Utilizando una envolvente generada a partir de los polígonos del Modelo de Ocupación Territorial - MOT, descargue, componga y reproyecte al CRS 9733, imágenes y bandas satelitales de Landsat 7 y Lansat 9. Composiciones Landsat 7 B3B2B1 y Landsat 9 B4B3B2 para imágenes en falso color. Composiciones Landsat 7 B4B3B2 y Landsat 9 B5B4B3 para identificación de cuerpos de agua y vegetación. Análisis descriptivo de las diferencias encontradas entre los grupos de composiciones realizadas.

<div align="center"><img src="graph/RemoteSensingDL.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Descargar imágenes satelitales Landsat.
* Componer imágenes en falso color.
* Componer imágenes para identificar cuerpos de agua.


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:mortar_board:Actividad](../DEMSatellite/Readme.md): Modelo digital de elevación - DEM a partir de sensores remotos satelitales.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:man_technologist:Usuario](https://ers.cr.usgs.gov/): Creación de cuenta de usuario USGS.


## 0. Introducción general a sensores remotos y fotointerpretación [^1]

Los sensores remotos o Teledetección [^2] comprenden diversas técnicas para localización, captura y transmisión de datos de objetos y fenómenos a distancia, sin contacto físico con el elemento o fenómeno de interés. Algunas de sus aplicaciones más interesantes en la ingeniería civil y ambiental son: representación y análisis de modelos de terreno - elevación, elaboración de mapas de pendientes, composición de bandas de imágenes para la restitución masiva de cuerpos de agua, delimitación detallada de cuencas hidrográficas y morfometría, monitoreo de vegetación y evaluación de su calidad por medio de índices, monitoreo de contaminación atmosférica, seguir trayectoria de huracanes, medir fenómenos de remoción en masa, flujo por avalanchas, inundaciones y fenómenos de expansión urbana, entre otros.

### 0.1. Espectro electromagnético

Comprende el rango completo de longitudes de onda (frecuencias) por el que se extiende la radiación electromagnética.

<div align="center"><img src="graph/Graph_ElectromagneticSpectrum.png" alt="R.SIGE" width="90%" border="0" /><br><sub>Imagen tomada de learn.arcgis.com </sub></div>


### 0.2. Plataformas utilizadas en sensores remotos satelitales


#### 0.2.1. Landsat [^3]

Los Landsat son una serie de satélites construidos y puestos en órbita por Estados Unidos de América para la observación en alta resolución de la superficie terrestre. Los satélites Landsat orbitan alrededor de la Tierra en órbita circular heliosincrónica, a 705 km de altura, con una inclinación de 98.2º respecto del ecuador y un período de 99 minutos. La órbita de los satélites está diseñada de tal modo que cada vez que estos cruzan el ecuador de norte a sur lo hacen entre las 10:00 y las 10:15 de la mañana hora local. Los Landsat están equipados con instrumentos específicos para la teledetección multiespectral. El primer satélite Landsat (en principio denominado ERTS-1) fue lanzado el 23 de julio de 1972. Landsat 9 fue puesto en órbita el 27 de septiembre de 2021. La resolución de las imágenes capturadas es de 15 a 100 metros dependiendo de la banda espectral y el modo de captura. https://landsat.gsfc.nasa.gov/

<div align="center"><img src="graph/Graph_LandsatTimeLine.png" alt="R.SIGE" width="70%" border="0" /><br><sub>Imagen tomada de learn.arcgis.com </sub></div>

<div align="center"><br>Bandas y longitudes de onda

| Landsat 7<br>Banda                   | Landsat 7<br>Ancho (µm) | Landsat 7<br>Resolución (m) | Landsat 8/9<br>Banda                   | Landsat 8/9<br>Ancho (µm) | Landsat 8/9<br>Resolución (m) |
|--------------------------------------|:-----------------------:|:---------------------------:|----------------------------------------|:-------------------------:|:-----------------------------:|
|                                      |                         |                             | Band 1 Coastal Aerosol                 |        0.43 – 0.45        |              30               |
| Band 1 Blue                          |       0.45 – 0.52       |             30              | Band 2 Blue                            |        0.45 – 0.51        |              30               |
| Band 2 Green                         |       0.52 – 0.60       |             30              | Band 3 Green                           |        0.53 – 0.59        |              30               |
| Band 3 Red                           |       0.63 – 0.69       |             30              | Band 4 Red                             |        0.64 – 0.67        |              30               |
| Band 4 NIR<br>Near Infrared          |       0.77 – 0.90       |             30              | Band 5 NIR<br>Near Infrared            |        0.85 – 0.88        |              30               |
| Band 5 SWIR1<br>Shortwave Infrared 1 |       1.55 – 1.75       |             30              | Band 6 SWIR1<br>Shortwave Infrared 1   |        1.57 – 1.65        |              30               |
| Band 7 SWIR2<br>Shortwave Infrared 2 |       2.09 – 2.35       |             30              | Band 7 SWIR2<br>Shortwave Infrared 2   |        2.11 – 2.29        |              30               |
| Band 8 Panchromatic                  |       0.52 – 0.90       |             15              | Band 8 Panchromatic                    |        0.50 – 0.68        |              15               |
|                                      |                         |                             | Band 9 Cirrus [^7]                     |        1.36 – 1.38        |              30               |
| Band 6 TIR<br>Thermal Infrared       |      10.40 – 12.50      |            30/60            | Band 10 TIRS1 [^8]<br>Thermal Infrared |       10.6 – 11.19        |              100              |
|                                      |                         |                             | Band 11 TIRS2<br>Thermal Infrared      |       11.5 – 12.51        |              100              |

</div>


#### 0.2.2. SPOT [^4]

Los satélites Spot (Satellite Pour l’Observation de la Terre: Satélite Para la Observación de la Tierra) son una serie de satélites de teledetección civiles de observación del suelo terrestre que han sido desarrollado por el CNES (Centro Nacional de Estudios Espaciales francés) en colaboración con Bélgica y Suecia. La primera versión de SPOT fue lanzada el 22 de febrero de 1986 (Ariane 1). SPOT 7 fue lanzado el 30 de junio de 2014. La resolución de las imágenes capturadas es de 2.5 a 20 metros dependiendo de la banda espectral y el modo de captura. https://earth.esa.int/eogateway/missions/spot


#### 0.2.3. Sentinel [^5]

Sentinel es un proyecto multi-satélite que está siendo desarrollado por la ESA (European Space Agency) en el marco del Programa Copérnico. Las misiones Sentinel incluyen satélites de radar y satélites de imágenes super-espectrales para la vigilancia terrestre, oceánica y atmosférica de la Tierra. La primera versión fue lanzada el 3 de abril de 2014, la versión 6 que incluye radar altimétrico fue lanzada el 21 de noviembre de 2020. La resolución de las imágenes capturadas es de 5 a 300 metros dependiendo de la banda espectral, el modo de captura, y la polarización. https://www.esa.int/Applications/Observing_the_Earth/Copernicus/The_Sentinel_missions


#### 0.2.4. Ikonos [^6]

Los satélites comerciales Ikonos para la observación de la tierra, capturaban colecciones de imágenes multiespectrales y pancromáticas. La primera versión fue lanzada el 24 de septiembre de 1999 y la versión 2 fue lanzada en enero del 2000 y suspendida el 31 de marzo de 2016.  La resolución de las imágenes capturadas es de 1 a 4 metros dependiendo de la banda espectral y el modo de captura. https://www.esa.int/SPECIALS/Eduspace_ES/SEM776E3GXF_0.html


## 1. Descarga de imágenes desde earthexplorer.usgs.gov

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _RemoteSensing_ y establezca el CRS 9377. Agregue al mapa las capas `Mpio25899_MOT2013` y `Mpio25899_MOT2013_Envelope` disponibles en la ruta `\file\gdb\SIGE.gdb\SIGE` y represente por contornos.  

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Exporte la clase de entidad `Mpio25899_MOT2013_Envelope` a un archivo de formas shapefile en la ruta `\file\shp\Mpio25899_MOT2013_Envelope4329.shp` asignando el CRS 4326.

<div align="center"><img src="graph/ArcGISPro_ExportFeatures1.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Desde el directorio `\shp` comprima los archivos `Mpio25899_MOT2013_Envelope.shp`, `Mpio25899_MOT2013_Envelope.shx`, `Mpio25899_MOT2013_Envelope.dbf`, `Mpio25899_MOT2013_Envelope.prj` en un archivo `.zip` con el nombre `Mpio25899_MOT2013_Envelope.zip`.

<div align="center"><img src="graph/Windows_Zip1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Ingrese al portal https://earthexplorer.usgs.gov/ y en la parte superior derecha a través de la opción _Login_ ingrese con su cuenta de usuario del Servicio Geológico de los Estados Unidos de América - USGS.  

<div align="center"><img src="graph/Chrome_EarthExplorer1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Chrome_EarthExplorer2.png" alt="R.SIGE" width="100%" border="0" /></div>

5. En las opciones de _Search Criteria_, agregue el archivo comprimido que delimita la zona de estudio, podrá observar que la ventana de búsqueda muestra el límite espacial y las esquinas de la zona de búsqueda. En la parte inferior, ingrese la fecha (mm/dd/yyyy) 01/11/2003 debido a que inicialmente descargaremos imágenes Landsat 7 de esta fecha.

<div align="center"><img src="graph/Chrome_EarthExplorer3.png" alt="R.SIGE" width="100%" border="0" /></div>

6. En la pestaña _Data Sets_, busque y seleccione el conjunto de datos _Landsat 7 ETM+ C2 L2_

<div align="center"><img src="graph/Chrome_EarthExplorer4.png" alt="R.SIGE" width="100%" border="0" /></div>

7. En la pestaña _Additional Criteria_ busque la ruta o path 008 y la fila o row 056.

<div align="center"><img src="graph/Chrome_EarthExplorer5.png" alt="R.SIGE" width="100%" border="0" /></div>

8. Desde la pestaña de resultados, visualice la imagen `LE07_L2SP_008056_20030111_20200916_02_T1`, podrá observar que cubre un área más amplia y que en la zona de estudio se presentan pocas nubes.

<div align="center"><img src="graph/Chrome_EarthExplorer6.png" alt="R.SIGE" width="100%" border="0" /></div>

9. Utilizando la opción de descarga, obtenga las bandas de reflectancia y de emisión térmica, guarde como `\grid\LE07_L2SP\LE07_L2SP_008056_20030111_20200916_02_T1.tar`.

<div align="center"><img src="graph/Chrome_EarthExplorer7.png" alt="R.SIGE" width="100%" border="0" /></div>

10. Repita el procedimiento anterior y descargue imágenes Landsat 9 de la misma ruta o path 008 y fila o row 056 del 03 de febrero de 2023, guarde como `\grid\LC09_L2SP\LC09_L2SP_008056_20230203_20230311_02_T1.tar`.

<div align="center"><img src="graph/Chrome_EarthExplorer8.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Chrome_EarthExplorer9.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Composición de imágenes en falso color

1. Del comprimido `\grid\LE07_L2SP\LE07_L2SP_008056_20030111_20200916_02_T1.tar`, extraiga en la carpeta `\grid\LE07_L2SP\` los archivos correspondientes a las bandas B1 a B6.

<div align="center"><img src="graph/Windows_RarUncompress1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Del comprimido `\grid\LC09_L2SP\LC09_L2SP_008056_20230203_20230311_02_T1.tar`, extraiga en la carpeta `\grid\LC09_L2SP\` los archivos correspondientes a las bandas B1 a B7.

<div align="center"><img src="graph/Windows_RarUncompress2.png" alt="R.SIGE" width="100%" border="0" /></div>

3. En ArcGIS Pro y ejecutando la herramienta de geo-procesamiento _Data Management Tools / Composite Bands_, componga las bandas satelitales Landsat 7 B3B2B1, guarde el archivo de composición como `\file\grid\LE07_L2SP\L7B3B2B1.tif`. Una vez terminado el proceso, podrá observar la imagen en falso color.

<div align="center"><img src="graph/ArcGISPro_CompositeBands1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Repita el procedimiento anterior para Landsat 9 realizando la composición B4B3B2, guarde el archivo de composición como `\file\grid\LC09_L2SP\L9B4B3B2.tif`

<div align="center"><img src="graph/ArcGISPro_CompositeBands2.png" alt="R.SIGE" width="100%" border="0" /></div>

5. En la tabla de contenido, seleccione la imagen `L7B3B2B1.tif` y desde el menú _Layer_ active la opción de rango dinámico _DRA_ y ajuste o _Stretch Type_ _Esri_. Repita este ajuste para la composición de Landsat 9. Podrá observar la diferencia entre el límite de la zona urbana y el desarrollo rural en 20 años.

<div align="center"><img src="graph/ArcGISPro_RasterLayerDRA1.png" alt="R.SIGE" width="100%" border="0" /></div>

6. Utilizando la herramienta de geo-procesamiento _Data Management Tools / Clip Raster_, recorte las imágenes hasta el límite municipal del MOT, nombre como `\file\grid\LE07_L2SP\L7B3B2B1Clip.tif` y `\file\grid\LC09_L2SP\L9B4B3B2Clip.tif`.

<div align="center"><img src="graph/ArcGISPro_RasterClip1.png" alt="R.SIGE" width="100%" border="0" /></div>


## 3. Identificación cuerpos de agua y vegetación

1. Ejecutando la herramienta de geo-procesamiento _Data Management Tools / Composite Bands_, componga las bandas satelitales Landsat 7 B4B3B2, guarde el archivo de composición como `\file\grid\LE07_L2SP\L7B4B3B2.tif`. Una vez terminado el proceso, podrá observar que los cuerpos de agua aparecen en negro, la vegetación en rojo y las zonas urbanizadas en color gris.

<div align="center"><img src="graph/ArcGISPro_CompositeBands3.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Repita el procedimiento anterior para Landsat 9 realizando la composición B5B4B3, guarde el archivo de composición como `\file\grid\LC09_L2SP\L9B5B4B3.tif`

<div align="center"><img src="graph/ArcGISPro_CompositeBands4.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Utilizando la herramienta de geo-procesamiento _Data Management Tools / Clip Raster_, recorte las imágenes hasta el límite municipal del MOT, nombre como `\file\grid\LE07_L2SP\L7B4B3B2Clip.tif` y `\file\grid\LC09_L2SP\L9B5B4B3Clip.tif`, ajuste la simbología por recorte porcentual y rango dinámico DRA.

<div align="center"><img src="graph/ArcGISPro_RasterClip2.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_RasterClip3.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_RasterClip4.png" alt="R.SIGE" width="100%" border="0" /></div>


## 4. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                                     | Procedimiento                                                                                             |
|:------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| Simbología                                                  | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                   |
| Composición de bandas en imágenes ráster (Composite Bands)  | Herramienta disponible en el _Processing Toolbox / GRASS / Raster / r.composite.                          |
| Recorte de imágenes ráster (Clip Raster)                    | Herramienta disponible en el _Processing Toolbox / GDAL / Raster extraction / Clip raster by mask layer.  |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)  
[:notebook:Herramientas comúnmente utilizadas en QGIS](../QGIS.md)


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre           | Descripción                                                                                            | Geometría    | Registros  | 
|------------------|--------------------------------------------------------------------------------------------------------|--------------|------------| 
| L7B3B2B1.tif     | Composición de bandas Landsat 7 B3B2B2 de imagen en falso color.                                       | (grid)       | n/a        | 
| L9B4B3B2.tif     | Composición de bandas Landsat 9 B4B3B2 de imagen en falso color.                                       | (grid)       | n/a        | 
| L7B3B2B1Clip.tif | Recorte composición de bandas Landsat 7 B3B2B2 de imagen en falso color hasta límite municipal.        | (grid)       | n/a        | 
| L9B4B3B2Clip.tif | Recorte composición de bandas Landsat 9 B4B3B2 de imagen en falso color hasta límite municipal.        | (grid)       | n/a        | 
| L7B4B3B2.tif     | Composición de bandas Landsat 7 B3B2B2 de vegetación y cuerpos de agua.                                | (grid)       | n/a        | 
| L9B5B4B3.tif     | Composición de bandas Landsat 9 B4B3B2 de vegetación y cuerpos de agua.                                | (grid)       | n/a        | 
| L7B4B3B2Clip.tif | Recorte composición de bandas Landsat 7 B3B2B2 de vegetación y cuerpos de agua hasta límite municipal. | (grid)       | n/a        | 
| L9B5B4B3Clip.tif | Recorte composición de bandas Landsat 9 B4B3B2 de vegetación y cuerpos de agua hasta límite municipal. | (grid)       | n/a        | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad      | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P6**  | Realice los análisis de imágenes satelitales contenidos en esta actividad y realice un análisis descriptivo de las diferencias encontradas. Para su zona de estudio deberá buscar imágenes sin cobertura por nubosidad.                                                                                                                                                                                                                             | 
| Avance **P6**  | :compass:Mapa digital impreso _P6-01: Mapa de comparación de imagen en falso color Landsat 7 de 2003 vs Landsat 9 de 2023._<br>Incluir texto descriptivo de diferencias encontradas. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                  | 
| Avance **P6**  | :compass:Mapa digital impreso _P6-02: Mapa de comparación e identificación de cuerpos de agua y vegetaciones Landsat 7 de 2003 vs Landsat 9 de 2023._<br>Incluir texto descriptivo de diferencias encontradas. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                 | 
| Avance **P6** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/composite-bands.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/clip.htm


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas  |
|------------|:-----------------------------------------------------------|--------------------------------------------|:------:|
| 2024.04.02 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4    |
| 2024.09.13 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   6    |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../Reservoir/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/36)  | [Siguiente :arrow_forward:](../RemoteSensingNSC/Readme.md) |
|-----------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------|

[^1]: https://learn.arcgis.com/es/arcgis-imagery-book/chapter2/
[^2]: http://mappinggis.com/2015/05/como-descargar-imagenes-landsat/
[^3]: https://es.wikipedia.org/wiki/Landsat
[^4]: https://es.wikipedia.org/wiki/SPOT
[^5]: https://es.wikipedia.org/wiki/Sentinel_(sat%C3%A9lite)
[^6]: https://en.wikipedia.org/wiki/Ikonos
[^7]: https://surfaceheat.sites.yale.edu/sites/default/files/files/Cirrus%20Band_2.pdf
[^8]: https://www.satimagingcorp.com/satellite-sensors/other-satellite-sensors/landsat-8/
