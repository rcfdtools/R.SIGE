# Modelo digital de elevación - DEM a partir de sensores remotos satelitales
Keywords: `aster-gdem` `srtm` `alos-palsar` `copernicus` `feature-envelope` `extract-multivalues-to-points`

Descargue y procese los siguientes modelos de terreno con cubrimiento hasta el límite de la envolvente de las Subzonas Hidrográficas SZH de proyecto (utilice la envolvente creada para definir la zona de selección de las imágenes satelitales de terreno): ASTER GDEM v3, SRTM, ALOS PALSAR y ESA Copernicus. Cree una red de muestreo regular con nodos cada 1 km utilizando el límite municipal generado previamente a partir del MOT y obtenga en cada punto las elevaciones a partir de estos 4 modelos y el modelo generado a partir de las curvas de nivel del POT, compare y analice con matrices de dispersión múltiple las diferencias encontradas. A partir del DEM Copernicus, genere curvas de nivel categorizadas principales cada 50 metros y secundarias cada 10 metros, compare y analice las diferencias con respecto a las curvas del POT.

<div align="center"><img src="graph/DEMSatellite.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Descarga e integrar modelos digitales de elevación a partir de información de sensores remotos satelitales.
* Comparar y entender las diferencias entre las elevaciones obtenidas a partir de los modelos digitales de elevación Aster, SRTM, Alos Palsar y Copernicus.
* Crear curvas de nivel a partir de DEM satelitales.


## Requerimientos

* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../SZH/Readme.md): Análisis de sub-zonas hidrográficas.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:man_technologist:Usuario](https://urs.earthdata.nasa.gov/): Creación de cuenta de usuario NASA. 
* [:man_technologist:Usuario](https://ers.cr.usgs.gov/): Creación de cuenta de usuario USGS.
* [:man_technologist:Usuario:](https://portal.opentopography.org/newUser): Creación de cuenta de usuario en Open Topography. 


## 1. Creación de máscara para obtención de modelos digitales de elevación - DEM 

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _DEMSatellite_ y establezca el CRS 9377. Agregue al mapa la capa del límite territorial municipal generado a partir del Modelo de Ocupación Territorial - MOT disponible en la ruta `\file\gdb\SIGE.gdb\SIGE\Mpio25899_MOT2013` y ajuste la simbología a contorno rojo sin relleno.  

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Utilizando la herramienta de geo-procesamiento _Data Management Tools / Feature Envelope To Polygon_, genere un polígono envolvente alrededor del límite municipal, nombre como `\file\gdb\SIGE.gdb\SIGE\Mpio25899_MOT2013_Envelope`.

<div align="center"><img src="graph/ArcGISPro_FeatureEnvelopeToPolygon1.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Utilizando la herramienta de geo-procesamiento _Analysis Tools / Buffer_, cree un polígono aferente externo de 2500 metros alrededor de la envolvente obtenida. Nombre la capa resultante como `\file\gdb\SIGE.gdb\SIGE\Mpio25899_MOT2013_Envelope_Buffer2500m`.

> Este polígono aferente será utilizado para definir el límite de descarga de los modelos digitales de elevación y hemos utilizado 2500 metros para que el terreno obtenido cubra los drenajes próximos que fluyen hacia dentro del área municipal evaluada.

<div align="center"><img src="graph/ArcGISPro_Buffer1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Desde la tabla de contenido y utilizando la herramienta _Export Features_, exporte la capa `Mpio25899_MOT2013_Envelope_Buffer2500m` en un archivo de formas shapefile dentro de la carpeta `\file\shp`. Utilice el mismo nombre de la clase de entidad contenida en la GDB y en entornos o _Environments_ establezca el sistema 4326 correspondiente a GCS_WGS_1984.

<div align="center"><img src="graph/ArcGISPro_ExportFeatures1.png" alt="R.SIGE" width="50%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_ExportFeatures2.png" alt="R.SIGE" width="50%" border="0" /></div>

5. 







## 2. Modelo digital de elevación NASA ASTER GDEM







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

| [:arrow_backward: Anterior](../DEMContour/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|----------------------------------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 